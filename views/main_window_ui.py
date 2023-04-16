# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 587)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        self.action_cut = QAction(MainWindow)
        self.action_cut.setObjectName(u"action_cut")
        self.action_paste = QAction(MainWindow)
        self.action_paste.setObjectName(u"action_paste")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.action_redo = QAction(MainWindow)
        self.action_redo.setObjectName(u"action_redo")
        self.action_bold = QAction(MainWindow)
        self.action_bold.setObjectName(u"action_bold")
        self.action_italic = QAction(MainWindow)
        self.action_italic.setObjectName(u"action_italic")
        self.action_underline = QAction(MainWindow)
        self.action_underline.setObjectName(u"action_underline")
        self.action_zoom_out = QAction(MainWindow)
        self.action_zoom_out.setObjectName(u"action_zoom_out")
        self.action_zoom_out.setCheckable(False)
        self.action_zoom_out.setMenuRole(QAction.NoRole)
        self.action_zoom_in = QAction(MainWindow)
        self.action_zoom_in.setObjectName(u"action_zoom_in")
        self.action_zoom_in.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"text_edit")

        self.verticalLayout.addWidget(self.text_edit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_format = QMenu(self.menubar)
        self.menu_format.setObjectName(u"menu_format")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_view.setTearOffEnabled(False)
        self.menu_view.setToolTipsVisible(False)
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setAllowedAreas(Qt.TopToolBarArea)
        self.toolBar.setOrientation(Qt.Horizontal)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet(u"")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_format.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addAction(self.action_undo)
        self.menu_edit.addAction(self.action_redo)
        self.menu_format.addAction(self.action_bold)
        self.menu_format.addAction(self.action_italic)
        self.menu_format.addAction(self.action_underline)
        self.menu_view.addAction(self.action_zoom_out)
        self.menu_view.addAction(self.action_zoom_in)
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_copy)
        self.toolBar.addAction(self.action_cut)
        self.toolBar.addAction(self.action_paste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_undo)
        self.toolBar.addAction(self.action_redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_bold)
        self.toolBar.addAction(self.action_italic)
        self.toolBar.addAction(self.action_underline)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Text Editor", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.action_cut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.action_paste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.action_redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.action_bold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.action_italic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.action_underline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.action_zoom_out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.action_zoom_in.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menu_format.setTitle(QCoreApplication.translate("MainWindow", u"Format", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToolBar", None))
#if QT_CONFIG(tooltip)
        self.toolBar.setToolTip(QCoreApplication.translate("MainWindow", u"Text editing tools", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

