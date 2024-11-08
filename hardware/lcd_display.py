from hardware.lcd_driver import LcdDriver
import time

class LCD_Display:
    def __init__(self, is_backlight=True, is_disabled=False):
        self.is_disabled = is_disabled
        if is_disabled:
            print("LCD is disabled")
            return

        self.LCD = LcdDriver(pi_rev=2, i2c_addr=0x27, backlight=is_backlight)

    def printTerminalMessage(self, message, headerText=""):
          print(f"\n---------\n{headerText}\n{message}\n---------\n")



    def printMessageWithDelay(self, duration_sec, message, headerText=""):
        if self.is_disabled:
            self.printTerminalMessage(message, headerText)
            return

        self.printMessage(message, headerText)
        time.sleep(duration_sec)
        self.LCD.clear()

    def printMessage(self, message, headerText=""):
        if self.is_disabled:
            self.printTerminalMessage(message, headerText)
            return

        if len(headerText) > 0:
            self.LCD.message(headerText, line=1)

        self.LCD.message(message, line=2)

    def clear(self):
        if self.is_disabled:
            return

        self.LCD.clear()
