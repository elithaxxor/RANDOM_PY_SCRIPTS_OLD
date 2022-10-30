import threading
import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode as keyboard
#
delay = 0.01
button = Button.left
start_stop_key = KeyCode(char='a')
exit_key = KeyCode(char='e')

class Clickmouse(threading.Thread):
    def __init__ (self, delay, button):
        super(ClickMouse, self).__init__
        self.delay = delay
        self.butto = button
        self.running  = False
        self.program_running = True

    def start_running(self):
        self.running = True
    def stop_running(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.stop_clicking()
    elif key == exit_key:
        click_thread.exit()
        listner.stop()



with Listener(on_press=on_press) as listiner:
    listiner.join()
