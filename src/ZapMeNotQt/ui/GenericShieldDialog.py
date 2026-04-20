# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenericShieldDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(298, 591)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.name_label = QLabel(Dialog)
        self.name_label.setObjectName(u"name_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.name_label)

        self.name_field = QComboBox(Dialog)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setEditable(True)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.name_field)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.material = QComboBox(self.groupBox)
        self.material.setObjectName(u"material")

        self.verticalLayout_2.addWidget(self.material)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.densityLabel = QLabel(self.groupBox)
        self.densityLabel.setObjectName(u"densityLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.densityLabel)

        self.density = QLineEdit(self.groupBox)
        self.density.setObjectName(u"density")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.density)


        self.verticalLayout_2.addLayout(self.formLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.triplet1Xname = QLabel(self.groupBox_2)
        self.triplet1Xname.setObjectName(u"triplet1Xname")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.triplet1Xname)

        self.triplet1Yname = QLabel(self.groupBox_2)
        self.triplet1Yname.setObjectName(u"triplet1Yname")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.triplet1Yname)

        self.triplet1Zname = QLabel(self.groupBox_2)
        self.triplet1Zname.setObjectName(u"triplet1Zname")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.triplet1Zname)

        self.triplet1X = QLineEdit(self.groupBox_2)
        self.triplet1X.setObjectName(u"triplet1X")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.triplet1X)

        self.triplet1Y = QLineEdit(self.groupBox_2)
        self.triplet1Y.setObjectName(u"triplet1Y")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.triplet1Y)

        self.triplet1Z = QLineEdit(self.groupBox_2)
        self.triplet1Z.setObjectName(u"triplet1Z")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.triplet1Z)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_5 = QFormLayout(self.groupBox_3)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.triplet2Xname = QLabel(self.groupBox_3)
        self.triplet2Xname.setObjectName(u"triplet2Xname")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.triplet2Xname)

        self.triplet2Yname = QLabel(self.groupBox_3)
        self.triplet2Yname.setObjectName(u"triplet2Yname")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.triplet2Yname)

        self.triplet2Zname = QLabel(self.groupBox_3)
        self.triplet2Zname.setObjectName(u"triplet2Zname")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.triplet2Zname)

        self.triplet2X = QLineEdit(self.groupBox_3)
        self.triplet2X.setObjectName(u"triplet2X")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.triplet2X)

        self.triplet2Y = QLineEdit(self.groupBox_3)
        self.triplet2Y.setObjectName(u"triplet2Y")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.triplet2Y)

        self.triplet2Z = QLineEdit(self.groupBox_3)
        self.triplet2Z.setObjectName(u"triplet2Z")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.triplet2Z)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.radius1Label = QLabel(Dialog)
        self.radius1Label.setObjectName(u"radius1Label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.radius1Label)

        self.radius1 = QLineEdit(Dialog)
        self.radius1.setObjectName(u"radius1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.radius1)

        self.radius2Label = QLabel(Dialog)
        self.radius2Label.setObjectName(u"radius2Label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.radius2Label)

        self.radius2 = QLineEdit(Dialog)
        self.radius2.setObjectName(u"radius2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.radius2)

        self.shellCheckBox = QCheckBox(Dialog)
        self.shellCheckBox.setObjectName(u"shellCheckBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.shellCheckBox)

        self.shellButton = QPushButton(Dialog)
        self.shellButton.setObjectName(u"shellButton")
        self.shellButton.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.shellButton)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.material, self.density)
        QWidget.setTabOrder(self.density, self.triplet1X)
        QWidget.setTabOrder(self.triplet1X, self.triplet1Y)
        QWidget.setTabOrder(self.triplet1Y, self.triplet1Z)
        QWidget.setTabOrder(self.triplet1Z, self.triplet2X)
        QWidget.setTabOrder(self.triplet2X, self.triplet2Y)
        QWidget.setTabOrder(self.triplet2Y, self.triplet2Z)
        QWidget.setTabOrder(self.triplet2Z, self.radius1)
        QWidget.setTabOrder(self.radius1, self.radius2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generic Shield", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"Shield Name:", None))
        self.name_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"New ...", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Material Information", None))
        self.densityLabel.setText(QCoreApplication.translate("Dialog", u"Density (g/cm3):", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Triplet #1", None))
        self.triplet1Xname.setText(QCoreApplication.translate("Dialog", u"X (cm):", None))
        self.triplet1Yname.setText(QCoreApplication.translate("Dialog", u"Y (cm):", None))
        self.triplet1Zname.setText(QCoreApplication.translate("Dialog", u"Z (cm):", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Triplet #2", None))
        self.triplet2Xname.setText(QCoreApplication.translate("Dialog", u"X (cm):", None))
        self.triplet2Yname.setText(QCoreApplication.translate("Dialog", u"Y (cm):", None))
        self.triplet2Zname.setText(QCoreApplication.translate("Dialog", u"Z (cm):", None))
        self.radius1Label.setText(QCoreApplication.translate("Dialog", u"Radius 1 (cm):", None))
        self.radius2Label.setText(QCoreApplication.translate("Dialog", u"Radius 2 (cm):", None))
        self.shellCheckBox.setText(QCoreApplication.translate("Dialog", u"Include Shell", None))
        self.shellButton.setText(QCoreApplication.translate("Dialog", u"Shell ...", None))
    # retranslateUi

