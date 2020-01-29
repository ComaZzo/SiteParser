from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem

import html_parser
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(QApplication.instance().exit)
        self.ui.actionAbout.triggered.connect(self._on_action_about_triggered)
        
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Header', 'Author', 'Url', 'Count comments', 'Count likes'])
        self.init_table_widget()
        self.ui.tableWidget.resizeColumnsToContents()
    
    def _on_action_about_triggered(self):
        QMessageBox.about(self, 'About', 'Chuvaev Pavel\n8-Т3О-302Б-16')
    
    def init_table_widget(self):
        posts = html_parser.load_habr_news_posts()
        i = 0
        self.ui.tableWidget.setRowCount(len(posts))
        for post in posts:
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(post['title']))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(post['author']))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(post['href']))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(post['comms']))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(post['votes']))
            i += 1
