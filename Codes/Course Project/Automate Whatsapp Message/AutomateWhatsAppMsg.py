import pywhatkit
import time
import pyautogui
import keyboard as k

#number1 = input("Enter the Number (with Country Code): ")
#string1 = input("Enter the Message to be Sent: ")
#hour1 = input("Enter Hour (24 Hour Format): ")
#int(hour1)
#min1 = input("Enter Minutes: ")
#int(min1)

pywhatkit.sendwhatmsg("+91"+input("Enter Mobile Number: "), input("Enter Message: "), int(input("Enter the Hour (24 Hr Format): ")), int(input("Enter the minutes: ")))
pyautogui.click(1050, 950)
time.sleep(20)
k.press_and_release('enter')