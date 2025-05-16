# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'int.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 480, 171, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 35, 561, 421))
        self.label.setPixmap(QPixmap(u"../../Downloads/pngwing.com (2).png"))
        self.label.setScaledContents(True)
        self.goat = QLabel(self.centralwidget)
        self.goat.setObjectName(u"goat")
        self.goat.setGeometry(QRect(100, 300, 51, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goat.sizePolicy().hasHeightForWidth())
        self.goat.setSizePolicy(sizePolicy)
        self.goat.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        # Загружаем оригинальное изображение
        original_pixmap = QPixmap(u"../../Downloads/pngwing.com (3).png")
        # Создаем отзеркаленную версию
        mirrored_pixmap = original_pixmap.transformed(QTransform().scale(-1, 1))
        self.goat.setPixmap(QPixmap(mirrored_pixmap))
        self.goat.setScaledContents(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(590, 30, 301, 431))
        self.textEdit.setText('Человек\tКоза\tКапуста\tВолк\n\n')
        self.man = QLabel(self.centralwidget)
        self.man.setObjectName(u"man")
        self.man.setGeometry(QRect(100, 230, 51, 71))
        self.man.setPixmap(QPixmap(u"../../Downloads/pngwing.com (4).png"))
        self.man.setScaledContents(True)
        self.cabbage = QLabel(self.centralwidget)
        self.cabbage.setObjectName(u"cabbage")
        self.cabbage.setGeometry(QRect(100, 360, 41, 41))
        self.cabbage.setPixmap(QPixmap(u"../../Downloads/pngwing.com (6).png"))
        self.cabbage.setScaledContents(True)
        self.wolf = QLabel(self.centralwidget)
        self.wolf.setObjectName(u"wolf")
        self.wolf.setGeometry(QRect(100, 400, 51, 51))
        self.wolf.setPixmap(QPixmap(u"../../Downloads/pngwing.com (5).png"))
        self.wolf.setScaledContents(True)
        self.boat = QLabel(self.centralwidget)
        self.boat.setObjectName(u"boat")
        self.boat.setEnabled(True)
        self.boat.setGeometry(QRect(180, 320, 51, 51))
        self.boat.setPixmap(QPixmap(u"../../Downloads/pngwing.com (7).png"))
        self.boat.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Переправка", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label.setText("")
        self.goat.setText("")
        self.man.setText("")
        self.cabbage.setText("")
        self.wolf.setText("")
        self.boat.setText("")
    # retranslateUi

