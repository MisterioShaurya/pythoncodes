import datetime
import time
from plyer import notification
userpass = int(input("Enter your 4 digit password here: "))
passw = 0
while userpass != passw:
    print(passw)
    passw = passw +1
if userpass == passw:
    notification.notify(
        title = "Password Cracked!".format(datetime.date.today()),
        message = f"Password is: {passw}",
        app_icon = "D:/icons/Slogografientnobgico.ico",
        timeout = 10
        )
print(f"Your password is: {passw}")
