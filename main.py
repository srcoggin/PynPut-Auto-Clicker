from PyQt5.QtWidgets import QMessageBox, QMainWindow
from UserInterface import Ui_AutoClicker

import time  
import threading  
from pynput.mouse import Button, Controller  
from pynput.keyboard import Listener, KeyCode 

# button = Button.left  
# delay = 0.001  
# startStopButton = KeyCode(char='1')  
# terminateButton = KeyCode(char='2')
 

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_AutoClicker()
        self.ui.setupUi(self.main_win)
       
        self.ClickProgram = False
        self.ui.About_Me_Button.clicked.connect(self.About_Me)
        # self.ui.Exit_Button.clicked.connect(ClickMouse.exitScript)
        self.ui.Save_Info_Button.clicked.connect(self.Save_Info)
        # self.ui.Start_Button.clicked.connect(ClickMouse.startMouseClick)

    def About_Me(self):
        msg = QMessageBox()
        msg.setText('''
Thank you for using my Automatic Mouse Clicker!
I hope it helps you on your cookie clicker journey, or whatever clicker game you are playing.
This application was Coded and Developed by Will Coggins in one boring Literature 11 class
Please enjoy my other works such as "FIA2", "FIA1", or "Brad-File".
All of which can be found on my github @srcoggin. 
Please follow me, and start my Repos! 
''')
        msg.setWindowTitle("About Me!")
        msg.setStandardButtons(msg.close)
        msg.exec()

    def Save_Info(self):
        Delay = self.ui.Delay_Time_Input.text()
        Start_Key = self.ui.Start_Key_Input.text()
        Stop_Key = self.ui.Stop_Key_Input.text()
        return Delay, Start_Key, Stop_Key


# class ClickMouse(threading.Thread):  
#     def __init__(self, delay, button):  
#         super(ClickMouse, self).__init__()  
#         self.delay = delay 
#         self.button = button 
#         self.running = False  
#         self.program_running = False  

#     def startMouseClick(self):
#         self.running = True  
      
#     def stopMouseClick(self):  
#         self.running = False  
      
#     def exitScript(self):  
#         self.stopMouseClick()  
#         self.program_running = False  

#     def run(self):  
#         while self.program_running:  
#             while self.running:  
#                 mouse.click(self.button)  
#                 time.sleep(self.delay)  
#             time.sleep(0.1)  

# mouse = Controller()  
# clickThread = ClickMouse(delay, button)  
# clickThread.start()  


# def on_press(key):  
#     if key == startStopButton:  
#         if clickThread.running:  
#             clickThread.stopMouseClick()  
#         else:  
#             clickThread.startMouseClick()  
#     elif key == terminateButton:  
#         clickThread.exitScript()  
#         listener.stop()  
  
  
# with Listener(on_press=on_press) as listener:  
#     listener.join()