from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from UserInterface import Ui_AutoClicker
import  sys
import os
import time
import pyautogui


class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_AutoClicker()
        self.ui.setupUi(self.main_win)
        
       

        self.ui.About_Me_Button.clicked.connect(self.About_Me)
        self.ui.Start_Button.clicked.connect(self.run)
        self.ui.Exit_Button.clicked.connect(self.exit)
     

    def exit(self):
        exit()

    def About_Me(self):
        msg = QMessageBox()
        msg.setText('''
Thank you for using my Automatic Mouse Clicker!
I hope it helps you on your cookie clicker journey, or whatever clicker game you are playing.
This application was Coded and Developed by Will Coggins 
in one boring Literature 11 class
Please enjoy my other works such as "FIA2", "FIA1", or "Brad-File".
All of which can be found on my github @srcoggin. 
Please follow me, and start my Repos! 
''')
        msg.setWindowTitle("About Me!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def show(self):
        self.main_win.show()


    def click(self):
        num2 = int(self.ui.Delay_Time_Input.text())
        time.sleep(num2)
        pyautogui.click()
        self.ui.Delay_Time_Input.clear()
        self.ui.num_of_clicks.clear()

    def run(self):
        num = int(self.ui.num_of_clicks.text())
        time.sleep(5)
        for i in range(num):
            self.click()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())