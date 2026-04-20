# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OptionsQuadratureDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(312, 442)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.triplet1Xname = QLabel(self.groupBox_2)
        self.triplet1Xname.setObjectName(u"triplet1Xname")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.triplet1Xname)

        self.triplet1X = QLineEdit(self.groupBox_2)
        self.triplet1X.setObjectName(u"triplet1X")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.triplet1X)

        self.triplet1Yname = QLabel(self.groupBox_2)
        self.triplet1Yname.setObjectName(u"triplet1Yname")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.triplet1Yname)

        self.triplet1Y = QLineEdit(self.groupBox_2)
        self.triplet1Y.setObjectName(u"triplet1Y")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.triplet1Y)

        self.triplet1Zname = QLabel(self.groupBox_2)
        self.triplet1Zname.setObjectName(u"triplet1Zname")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.triplet1Zname)

        self.triplet1Z = QLineEdit(self.groupBox_2)
        self.triplet1Z.setObjectName(u"triplet1Z")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.triplet1Z)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.triplet1X, self.triplet1Y)
        QWidget.setTabOrder(self.triplet1Y, self.triplet1Z)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generic Shield", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Source Quadrature</p><p>Please enter a preferred source quadrature. Three values represent the quadrature for X, Y, Z (rectangular geometries), R, Theta, Z (cylidrical geometries), and R, Theta, Phi (spherical geometries). Line sources use only the first entry. Point sources do not use quadrature. Default values used by ZapMeNotQt are 10, 10, 10.</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Quadrature Entries", None))
        self.triplet1Xname.setText(QCoreApplication.translate("Dialog", u"First", None))
        self.triplet1Yname.setText(QCoreApplication.translate("Dialog", u"Second", None))
        self.triplet1Zname.setText(QCoreApplication.translate("Dialog", u"Third", None))
    # retranslateUi

