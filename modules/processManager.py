"""This class provides functionality to delete all the Android applications using ADB commands."""
import subprocess
from config import adb_path

class processManager():
    def rename(self, array):
        for i in range(len(array)):
            if array[i].startswith('package:'):
                array[i] = array[i][len('package:'):]

        for i in range(len(array)):
            element = array[i]
            word_index = element.find(".apk=")
            if word_index != -1:
                array[i] = element[word_index + 5:]

        return array
    

    def delete(self, process):
        if process == "":
            return
        if process == "android":
            return
        result = subprocess.run([adb_path, "shell", "pm", "uninstall", "-k", "--user", "0" , f"{process}"], text=True, capture_output=True, shell=False)
        if "no devices/emulators found" in result.stdout:
            return print(f"The device or the emulator was disconnected, the package {process} is still on the device")
        return print(f'{process} was successfully deleted !')