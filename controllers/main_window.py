from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QMainWindow

from views.main_window_ui import Ui_MainWindow
from utils.config_utils import load_config, save_config
from utils.font_utils import update_font

class MainWindowForm(QMainWindow, QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Elements
        self.font = QFont()

        # Load config
        self.config = load_config()
        self.update_font({
            'size' : self.config['font-size'],
            'family' : self.config['font-family'],
            # 'color' : self.config['font-color'],
        })

        # Connects
        self.action_zoom_in.triggered.connect(self.zoom_in)
        self.action_zoom_out.triggered.connect(self.zoom_out)

    def zoom_in(self):
        self.config['font-size'] += 1
        self.update_font({'size' : self.config['font-size']})
        self.menu_view.setVisible(True)

    def zoom_out(self):
        if self.config['font-size'] > 1:
            self.config['font-size'] -= 1
            self.update_font({'size' : self.config['font-size']})
            self.menu_view.setVisible(True)

    def update_font(self, changes):
        if changes:
            self.font = update_font(self.font, changes)
            self.text_edit.setFont(self.font)
            if 'color' in changes:
                self.text_edit.setTextColor(QColor(changes['color']))

    def update_status_bar(self):
        pass

    def closeEvent(self, event): # Metodo por defecto
        # Guardar configuración antes de cerrar la aplicación
        save_config(self.config)
        super().closeEvent(event)