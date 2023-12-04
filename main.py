import pygame
pygame.init()
from menu import Menu
import subprocess
from guide import Guide



def main_menu():
    menu = Menu()
    guide = None

    while True:
        menu.loop()
        if menu.pvp:
            menu.init_btn()
            file_to_run = "pvp.py"
            try:
                result = subprocess.run(["python", file_to_run], capture_output=True, text=True, check=True)
                print("Output:", result.stdout)
            except subprocess.CalledProcessError as e:
                print("Error:", e.stderr)
            if menu.pvp : del menu.pvp
            menu.pvp = None
            menu.running = True
            
        menu.loop()
        if menu.pve:
            menu.init_btn()
            file_to_run = "pve.py"
            try:
                result = subprocess.run(["python", file_to_run], capture_output=True, text=True, check=True)
                print("Output:", result.stdout)
            except subprocess.CalledProcessError as e:
                print("Error:", e.stderr)
            if menu.pve : del menu.pve
            menu.pve = None
            menu.running = True
                    
        if menu.guide:
            menu.init_btn()
            guide = Guide()
            guide.loop()
            if guide : del guide
            guide = None
            menu.running = True
          


main_menu()