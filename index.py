from random import *
from time import *
from tictactoe import TicTacToe
from pong import pong_game
import os
from pystyle import *

name = os.name
if name == "nt":
    command = "cls"

elif name== "posix":
    command = "clear"

banner1 = """              
                        .__          __    __          
    _______  ____  __ __|  |   _____/  |__/  |_  ____  
    \_  __ \/  _ \|  |  \  | _/ __ \   __\   __\/ __ \ 
    |  | \(  <_> )  |  /  |_\  ___/|  |  |  | \  ___/ 
    |__|   \____/|____/|____/\___  >__|  |__|  \___  >  by @Lluciocc
                                 \/                \/  
                               
"""

banner2 = """
     ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄     ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄ 
█   █   █ █      █ █   █    █ █    █     ▐  ▄▀   ▐ █    █  ▐ █    █  ▐ ▐  ▄▀   ▐ 
▐  █▀▀█▀  █      █ ▐  █    █  ▐    █       █▄▄▄▄▄  ▐   █     ▐   █       █▄▄▄▄▄  
 ▄▀    █  ▀▄    ▄▀   █    █       █        █    ▌     █         █        █    ▌  
█     █     ▀▀▀▀      ▀▄▄▄▄▀    ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄    ▄▀        ▄▀        ▄▀▄▄▄▄   
▐     ▐                         █         █    ▐   █         █          █    ▐   
                                ▐         ▐        ▐         ▐          ▐        by @Lluciocc
                                
"""
banner3 = """
 ██▀███   ▒█████   █    ██  ██▓    ▓█████▄▄▄█████▓▄▄▄█████▓▓█████ 
▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██▒    ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ 
▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▒██░    ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   
▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██░    ▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ 
░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ░██████▒░▒████▒ ▒██▒ ░   ▒██▒ ░ ░▒████▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░     ▒ ░░   ░░ ▒░ ░
  ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░ ░ ░  ░   ░        ░     ░ ░  ░
  ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░   ░ ░      ░    ░        ░         ░   
   ░         ░ ░     ░         ░  ░   ░  ░                    ░  ░      by @Lluciocc

"""

banner4 = """
██████╗  ██████╗ ██╗   ██╗██╗     ███████╗████████╗████████╗███████╗
██╔══██╗██╔═══██╗██║   ██║██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║   ██║██║   ██║██║     █████╗     ██║      ██║   █████╗  
██╔══██╗██║   ██║██║   ██║██║     ██╔══╝     ██║      ██║   ██╔══╝  
██║  ██║╚██████╔╝╚██████╔╝███████╗███████╗   ██║      ██║   ███████╗
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝    by @Lluciocc
"""
pong_banner = """
██████╗  ██████╗ ███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗  ██║██╔════╝ 
██████╔╝██║   ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║   ██║██║╚██╗██║██║   ██║
██║     ╚██████╔╝██║ ╚████║╚██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝                             
"""

tictactoe_banner = """
████████╗██╗ ██████╗████████╗ █████╗  ██████╗████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║        ██║   ███████║██║        ██║   ██║   ██║█████╗  
   ██║   ██║██║        ██║   ██╔══██║██║        ██║   ██║   ██║██╔══╝  
   ██║   ██║╚██████╗   ██║   ██║  ██║╚██████╗   ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                                                 
"""

banners = [banner1, banner2, banner3, banner4]
def banner():
    os.system(command)
    print(Colorate.Horizontal(Colors.blue_to_green ,(Center.XCenter(choice(banners)))))
banner()

Write.Print("Type 'play' or 'roulette' to play.", Colors.purple_to_blue, interval=0.05)
print(" ")

terminal_alive = True

def help_message():
    print(Colorate.Horizontal(Colors.green_to_red, "Type 'play' to play the game."))
    print(Colorate.Horizontal(Colors.green_to_red, "Type 'ping' to pong."))
    print(Colorate.Horizontal(Colors.green_to_red, "Type 'help' to show this message."))
    
    print(Colorate.Horizontal(Colors.green_to_red, "Good Game !"))
    print(Colorate.Horizontal(Colors.green_to_red, "(Credit @Lluciocc)"))

def restart():
    print(Colorate.Horizontal(Colors.cyan_to_blue, "Do you want restart ? (y/n)"))
    terminal_restart = input(Colorate.Horizontal(Colors.green_to_red, ">>>>     "))
    if terminal_restart == "yes":
        os.system(command)
        banner()
        game_roulette()
    elif terminal_restart == "y":
        os.system(command)
        banner()
        game_roulette()
    elif terminal_restart == "no":
        Colorate.Horizontal("okay",Colors.green)
        os.system(command)
        banner()
    elif terminal_restart == "n":
        Colorate.Horizontal("okay",Colors.green)
        os.system(command)
        banner()
    else:
        Write.Print("ERROR ", Colors.red_to_yellow, interval=0.05)
        restart()

def game_roulette():
    roulette = randint(1,6)
    choix = int(Write.Input("Pick a number:    ", Colors.red_to_purple, interval=0.05))
    if choix <= 6:
        if choix == roulette:
            Write.Print( "PAN !", Colors.red_to_yellow, interval=0.05)
            print(" ")
            print(" ")
            Write.Print(".   .   .", Colors.red_to_yellow, interval=0.10)
            print(" ")
            print(" ")
            Write.Print("You're dead !", Colors.red_to_yellow,  interval=0.05)
            print(" ")
            restart()
        elif choix != roulette:
            Write.Print("PAN !", Colors.red_to_yellow,  interval=0.05)
            print(" ")
            print(" ")
            Write.Print(".   .   .", Colors.red_to_yellow, interval=0.10)
            print(" ")
            print(" ")
            Write.Print("You're alive !", Colors.green_to_white, interval=0.05)
            print(" ")
            restart()
    else:
        Write.Print("ERROR ", Colors.red_to_yellow, interval=0.05)
        print(" ")
        Write.Print("Please pick a number between 1 and 6.", Colors.red_to_yellow, interval=0.05)
        print(" ")
        print(" ")
        game_roulette()
    
    

while terminal_alive == True:
    terminal_input = Write.Input(">>   ", Colors.blue_to_cyan, interval=0.05)

    if terminal_input == "h":
        help_message()
    elif terminal_input == "help":
        help_message()
    elif terminal_input == "start":
        os.system(command)
        banner()
        game_roulette()
    elif terminal_input == "play":
        os.system(command)
        banner()
        game_roulette()
    elif terminal_input == "roulette":
        os.system(command)
        banner()
        game_roulette()
    elif terminal_input == "tictactoe":
        print(tictactoe_banner)
        tictactoe = TicTacToe()
        tictactoe.start()
    elif terminal_input == "pong":
        print(pong_banner)
        pong_game()
    elif terminal_input == "ping":
        Write.Print("Pong !", Colors.black_to_blue, interval=0.05)
        print(" ")
        Write.Print("You can also try the command 'pong'", Colors.all_colors, interval=0.05)
    elif terminal_input == "quit":
        os.system(command)
        break
    else:
        Write.Print("ERROR ", Colors.red_to_yellow, interval=0.05)
        print(" ")
        Write.Print("Type 'help' for help. ", Colors.red_to_yellow, interval=0.05)
        print(" ")