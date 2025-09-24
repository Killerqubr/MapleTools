from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QObject
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QLabel
import typing

class MuAnimation:
    "add functionded pre-set Animation to QWidget"
    __version__ = 1
    
    @staticmethod
    def posAnim(Widget: typing.Optional[QLabel],
                Duration: int,
                StartValue : QPoint,
                EndValue: QPoint,
                Ease: QEasingCurve.Type = QEasingCurve.Type.OutExpo
                ) -> QPropertyAnimation:
        AnimObj = QPropertyAnimation(Widget, b'pos')
        AnimObj.setDuration(Duration)
        AnimObj.setStartValue(StartValue)
        AnimObj.setEndValue(EndValue)
        AnimObj.setEasingCurve(Ease)
        return AnimObj
    
    @staticmethod
    def opaAnim(parent: QObject,
                Widget: typing.Optional[QLabel],
                Duration: int,
                StartValue: float | int,
                EndValue: float | int,
                Ease: QEasingCurve.Type = QEasingCurve.Type.OutExpo
                ) -> QPropertyAnimation:
        AnimEffect = QGraphicsOpacityEffect(parent)
        AnimObj = QPropertyAnimation(AnimEffect, b'opacity')
        Widget.setGraphicsEffect(AnimEffect)
        AnimObj.setDuration(Duration)
        AnimObj.setStartValue(StartValue)
        AnimObj.setEndValue(EndValue)
        AnimObj.setEasingCurve(Ease)
        return AnimObj