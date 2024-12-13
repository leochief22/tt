# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget,QVBoxLayout)
import os

class Ui_Widget(object):
    def setupUi(self, Widget):
        #rutaTA = os.path.abspath(r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TA.png")
        #print("Ruta absoluta:", rutaTA)
        #print("¿Archivo existe?:", os.path.exists(rutaTA))
        #pixmap = QPixmap(rutaTA)
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 40, 271, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inciarButton = QPushButton(self.frame)
        self.inciarButton.setObjectName(u"inciarButton")
        self.inciarButton.setGeometry(QRect(50, 230, 181, 61))
        self.inciarButton.setStyleSheet(u"background-color: rgb(20, 255, 8);")
        self.detenerButton_2 = QPushButton(self.frame)
        self.detenerButton_2.setObjectName(u"detenerButton_2")
        self.detenerButton_2.setGeometry(QRect(50, 300, 181, 61))
        self.detenerButton_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.imagen_label = QLabel(self.frame)
        self.imagen_label.setPixmap(QPixmap())  # Inicialmente vacío
        self.imagen_label.setGeometry(QRect(20, 5, 100, 100))
        self.imagen_label.setScaledContents(True)  # Ajustar imagen al QLabel
        self.imagen_label.setFixedSize(200, 200)  # Tamaño fijo para la etiqueta

        self.imagenTC = QLabel(self.frame)
        self.imagenTC.setObjectName(u"imagenTC")
        self.imagenTC.setGeometry(QRect(50, 40, 151, 91))
        self.imagenTC.setStyleSheet(u"image: url(:/TC/TC.png);")
        self.imagenTM = QLabel(self.frame)
        self.imagenTM.setObjectName(u"imagenTM")
        self.imagenTM.setGeometry(QRect(60, 50, 151, 91))
        self.imagenTM.setStyleSheet(u"image: url(:/tostadosCafe/TM.png);")
        self.imagenTO = QLabel(self.frame)
        self.imagenTO.setObjectName(u"imagenTO")
        self.imagenTO.setGeometry(QRect(60, 50, 151, 91))
        self.imagenTO.setStyleSheet(u"image: url(:/tostadosCafe/TO.png);")
        self.imagenTA = QLabel(self.frame)
        self.imagenTA.setObjectName(u"imagenTA")
        self.imagenTA.setGeometry(QRect(60, 50, 151, 91))
        #self.imagenTA.setPixmap(pixmap)
        #self.imagenTA.setScaledContents(True)  # Ajusta la imagen al QLabel
        #self.imagenTA.setStyleSheet(f"image: url({rutaTA});")
        
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")    
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 210, 231, 31))
        #self.comboBox.setParent(self)  # Establecer la ventana como padre del ComboBox
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"border-radius:8px;\n"
"}")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def cambiar_imagen(self, texto):
            """Cambia la imagen del QLabel según la selección del ComboBox."""
            ruta = self.imagenes.get(texto, None)  # Obtener la ruta de la imagen seleccionada
            if ruta and os.path.exists(ruta):  # Verificar que la ruta sea válida
                pixmap = QPixmap(ruta)
                if not pixmap.isNull():  # Verificar que se cargó la imagen
                    self.imagen_label.setPixmap(pixmap)
                else:
                    self.imagen_label.clear()  # Si no se puede cargar, limpiar QLabel
            else:
                self.imagen_label.clear()  # Si no hay ruta o no existe, limpiar QLabel



    def retranslateUi(self, Widget):
        self.imagenes = {
            "Seleccione una opción": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/wait.png",
            "TUESTE CLARO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TC.png",
            "TUESTE MEDIO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TM.png",
            "TUESTE OBSCURO": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TO.png",
            "TUESTE ARTESANAL": r"C:/Users/EQUIPO/Documents/11vo/TT/PRUEBAS/interfazPyqt6/qtCreator/pruebaProyecto/TA.png",
        }
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.inciarButton.setText(QCoreApplication.translate("Widget", u"INICIO", None))
        self.detenerButton_2.setText(QCoreApplication.translate("Widget", u"DETENER", None))
        self.imagenTC.setText("")
        self.imagenTM.setText("")
        self.imagenTO.setText("")
        self.imagenTA.setText("")
        self.comboBox.currentTextChanged.connect(self.cambiar_imagen)
        #self.imagen_label.setText(QCoreApplication.translate("retranslateUi", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Seleccione una opción", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"TUESTE CLARO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"TUESTE MEDIO", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"TUESTE OBSCURO", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"TUESTE ARTESANAL", None))

    # retranslateUi

