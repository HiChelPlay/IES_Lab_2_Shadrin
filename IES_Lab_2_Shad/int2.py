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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(87, 560, 170, 40))
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(307, 560, 170, 40))
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
        self.goat.setPixmap(QPixmap(u"../../Downloads/pngwing.com (3).png"))
        self.goat.setScaledContents(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 30, 500, 431))
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
        self.wolf2 = QLabel(self.centralwidget)
        self.wolf2.setObjectName(u"cabbage")
        self.wolf2.setGeometry(QRect(100, 360, 41, 41))
        self.wolf2.setPixmap(QPixmap(u"../../Downloads/pngwing.com (6).png"))
        self.wolf2.setScaledContents(True)
        self.dog = QLabel(self.centralwidget)
        self.dog.setObjectName(u"cabbage")
        self.dog.setGeometry(QRect(100, 360, 41, 41))
        self.dog.setPixmap(QPixmap(u"../../Downloads/pngwing.com (6).png"))
        self.dog.setScaledContents(True)
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
        self.Start = QTableView(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(65, 480, 209, 57))
        self.Goal = QTableView(self.centralwidget)
        self.Goal.setObjectName(u"Goal")
        self.Goal.setGeometry(QRect(285, 480, 209, 57))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(95, 460, 141, 20))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(315, 460, 151, 20))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 892, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Переправка", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Поиск в глубину", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Поиск в ширину", None))
        self.label.setText("")
        self.goat.setText("")
        self.man.setText("")
        self.cabbage.setText("")
        self.wolf.setText("")
        self.boat.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
    # retranslateUi

