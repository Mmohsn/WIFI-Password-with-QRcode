import subprocess
import qrcode

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print("Enter Network Name")
ssid = input()
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    if ssid in i: 
        print("Your Password is =" , results[0] ,"\n")
        print('Do you want QR-Code ? , Press y for yes - n for no')
        q = input()
        if q == "y" :
            img = qrcode.make(str(results[0]))
            img.save(str(i)+'.png')
            print("QR Code Image is Generated Sucessfully")
        elif q == "n":
            print("Thanks")
            break
        break