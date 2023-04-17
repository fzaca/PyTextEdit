from PySide6.QtWidgets import QDialog

from views.unsaved_changes_dialog_ui import Ui_unsaved_changes_dialog

class UnsavedChangesDialogForm(QDialog, Ui_unsaved_changes_dialog):
    Discarded = 0
    Saved = 1 
    Canceled = 2
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.discard_button.clicked.connect(self.discard_clicked)
        self.save_button.clicked.connect(self.save_clicked)

    def cancel_clicked(self):
        self.done(self.Canceled)

    def discard_clicked(self):
        self.done(self.Discarded)

    def save_clicked(self):
        self.done(self.Saved)