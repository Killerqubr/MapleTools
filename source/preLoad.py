from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap
import os

class preLoadWindow(QMainWindow):
    """
    preLoader for Maple Tools.
    """
    def __init__(self, __version__):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(750, 500)
        
        self.__version__ = __version__
        self.initUI()
        self.loadImages()

    def initUI(self):
        self.setupCentralWidget()
        self.setupLeftContent()
        self.setupRightContent()
        self.setupWindowStyle()

    def setupCentralWidget(self):
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("CentralWidget")
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(QVBoxLayout())

    def setupLeftContent(self):
        self.leftContent = QWidget()
        self.leftContent.setGeometry(0, 0, 340, 500)
        self.leftContent.setStyleSheet("background-color: transparent;")
        
        self.leftLayout = QVBoxLayout(self.leftContent)
        self.leftLayout.setContentsMargins(20, 80, 20, 40)
        self.leftLayout.setSpacing(30)

        self.setupMtIconLabel()
        self.setupMtNameLabel()
        self.setupMtInfoLabel()
        self.setupProgressLabel()
        self.setupProgressAltLabel()
        self.setupProgressNumLabel()

        self.centralWidget.layout().addWidget(self.leftContent) # type: ignore

    def setupMtIconLabel(self):
        self.iconLabel = QLabel(self.centralWidget) # type: ignore
        self.iconLabel.setGeometry(0, 0, 150, 150)
        self.iconLabel.setStyleSheet("background-color: transparent; border-radius: 5px;")

    def setupMtNameLabel(self):
        self.nameLabel = QLabel(self.centralWidget) # type: ignore
        self.nameLabel.setGeometry(-50, -50, 400, 400)
        self.nameLabel.setStyleSheet("background-color: transparent; border-radius: 5px;")

    def setupMtInfoLabel(self):
        self.infoLabel = QLabel(self.centralWidget) # type: ignore
        self.infoLabel.setGeometry(40, 180, 400, 150)
        self.infoLabel.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #bbbbbb;
                font-size: 16px;
                font-family: Source Han Sans CN;
                font-weight: 500;
            }
        """)
        self.infoLabel.setAlignment(Qt.AlignLeft) # type: ignore
        self.infoLabel.setText(f"内部版本 {self.__version__}\n\nCopyright ©\n2025 Killerqubr & flizc\n\nAll rights reserved.")

    def setupProgressAltLabel(self):
        self.progressInfoLabel = QLabel(self.centralWidget) # type: ignore
        self.progressInfoLabel.setGeometry(40, 425, 400, 30)
        self.progressInfoLabel.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #bbbbbb;
                font-size: 15px;
                font-family: Source Han Sans CN;
                font-weight: 500;
            }
        """)
        self.progressInfoLabel.setAlignment(Qt.AlignLeft) # type: ignore
        self.progressInfoLabel.setText("")

    def setupProgressLabel(self):
        self.progressLabel = QLabel(self.centralWidget) # type: ignore
        self.progressLabel.setGeometry(40, 450, 400, 100)
        self.progressLabel.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #bf514e;
                font-size: 16px;
                font-family: Source Han Sans CN;
                font-weight: 570;
            }
        """)
        self.progressLabel.setAlignment(Qt.AlignLeft) # type: ignore

    def setupProgressNumLabel(self):
        self.progressNumLabel = QLabel(self.centralWidget) # type: ignore
        self.progressNumLabel.setGeometry(40, 450, 230, 100)
        self.progressNumLabel.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #eeeeee;
                font-size: 16px;
                font-family: Source Han Sans CN;
                font-weight: 500;
            }
        """)
        self.progressNumLabel.setAlignment(Qt.AlignRight) # type: ignore

    def setupRightContent(self):
        self.rightImageLabel = QLabel(self.centralWidget) # type: ignore
        self.rightImageLabel.setGeometry(310, 0, 390, 500)
        self.rightImageLabel.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
            }
        """)

    def setupWindowStyle(self):
        self.setStyleSheet("""
            #CentralWidget {
                background-color: #252020;
                border-radius: 30px;
            }
        """)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(32, 32, 32)))
        painter.setPen(Qt.NoPen) # type: ignore
        painter.drawRoundedRect(self.rect(), 30, 30)

    def loadImages(self):
        from source.MuLib import MuMessageBox
        self.MuMsgBox = MuMessageBox()
        self.loadIconImage()
        self.loadNameImage()
        self.loadBackgroundImage()

    def loadIconImage(self):
        self.MuMsgBox.Critical(None, self.__version__, Preset=FileNotFoundError, info="'assets/preLoader/MtIcon.png'") if not os.access("assets/preLoader/MtIcon.png", os.F_OK) else None
        iconPixmap = QPixmap("assets/preLoader/MtIcon.png")
        if not iconPixmap.isNull():
            iconPixmap = iconPixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation) # type: ignore
            self.iconLabel.setPixmap(iconPixmap)
        else:
            self.closePreLoad()

    def loadNameImage(self):
        self.MuMsgBox.Critical(None, self.__version__, Preset=FileNotFoundError, info="'assets/preLoader/MtName.png'") if not os.access("assets/preLoader/MtName.png", os.F_OK) else None
        namePixmap = QPixmap("assets/preLoader/MtName.png")
        if not namePixmap.isNull():
            namePixmap = namePixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation) # type: ignore
            self.nameLabel.setPixmap(namePixmap)
        else:
            self.closePreLoad()

    def loadBackgroundImage(self):
        self.MuMsgBox.Critical(None, self.__version__, Preset=FileNotFoundError, info="'assets/preLoader/MapleBackg.jpg'") if not os.access("assets/preLoader/MapleBackg.jpg", os.F_OK) else None
        backgroundPixmap = QPixmap("assets/preLoader/MapleBackg.jpg")
        if not backgroundPixmap.isNull():
            backgroundPixmap = backgroundPixmap.scaled(500, 500, Qt.IgnoreAspectRatio, Qt.SmoothTransformation) # type: ignore
            self.rightImageLabel.setPixmap(backgroundPixmap)
        else:
            self.closePreLoad()

    def updateProgress(self, status=None, detail=None, progress=None):
        """
        Update Information in PreLoad Window.
        """
        if status:
            self.progressLabel.setText(status)
            self.posIntroPL.start()
            self.opaIntroPL.start()
        if detail:
            self.progressInfoLabel.setText(detail)
            self.opaIntroPIL.start()
            self.posIntroPIL.start()
        if progress:
            self.progressNumLabel.setText(progress)

    def initProgressAnimation(self):
        from source.MuLib.MuAnim import MuAnimation as MuAnim
        self.posIntroPL = MuAnim.posAnim(self.progressLabel, 800, QPoint(200,450), QPoint(40,450))
        self.opaIntroPL = MuAnim.opaAnim(self, self.progressLabel ,900, 0, 1)
        self.posIntroPIL = MuAnim.posAnim(self.progressInfoLabel, 800, QPoint(220,425), QPoint(40,425))
        self.opaIntroPIL = MuAnim.opaAnim(self, self.progressInfoLabel ,900, 0, 1)

    def closePreLoad(self):
        self.close()

    @staticmethod
    def ResouceVerification():
        import hashlib
        

    class preLoad:
        """
        Load resource while program is running.
        """
        def __init__(self, pL, MuMsgBox):
            from source.MuLib import MuMessageBox
            self.MuMsgBox = MuMessageBox()
            self.pL = pL # type: preLoadWindow
            self.MuMsgBox = MuMsgBox
            self.pL.updateProgress("初始化", None, None)

        def LoadResource(self):
            #self.pL.updateProgress("加载资源", None, None)
            self.pL.updateProgress("加载资源", None, "完成")
            QTimer.singleShot(1000, self.LoadModule)

        def LoadModule(self):
            #self.pL.updateProgress("加载模块", None, None)

            self.pL.updateProgress("加载模块", None, "完成")
            QTimer.singleShot(1000, self.LoadFinal)
        
        def LoadFinal(self):
            self.pL.updateProgress("正在加载 Maple Tools", "准备就绪", " ")
            QTimer.singleShot(1000, self.LaunchMapleUI)

        def LaunchMapleUI(self):
            if self.pL:
                self.pL.closePreLoad()

            from source import MapleUIWindow
            self.MapleUI = MapleUIWindow()
            self.MapleUI.show()