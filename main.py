import customtkinter as ctk

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
    if method == "Wireless Debugging":
        root.geometry("300x410")
        ip_label.pack()
        ip_input.pack()
        port_label.pack()
        port_input.pack()
        yes_radio.pack(pady=7, padx=125)
        no_radio.pack(pady=5, padx=125)
        ip_pair_label.pack()
        ip_pair_input.pack()
        port_pair_label.pack()
        port_pair_input.pack()
        wireless_button.pack(pady=15)
        usb_button.pack_forget()

def isPaired():
    if is_paired.get() == True:
        ip_pair_input.delete(0, 'end')
        port_pair_input.delete(0, 'end')
        ip_pair_input.configure(state="disabled")
        port_pair_input.configure(state="disabled")
    elif is_paired.get() == False:
        ip_pair_input.configure(state="normal")
        port_pair_input.configure(state="normal")

first_label = ctk.CTkLabel(root, text="How do you want to connect to the target ?")
combobox_values = ["USB Debugging", "Wireless Debugging"]
combobox = ctk.CTkComboBox(root, values=combobox_values, width=170, command=displayedMethod)
usb_button = ctk.CTkButton(root, text="Start softbricking")

wireless_button = ctk.CTkButton(root, text="Start wireless softbricking")
ip_label = ctk.CTkLabel(root, text="IP Address:")
ip_input = ctk.CTkEntry(root)
port_label = ctk.CTkLabel(root, text="Port:")
port_input = ctk.CTkEntry(root)
is_paired = ctk.BooleanVar()
yes_radio = ctk.CTkRadioButton(root, text="Yes", value=True, variable=is_paired, command=isPaired)
no_radio = ctk.CTkRadioButton(root, text="No", value=False, variable=is_paired, command=isPaired)
ip_pair_label = ctk.CTkLabel(root, text="IP Address for pairing:")
ip_pair_input = ctk.CTkEntry(root)
port_pair_label = ctk.CTkLabel(root, text="Port for pairing:")
port_pair_input = ctk.CTkEntry(root)

is_paired.set(True)

first_label.pack()
combobox.pack()
combobox.set("USB Debugging")
usb_button.pack(pady=10)

root.mainloop()