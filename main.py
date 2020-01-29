import sys

from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('News sites parser')
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())
