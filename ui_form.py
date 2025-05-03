# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 271, 291))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(270, 0, 221, 291))
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(490, 0, 271, 291))
        self.newAccountGroup = QPushButton(self.tab)
        self.newAccountGroup.setObjectName(u"newAccountGroup")
        self.newAccountGroup.setGeometry(QRect(10, 310, 101, 32))
        self.addAddressButton = QPushButton(self.tab)
        self.addAddressButton.setObjectName(u"addAddressButton")
        self.addAddressButton.setGeometry(QRect(130, 310, 101, 32))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u54c6\u5566\u5957\u5229\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u5206\u7ec4\u7ba1\u7406", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5f85\u529e", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u63d2\u4ef6\u7ba1\u7406", None))
        self.newAccountGroup.setText(QCoreApplication.translate("Widget", u" \u65b0\u5efa\u8d26\u6237\u7ec4", None))
        self.addAddressButton.setText(QCoreApplication.translate("Widget", u" \u6dfb\u52a0\u5730\u5740", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u64b8\u6bdb\u533a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u5957\u5229\u533a", None))
    # retranslateUi

