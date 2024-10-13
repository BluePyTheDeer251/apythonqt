# This Python file uses the following encoding: utf-8
import sys
import numpy as np
from PySide6.QtWidgets import QApplication

print "Yeah, u wont read this, ever."
def AppOpening():
    if app.exec()  == True:
        print("Welcome!")

np #So no warnings arrive (read below)
 #I have no idea what I'm doing, but I love it
AppOpening(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ...
    sys.exit(app.exec())
