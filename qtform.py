# !/usr/bin/python
import sys
from PyQt4.QtGui import *
class TableWidget(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('PriceView')
        self.table = QTableWidget(13,8)
		self.table.setHorizontalHeaderLabels(['Product','WorkingShortOrder','BidQty','BidPx','AskPx','AskQty','WorkingLongOrder'])
        self.setCentralWidget(self.table)
app = QApplication(sys.argv)
tb = TableWidget()
tb.show()
app.exec_()