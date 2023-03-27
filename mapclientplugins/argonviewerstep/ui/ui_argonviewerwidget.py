# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'argonviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

class Ui_ArgonViewerWidget(object):
    def setupUi(self, ArgonViewerWidget):
        if not ArgonViewerWidget.objectName():
            ArgonViewerWidget.setObjectName(u"ArgonViewerWidget")
        ArgonViewerWidget.resize(908, 833)
        self.centralwidget = QWidget(ArgonViewerWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewTabWidget = QTabWidget(self.centralwidget)
        self.viewTabWidget.setObjectName(u"viewTabWidget")

        self.verticalLayout.addWidget(self.viewTabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDocumentation = QPushButton(self.centralwidget)
        self.pushButtonDocumentation.setObjectName(u"pushButtonDocumentation")

        self.horizontalLayout.addWidget(self.pushButtonDocumentation)

        self.pushButtonDone = QPushButton(self.centralwidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)


        self.verticalLayout.addLayout(self.horizontalLayout)

        ArgonViewerWidget.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(ArgonViewerWidget)
        self.toolBar.setObjectName(u"toolBar")
        ArgonViewerWidget.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(ArgonViewerWidget)

        QMetaObject.connectSlotsByName(ArgonViewerWidget)
    # setupUi

    def retranslateUi(self, ArgonViewerWidget):
        ArgonViewerWidget.setWindowTitle(QCoreApplication.translate("ArgonViewerWidget", u"Argon Viewer", None))
        self.pushButtonDocumentation.setText(QCoreApplication.translate("ArgonViewerWidget", u"Online Documentation", None))
        self.pushButtonDone.setText(QCoreApplication.translate("ArgonViewerWidget", u"Done", None))
    # retranslateUi

