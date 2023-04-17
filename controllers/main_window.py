from os.path import expanduser

from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QMainWindow, QFileDialog

from views.main_window_ui import Ui_MainWindow
from utils.config_utils import load_config, save_config
from utils.font_utils import update_font
from utils.file_utils import read_file, write_file

class MainWindowForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Elements
        self.font = QFont()
        self.file_path = ''
        self.file_text = ''
        self.unsaved_changes = True

        # Habilidar rehacer y deshacer
        self.text_edit.document().setUndoRedoEnabled(True)

        # Load config
        self.config = load_config()
        self.update_font({
            'size' : self.config.get('font-size'),
            'family' : self.config.get('font-family'),
            # 'color' : self.config.get('font-color'),
        })

        self.update_status_bar()

        # Connects signals
        self.connect_signals()

    def connect_signals(self):
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.action_zoom_in.triggered.connect(self.zoom_in_clicked)
        self.action_zoom_out.triggered.connect(self.zoom_out_clicked)
        self.action_new.triggered.connect(self.new_clicked)
        self.action_open.triggered.connect(self.open_clicked)
        self.action_save.triggered.connect(self.save_clicked)
        self.action_save_as.triggered.connect(self.save_as_clicked)
        self.action_close.triggered.connect(self.close)
        self.action_copy.triggered.connect(self.text_edit.copy)
        self.action_cut.triggered.connect(self.text_edit.cut)
        self.action_paste.triggered.connect(self.text_edit.paste)
        self.action_undo.triggered.connect(self.text_edit.undo)
        self.action_redo.triggered.connect(self.text_edit.redo)

    def zoom_in_clicked(self):
        self.config['font-size'] += 1
        self.update_font({'size' : self.config['font-size']})
        self.menu_view.setVisible(True)

    def zoom_out_clicked(self):
        if self.config.get('font-size') > 1:
            self.config['font-size'] -= 1
            self.update_font({'size' : self.config['font-size']})
            self.menu_view.setVisible(True)

    def update_font(self, changes):
        if changes:
            self.font = update_font(self.font, changes)
            self.text_edit.setFont(self.font)
            if 'color' in changes:
                self.text_edit.setTextColor(QColor(changes['color']))

    def new_clicked(self):
        self.file_text = ''
        self.file_path = ''
        self.text_edit.clear()

    def open_clicked(self):
        file_path = self.open_file_dialog()
        if file_path: 
            self.file_path = file_path
            self.file_text = read_file(file_path)
            self.text_edit.clear()
            self.text_edit.setText(self.file_text)
            self.update_status_bar()
        
    def save_clicked(self):
        if self.file_path:
            self.file_text = self.text_edit.toPlainText()
            write_file(self.file_path, self.file_text)
            self.unsaved_changes = False
            self.update_status_bar()
        else:
            self.save_as_clicked()

    def save_as_clicked(self):
        file_path = self.save_file_dialog()
        if file_path:
            self.file_text = self.text_edit.toPlainText()
            write_file(file_path, self.file_text)
            self.file_path = file_path
            self.unsaved_changes = False
            self.update_status_bar()

    def open_file_dialog(self):
        home_path = expanduser('~')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", home_path, "All files ();;Text files (.txt)", options=options)

        return file_path if file_path else False

    def save_file_dialog(self):
        home_path = expanduser('~')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Saved file", home_path, "All files ();;Text files (.txt)", options=options)

        return file_path if file_path else False
    
    def on_text_changed(self):
        if self.file_text != self.text_edit.toPlainText():
            self.unsaved_changes = True
        else:
            self.unsaved_changes = False
        self.update_status_bar()

    def update_status_bar(self):
        template = 'File: {} | Saved: {}'
        file = self.file_path.split('/')[-1] if self.file_path else 'Unnamed'
        saved = 'No' if self.unsaved_changes else 'Yes'
        message = template.format(file, saved)
        self.status_bar.showMessage(message)
        title = file + '*' if self.unsaved_changes else file
        self.setWindowTitle(title)

    def closeEvent(self, event): # Metodo por defecto
        # Guardar configuración antes de cerrar la aplicación
        save_config(self.config)

        # Agregar verificacion de cambios

        super().closeEvent(event)