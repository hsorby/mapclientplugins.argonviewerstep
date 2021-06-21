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
        self.verticalLayout = QVBoxLayout(ArgonViewerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(ArgonViewerWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.pushButtonAddSceneEditor = QPushButton(self.groupBox)
        self.pushButtonAddSceneEditor.setObjectName(u"pushButtonAddSceneEditor")
        self.pushButtonAddSceneEditor.setGeometry(QRect(-20, 40, 91, 23))
        self.pushButtonAddSceneviewerEditor = QPushButton(self.groupBox)
        self.pushButtonAddSceneviewerEditor.setObjectName(u"pushButtonAddSceneviewerEditor")
        self.pushButtonAddSceneviewerEditor.setGeometry(QRect(-30, 80, 118, 23))
        self.pushButtonDone = QPushButton(self.groupBox)
        self.pushButtonDone.setObjectName(u"pushButtonDone")
        self.pushButtonDone.setGeometry(QRect(0, 160, 75, 23))

        self.verticalLayout.addWidget(self.groupBox)

        self.viewStackedWidget = QStackedWidget(ArgonViewerWidget)
        self.viewStackedWidget.setObjectName(u"viewStackedWidget")

        self.verticalLayout.addWidget(self.viewStackedWidget)


        self.retranslateUi(ArgonViewerWidget)

        QMetaObject.connectSlotsByName(ArgonViewerWidget)
    # setupUi

    def retranslateUi(self, ArgonViewerWidget):
        self.groupBox.setTitle(QCoreApplication.translate("ArgonViewerWidget", u"GroupBox", None))
        self.pushButtonAddSceneEditor.setText(QCoreApplication.translate("ArgonViewerWidget", u"Add Scene Editor", None))
        self.pushButtonAddSceneviewerEditor.setText(QCoreApplication.translate("ArgonViewerWidget", u"Add Scene View Editor", None))
        self.pushButtonDone.setText(QCoreApplication.translate("ArgonViewerWidget", u"Done", None))
        pass
    # retranslateUi

