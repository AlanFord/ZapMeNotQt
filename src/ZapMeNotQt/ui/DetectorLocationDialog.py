# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetectorLocationDialog.ui'
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(252, 212)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 130, 171, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 20, 160, 85))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.x_label = QLabel(self.formLayoutWidget)
        self.x_label.setObjectName(u"x_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.x_label)

        self.x_text = QLineEdit(self.formLayoutWidget)
        self.x_text.setObjectName(u"x_text")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.x_text)

        self.y_text = QLineEdit(self.formLayoutWidget)
        self.y_text.setObjectName(u"y_text")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.y_text)

        self.y_label = QLabel(self.formLayoutWidget)
        self.y_label.setObjectName(u"y_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.y_label)

        self.z_label = QLabel(self.formLayoutWidget)
        self.z_label.setObjectName(u"z_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.z_label)

        self.z_text = QLineEdit(self.formLayoutWidget)
        self.z_text.setObjectName(u"z_text")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z_text)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Detector Location", None))
        self.x_label.setText(QCoreApplication.translate("Dialog", u"X (cm):", None))
        self.x_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.y_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.y_label.setText(QCoreApplication.translate("Dialog", u"Y (cm):", None))
        self.z_label.setText(QCoreApplication.translate("Dialog", u"Z (cm):", None))
        self.z_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"0.0", None))
    # retranslateUi

