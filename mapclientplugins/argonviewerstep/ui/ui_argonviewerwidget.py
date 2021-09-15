# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'argonviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ArgonViewerWidget(object):
    def setupUi(self, ArgonViewerWidget):
        if not ArgonViewerWidget.objectName():
            ArgonViewerWidget.setObjectName(u"ArgonViewerWidget")
        ArgonViewerWidget.resize(908, 833)
        self.toolBar = QToolBar(ArgonViewerWidget)
        self.toolBar.setObjectName(u"toolBar")
        ArgonViewerWidget.addToolBar(self.toolBar)
        self.centralwidget = QWidget(ArgonViewerWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewStackedWidget = QStackedWidget(self.centralwidget)
        self.viewStackedWidget.setObjectName(u"viewStackedWidget")

        self.verticalLayout.addWidget(self.viewStackedWidget)

        self.pushButtonDone = QPushButton(self.centralwidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.verticalLayout.addWidget(self.pushButtonDone)

        ArgonViewerWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArgonViewerWidget)

        QMetaObject.connectSlotsByName(ArgonViewerWidget)
    # setupUi

    def retranslateUi(self, ArgonViewerWidget):
        self.pushButtonDone.setText(QCoreApplication.translate("ArgonViewerWidget", u"Done", None))
        pass
    # retranslateUi

