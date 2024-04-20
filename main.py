import re
import os
import time
import subprocess
from zipfile import ZipFile
from modules.processManager import processManager

import customtkinter as ctk
import CTkMessagebox
from config import adb_path

root = ctk.CTk()
root.geometry("300x110")
root.title("ADSoftbricker")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue") 

def displayedMethod(self):
    method = combobox.get()
    if method == "USB Debugging":
        root.geometry("300x110")
        usb_button.pack(pady=10)
        wireless_button.pack_forget()
        ip_label.pack_forget()
        ip_input.pack_forget()
        port_label.pack_forget()
        port_input.pack_forget()
        ip_pair_label.pack_forget()
        ip_pair_input.pack_forget()
        port_pair_label.pack_forget()
        port_pair_input.pack_forget()
        yes_radio.pack_forget()
        no_radio.pack_forget()
        ispaired_label.pack_forget()
        returnlabel.pack_forget()
    if method == "Wireless Debugging":
        root.geometry("670x500")
        ip_label.pack()
        ip_input.pack()
        port_label.pack()
        port_input.pack()
        ispaired_label.pack(pady=3)
        yes_radio.pack(pady=4, padx=310, anchor="center")
        no_radio.pack(pady=5, padx=310, anchor="center")
        ip_pair_label.pack()
        ip_pair_input.pack()
        port_pair_label.pack()
        port_pair_input.pack()
        wireless_button.pack(pady=10)
        usb_button.pack_forget()

def isPaired():
    if is_paired.get() == True:
        ip_pair_input.delete(0, 'end')
        port_pair_input.delete(0, 'end')
        ip_pair_input.configure(placeholder_text="XXX.XXX.X.XX")
        port_pair_input.configure(placeholder_text="XXXXX")
        ip_pair_input.configure(state="disabled")
        port_pair_input.configure(state="disabled")
    elif is_paired.get() == False:
        ip_pair_input.configure(state="normal")
        port_pair_input.configure(state="normal")

def usbConfirmation():
    confirmation = CTkMessagebox.CTkMessagebox(title="Are you sure ?", message="Do you really want to softbrick your device ? This can cause huge damage to your phone.\nThe process may seem unresponsive during operation.",
                                 icon="warning", option_1="Yes", option_2="No")
    response = confirmation.get()
    if (response=="Yes"):
        usb()
    else:
        return

def wirelessConfirmation():
    confirmation = CTkMessagebox.CTkMessagebox(title="Are you sure ?", message="Do you really want to softbrick your device ? This can cause huge damage to your phone.\nThe process may seem unresponsive during operation.",
                                 icon="warning", option_1="Yes", option_2="No")
    response = confirmation.get()
    if (response=="Yes"):
        wireless()
    else:
        return
    
def usb():
    get_process = subprocess.run([adb_path, "shell", "pm", "list", "packages", "-f"], capture_output=True, text=True, shell=False)
    process_array = get_process.stdout.split('\n')

    process_array = processManager().rename(process_array)
    is_up = 1
    for i in range(len(process_array)):
            delete_return = processManager().delete(process_array[i])
            if delete_return == 0:
                is_up = 0
                break
    if is_up == 0:
        returnlabel.configure(text="The device was disconnected while deleting the packages, please reconnect it, and retry")
        returnlabel.pack()
        return
    else:
        subprocess.run([adb_path, "reboot"])
        CTkMessagebox.CTkMessagebox(root, title="Success !", message=f"The USB device was successfully softbricked")

def wireless():
    root.geometry("670x500")
    regex_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    regex_port = r'^([0-9]|[1-9][0-9]{1,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$'
    if not re.match(regex_ip, ip_input.get()):
        returnlabel.configure(text="The IP isn't in the correct format", text_color="red")
        returnlabel.pack()
        return
    elif not re.match(regex_port, port_input.get()):
        returnlabel.configure(text="The port isn't in the correct format", text_color="red")
        returnlabel.pack()
        return
    else:
        pass

    ip = ip_input.get()
    port = port_input.get()

    if is_paired.get() == False:
        if not re.match(regex_ip, ip_pair_input.get()):
           returnlabel.configure(text="The pair IP isn't in the correct format", text_color="red")
           returnlabel.pack()
           return
        elif not re.match(regex_port, port_pair_input.get()):
            returnlabel.configure(text="The pair port isn't in the correct format", text_color="red")
            returnlabel.pack()
            return
        else:
            pair_ip = ip_pair_input.get()
            pair_port = port_pair_input.get()
            paircode = pairPopup()
            regex_pair_code = r'\d{6}$'
            if paircode is None:
                root.geometry("670x500")
                returnlabel.pack_forget()
                return
            elif not re.match(regex_pair_code, paircode):
                returnlabel.configure(text="The pair code is not in the correct format")
                returnlabel.pack()
                return
            else:
                pair_return = subprocess.run([adb_path, 'pair', f'{pair_ip}:{pair_port}', paircode], shell=False, capture_output=True, text=True)
                if f"Successfully paired to {pair_ip}:{pair_port}" in pair_return.stdout:
                    print(pair_return.stdout)
                    returnlabel.configure(text=f"The device {pair_ip}:{pair_port} was successfully paired !", text_color="black")
                    returnlabel.pack()
                else:
                    print(pair_return.stdout)
                    returnlabel.configure(text="An error has occured while pairing the device, please check if the informations you gave are correct", text_color="red")
                    returnlabel.pack()
                    return

    time.sleep(3)
    connect_return = subprocess.run([adb_path, "connect", f"{ip}:{port}"], shell=False, text=True, capture_output=True)
    if f"connected to {ip}:{port}" in connect_return.stdout or f"already connected to {ip}:{port}" in connect_return.stdout:
        returnlabel.configure(f"Successfully connected to {ip}:{port} !", text_color="black")
        returnlabel.pack()
    else:
        print(connect_return.stdout, connect_return.stderr)
        returnlabel.configure(text="An error has occured while connecting to the device, please check if the information you gave are correct,\n and check if the phone and the computer are on the same network", text_color="red")
        returnlabel.pack()
        return
    
    get_process = subprocess.run([adb_path, "-s", f"{ip}:{port}", "shell", "pm", "list", "packages", "-f"], capture_output=True, text=True, shell=False)
    process_array = get_process.stdout.split('\n')

    process_array = processManager().rename(process_array)
    is_up = 1
    for i in range(len(process_array)):
            delete_return = processManager().delete(process_array[i])
            if delete_return == 0:
                is_up = 0
                break
    if is_up == 0:
        returnlabel.configure(text="The device was disconnected while deleting the packages, please reconnect it, and retry")
        returnlabel.pack()
        return
    
    subprocess.run([adb_path, "reboot"])
    CTkMessagebox.CTkMessagebox(root, title="Success !", message=f"The device {ip}:{port} was successfully softbricked")

def pairPopup():
    popup = ctk.CTkInputDialog(text="What is the six digit pair code ?", title="Pair code prompt")
    paircode = popup.get_input()
    return paircode
    
returnlabel = ctk.CTkLabel(root, text="", text_color="red")
returnlabel.configure(width=20, height=10)

first_label = ctk.CTkLabel(root, text="How do you want to connect to the target ?")
combobox_values = ["USB Debugging", "Wireless Debugging"]
combobox = ctk.CTkComboBox(root, values=combobox_values, width=170, command=displayedMethod)
usb_button = ctk.CTkButton(root, text="Start softbricking", command=usbConfirmation)

wireless_button = ctk.CTkButton(root, text="Start wireless softbricking", command=wirelessConfirmation)
ip_label = ctk.CTkLabel(root, text="IP Address:")
ip_input = ctk.CTkEntry(root, placeholder_text="XXX.XXX.X.XX")
port_label = ctk.CTkLabel(root, text="Port:")
port_input = ctk.CTkEntry(root, placeholder_text="XXXXX")
is_paired = ctk.BooleanVar()
ispaired_label = ctk.CTkLabel(root, text="Is the device paired to the application ?")
yes_radio = ctk.CTkRadioButton(root, text="Yes", value=True, variable=is_paired, command=isPaired)
no_radio = ctk.CTkRadioButton(root, text="No", value=False, variable=is_paired, command=isPaired)
ip_pair_label = ctk.CTkLabel(root, text="IP Address for pairing:")
ip_pair_input = ctk.CTkEntry(root, placeholder_text="XXX.XXX.X.XX")
port_pair_label = ctk.CTkLabel(root, text="Port for pairing:")
port_pair_input = ctk.CTkEntry(root, placeholder_text="XXXXX")
ip_pair_input.configure(state="disabled")
port_pair_input.configure(state="disabled")

is_paired.set(True)

first_label.pack(pady=4)
combobox.pack()
combobox.set("USB Debugging")
usb_button.pack(pady=10)

if not os.path.exists('modules\\platform-tools'):
            print("Downloading Android Debug Bridge")
            subprocess.run(["curl", "https://dl.google.com/android/repository/platform-tools-latest-windows.zip?hl=fr", "-o", "modules\\platform-tools.zip"])
            with ZipFile('modules\\platform-tools.zip', 'r') as zip:
                zip.extractall(path="modules")
            os.remove("modules\\platform-tools.zip")

root.mainloop()