from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import sys, os

class MapleUI:
    """
    Copyright © 2025 Killerqubr & flizc. All rights reserved.   
    Python 3.10.8 with PyQt 5.15.9.
    """
    __version__ = "Indev 1.5"

    def __init__(self):
        # Application-Attribute must be set before App-Instantiation.
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
        self.app = QApplication(sys.argv)

    def showPreLoad(self):
        from source import preLoadWindow
        from source.MuLib import MuMessageBox as MuMsgBox
        self.MuMsgBox = MuMsgBox()
        self.MtPreLoad = preLoadWindow(self.__version__)
        self.MuMsgBox.Critical(None, self.__version__, Preset=FileNotFoundError, info="'assets/preLoader/MtIcon.ico'") if not os.access("assets/preLoader/MtIcon.ico", os.F_OK) else None
        self.MtPreLoad.setWindowIcon(QIcon("assets/preLoader/MtIcon.ico"))
        self.MtPreLoad.show()

        QTimer.singleShot(500, self.runPreLoad)

    def runPreLoad(self):
        # QTimer.signalShot uses multi-threading to execute functions.
        # This means that the main thread will continue, even if the functions in the slots have not finished yet.
        # Update: The QTimer.timeout.connect execute function with also multi-thread.
        #         This means there's No way to pause the Main-Thread without Window-Forzened
        #         which uses the method 'QThread.wait()' to stop the Window Updating.
        # The main idea of time-pause is simulate the waiting time that caused by Loading-Process.
        # If it's not enough for 800ms, the Animation for text-appear will not show entirely.
        # As the speed of Python Image Loader, You might be not seen the Anim at all!
        
        # The program must under the control of main thread
        # of says 'MapleUI.py', in order to import other method directly.
        # As I Known, the main file will continue running while QTimer is active,
        # which means it might return before sub-thread finished.
        
        # ! The following code & infomation will be delete when the loading-process finished constracting but remains a sign.
        self.MtPreLoad.initProgressAnimation()
        self.MtP = self.MtPreLoad.preLoad(self.MtPreLoad, self.MuMsgBox)

        QTimer.singleShot(1000, self.MtP.LoadResource)

    def run(self):
        self.showPreLoad()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    MapleUI = MapleUI()
    MapleUI.run()