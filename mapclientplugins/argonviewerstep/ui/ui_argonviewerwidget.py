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

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_ArgonViewerWidget(object):
    def setupUi(self, ArgonViewerWidget):
        if not ArgonViewerWidget.objectName():
            ArgonViewerWidget.setObjectName(u"ArgonViewerWidget")
        self.horizontalLayout = QHBoxLayout(ArgonViewerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewStackedWidget = QStackedWidget(ArgonViewerWidget)
        self.viewStackedWidget.setObjectName(u"viewStackedWidget")

        self.horizontalLayout.addWidget(self.viewStackedWidget)

        self.pushButtonDone = QPushButton(ArgonViewerWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)

        self.verticalSpacer = QSpacerItem(20, 328, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.sceneviewerwidget = SceneviewerWidget(ArgonViewerWidget)
        self.sceneviewerwidget.setObjectName(u"sceneviewerwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerwidget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.sceneviewerwidget)


        self.retranslateUi(ArgonViewerWidget)

        QMetaObject.connectSlotsByName(ArgonViewerWidget)
    # setupUi

    def retranslateUi(self, ArgonViewerWidget):
        self.pushButtonDone.setText(QCoreApplication.translate("ArgonViewerWidget", u"Done", None))
        pass
    # retranslateUi

