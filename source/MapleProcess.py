from PyQt5.QtWidgets import QMainWindow, QToolBar, QStatusBar, QAction, QApplication, QMenu, QToolButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MapleToolsWindow(QMainWindow):
    """
    Main user Interface of the Program.
    """
    def __init__(self):
        super().__init__()
        
        # 界面初始化
        self.setWindowIcon(QIcon("assets/preLoader/MtIcon.ico"))
        self.setMinimumSize(1200, 800)
        self.move(0, 0)
        self.showMaximized()
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #161616;
            }
            QToolBar {
                background-color: #f0f0f0;
                border: none;
                border-bottom: 2px solid #d0d0d0;
            }
            QToolButton {
                background-color: transparent;
                border: 0px;
                border-radius: 0px;
                padding: 0px 4px;
                margin: 0px;
                font-family: "Source Han Sans CN";
                font-weight: 550;
                font-size: 15px;
                color: #000000;
            }
            QToolButton:hover {
                background-color: #f9e8e8;
                border: 1px solid #e8c9c9;
                color: #bf514e;
            }
            QToolButton:pressed {
                background-color: #f3d5d5;
                border: 1px solid #d9a8a8;
                color: #a8423f;
            }
            QToolButton:checked {
                background-color: #bf514e;
                border: 1px solid #a8423f;
                color: #ffffff;
            }
            QMenu::item:hover {
                border-color: #e8c9c9;
                background: #f9e8e8;
                color:#000000;
            }
            QMenu::item:selected {
                border-color: #d9a8a8;
                background: #f3d5d5;
                color:#bf514e;
            }
            QMenu::item:checked {
                border-color: #a8423f;
                background: #bf514e;
                color:#ffffff;
            }
            QMenu::item {
                padding-left: 30px;
                padding-right: 20px;
                padding-top: 2px;
                padding-bottom: 2px;
            }
            QStatusBar {
                background-color: #202020;
                color: #606060;
                border: none;
                border-top: 0px solid #d0d0d0;
                font-family: "Source Han Sans CN";
                font-size: 16px;
                padding: 5px 8px;
            }
            QStatusBar::item {
                border: none;
            }
        """)
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Maple Tools 2025")
        self.setupToolBar()
        self.setupStatusBar()
    
    def setupToolBar(self):
        self.toolbar = QToolBar("主工具栏", self)
        self.toolbar.setMovable(False)
        
        # 帮助菜单
        self.helpMenu = QMenu("帮助", self)
        self.aboutAction = QAction("关于 Maple Tools", self)
        
        self.helpMenu.addAction(self.aboutAction)
        
        self.helpButton = QToolButton(self)
        self.helpButton.setStyleSheet("QToolButton::menu-indicator{image:none;}")
        self.helpButton.setText("帮助(H)")
        self.helpButton.setMenu(self.helpMenu)
        self.helpButton.setPopupMode(QToolButton.InstantPopup)
        
        self.toolbar.addWidget(self.helpButton)
        
        self.addToolBar(Qt.TopToolBarArea, self.toolbar) # type: ignore
    
    def setupStatusBar(self):
        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage("就绪")
        
        self.setStatusBar(self.statusBar)