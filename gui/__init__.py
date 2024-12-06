import sys 
from PySide6.QtWidgets import QApplication 
from gui.cica_ui import Ui_Form

def main():
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()