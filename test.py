
from pystyle import * 
from pystyle import Write, Colors

name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Nice to meet you, {name}!", Colors.blue_to_green, interval=0.05)      

print(Center.XCenter("Hello, Welcome to Pystyle."))