import time  
import threading  
from pynput.mouse import Button, Controller  
from pynput.keyboard import Listener, KeyCode 


button = Button.left  
delay = 0.001  
startStopButton = KeyCode(char='1')  
terminateButton = KeyCode(char='2') 

class ClickMouse(threading.Thread):  
    def __init__(self, delay, button):  
        super(ClickMouse, self).__init__()  
        self.delay = delay 
        self.button = button 
        self.running = False  
        ClickProgram = self.program_running
        self.program_running = False  

    def startMouseClick(self):
        self.running = True  
      
    def stopMouseClick(self):  
        self.running = False  
      
    def exitScript(self):  
        self.stopMouseClick()  
        self.program_running = False  

    def run(self):  
        while self.program_running:  
            while self.running:  
                mouse.click(self.button)  
                time.sleep(self.delay)  
            time.sleep(0.1)  

mouse = Controller()  
clickThread = ClickMouse(delay, button)  
clickThread.start()  


def on_press(key):  
    if key == startStopButton:  
        if clickThread.running:  
            clickThread.stopMouseClick()  
        else:  
            clickThread.startMouseClick()  
    elif key == terminateButton:  
        clickThread.exitScript()  
        listener.stop()  
  
  
with Listener(on_press=on_press) as listener:  
    listener.join()