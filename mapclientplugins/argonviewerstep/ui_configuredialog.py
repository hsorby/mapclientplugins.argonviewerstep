# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.argonFile_rb = QRadioButton(self.configGroupBox)
        self.argonFile_rb.setObjectName(u"argonFile_rb")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.argonFile_rb)

        self.exfFile_rb = QRadioButton(self.configGroupBox)
        self.exfFile_rb.setObjectName(u"exfFile_rb")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.exfFile_rb)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.argonFile_rb.setText(QCoreApplication.translate("ConfigureDialog", u"Argon File", None))
        self.exfFile_rb.setText(QCoreApplication.translate("ConfigureDialog", u"Exf File", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Input File Type:", None))
    # retranslateUi

