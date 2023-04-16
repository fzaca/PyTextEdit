from PySide6.QtGui import QFont

def update_font_size(font: QFont, size: int) -> QFont:
    font.setPointSize(size)
    return font

def update_font_family(font: QFont, family: str) -> QFont:
    font.setFamily(family)
    return font

def update_font(font: QFont, changes: dict) -> QFont:
    if 'size' in changes:
        font = update_font_size(font, changes['size'])
    if 'family' in changes:
        font = update_font_family(font, changes['family'])
    return font