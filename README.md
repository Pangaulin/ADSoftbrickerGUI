
# ADSoftbrickerGUI

This software is for educational purposes only, I am not responsible of any damage made on your phone. This software was tested on Windows 10 and Windows 11 with Python 3.12, on a Samsung A03 and an emulator (LDPlayer).

This project adds a GUI to [ADSoftbricker](https://github.com/Pangaulin/ADSoftbricker) project made by me.

## How to start the program

In a command line, type :

```bash
  git clone https://github.com/Pangaulin/ADSoftbrickerGUI
  cd ADSoftbrickerGUI
  python main.py
```
Or : 
- Download source code
- Extract it with WinRAR, 7-Zip, on an other data compression and archiving software
- Launch the **start.bat** file

Then, enjoy !
## How to use USB Debug
After starting the software, you have a list with two choices
```bash
- USB Debug
- Wireless Debug 
```
If you choose USB debug, check if it's activated on your phone, here is a [tutorial](https://developer.android.com/studio/debug/dev-options?hl=en#enable). 

After this, plug the device to you computer, and press **Start softbricking**, and enjoy !
## How to use Wireless Debug

After starting the software, you have a list with two choices
```bash
- USB Debug 
- Wireless Debug
```

If you choose Wireless debug, follow this [tutorial](https://developer.android.com/studio/debug/dev-options?hl=en#enable), but enable the "Use wireless debugging" option, then click on it. If you have already paired your device, write the IP adress, in this case "192.168.1.242", then the port, in this case "38157", select the button **Yes** and press **Start wireless softbricking**, then enjoy !

![alt text](https://developer.android.com/static/studio/images/run/adb_wifi-wireless_debugging.png)

If you have not paired your device before, write IP address and port, like in the previous step, select the button **No**, then select "Pair device with pairing code" on your phone. 

Write the IP address in **IP address for pairing** and the port in **Port for pairing**. 
Press **Start wireless softbricking** and write the six digit code on your phone. Then enjoy !

**⚠️ WARNING : YOUR DEVICE NEED TO BE ON THE SAME NETWORK AS THE COMPUTER ⚠️**

## License

See the license [here](https://github.com/Pangaulin/ADSoftbrickerGUI/blob/main/LICENSE)
