# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unsaved_changes_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_unsaved_changes_dialog(object):
    def setupUi(self, unsaved_changes_dialog):
        if not unsaved_changes_dialog.objectName():
            unsaved_changes_dialog.setObjectName(u"unsaved_changes_dialog")
        unsaved_changes_dialog.resize(300, 100)
        self.verticalLayout = QVBoxLayout(unsaved_changes_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(unsaved_changes_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setSpacing(6)
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.save_button = QPushButton(unsaved_changes_dialog)
        self.save_button.setObjectName(u"save_button")

        self.horizontal_layout.addWidget(self.save_button)

        self.discard_button = QPushButton(unsaved_changes_dialog)
        self.discard_button.setObjectName(u"discard_button")

        self.horizontal_layout.addWidget(self.discard_button)

        self.cancel_button = QPushButton(unsaved_changes_dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontal_layout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontal_layout)


        self.retranslateUi(unsaved_changes_dialog)

        QMetaObject.connectSlotsByName(unsaved_changes_dialog)
    # setupUi

    def retranslateUi(self, unsaved_changes_dialog):
        unsaved_changes_dialog.setWindowTitle(QCoreApplication.translate("unsaved_changes_dialog", u"Unsaved changes", None))
        self.label.setText(QCoreApplication.translate("unsaved_changes_dialog", u"Do you want to save the changes?", None))
        self.save_button.setText(QCoreApplication.translate("unsaved_changes_dialog", u"Save", None))
        self.discard_button.setText(QCoreApplication.translate("unsaved_changes_dialog", u"Discard", None))
        self.cancel_button.setText(QCoreApplication.translate("unsaved_changes_dialog", u"Cancel", None))
    # retranslateUi

