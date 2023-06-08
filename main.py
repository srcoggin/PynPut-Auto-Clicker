from PyQt5.QtWidgets import QMessageBox, QMainWindow
from UserInterface import Ui_AutoClicker
from ClickMouse import ClickMouse

 
clickmouse = ClickMouse()
class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_AutoClicker()
        self.ui.setupUi(self.main_win)
       

        self.ui.About_Me_Button.clicked.connect(self.About_Me)
        self.ui.Exit_Button.clicked.connect(clickmouse.exitScript)
        self.ui.Save_Info_Button.clicked.connect(self.Save_Info)
        self.ui.Start_Button.clicked.connect(self.Start_Click)

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

    def Start_Click(self):
        ClickProgram = True

    def Save_Info(self):
        Delay = self.ui.Delay_Time_Input.text()
        Start_Key = self.ui.Start_Key_Input.text()
        Stop_Key = self.ui.Stop_Key_Input.text()
        return Delay, Start_Key, Stop_Key


  