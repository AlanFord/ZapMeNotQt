# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OptionsGroupsDialog.ui'
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
    QFormLayout, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 189)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.StandardButton = QRadioButton(Dialog)
        self.StandardButton.setObjectName(u"StandardButton")
        self.StandardButton.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.StandardButton)

        self.ThirtyButton = QRadioButton(Dialog)
        self.ThirtyButton.setObjectName(u"ThirtyButton")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ThirtyButton)

        self.DiscreteButton = QRadioButton(Dialog)
        self.DiscreteButton.setObjectName(u"DiscreteButton")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.DiscreteButton)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.StandardButton.setText(QCoreApplication.translate("Dialog", u"Standard Groups", None))
        self.ThirtyButton.setText(QCoreApplication.translate("Dialog", u"30 Energy Groups", None))
        self.DiscreteButton.setText(QCoreApplication.translate("Dialog", u"Discrete Photon Energies", None))
    # retranslateUi

