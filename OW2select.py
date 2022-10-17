from PySimpleGUI import *
import pyautogui
import time
import keyboard  
char = []
on = True
diva = [342,829]
widow =[1239,888]
reaper = [787,894]
groundhog = [342,896]
import os
os.system('cls')
print("""\u001b[32m

 ██████╗██╗  ██╗ █████╗ ██████╗  █████╗  ██████╗████████╗███████╗██████╗     ███████╗███████╗██╗     ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║███████║██████╔╝███████║██║        ██║   █████╗  ██████╔╝    ███████╗█████╗  ██║     █████╗  ██║        ██║   ██║   ██║██████╔╝
██║     ██╔══██║██╔══██║██╔══██╗██╔══██║██║        ██║   ██╔══╝  ██╔══██╗    ╚════██║██╔══╝  ██║     ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║╚██████╗   ██║   ███████╗██║  ██║    ███████║███████╗███████╗███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                               
 """, end = "")

print("-BY YANIS")

input("\u001b[35;1mpress y to start the character selector: ")

  
# GUI Layout
layout = [[Txt(''  * 10)],
          [Text('', size = (15, 1), font = ('Helvetica', 18),
                text_color = 'black', key = 'input')],
          [Txt(''  * 10)],
          [ReadFormButton('diva'), ReadFormButton('widowmaker')],
          [ReadFormButton('reaper'), ReadFormButton('groundhog')],
          [ReadFormButton('QUIT')]
          ]
  
# Set PySimpleGUI
form = FlexForm('overwatch selector by yanis', default_button_element_size = (5, 2),
                auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)
  
# Result Value
Result = ''
  
# Make Infinite Loop
while on == True:

   
    # Button Values
    button, value = form.Read()
      
    # Check Press Button Values
    if button == 'diva':
       char = diva
       on = False
    if button == 'widowmaker':
       char = widow
       on = False
    if button == 'reaper':
       char = reaper
       on = False
    if button == 'groundhog':
       char = groundhog
       on = False

    if button == 'QUIT':
        quit()
    




while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            time.sleep(1)
            pyautogui.moveTo(char[0],char[1])
            pyautogui.mouseDown()
            time.sleep(0.01)
            pyautogui.mouseUp() 
            time.sleep(0.3)
            pyautogui.moveTo(950,986)
            pyautogui.mouseDown()
            time.sleep(0.01)
            pyautogui.mouseUp()
            time.sleep(3)
            quit()
            
    except:
        break 
