from SnifferBase import*
from PyQt5 import QtCore, QtGui, QtWidgets
from SnifferDevGui import Ui_MainWindow
import os.path
import time as t

#obj = SnifferBase()
#obj.openLogFile()
#obj.RegEx()
#mod_time = os.path.getctime("test7.txt")
#print(t.strftime("%d.%m.%Y %H:%M:%S",t.localtime(mod_time)))



# ====================================================================================================
# Load Asp Bus Sniffer QT GUI 
# ====================================================================================================
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_MainWindow()
	ex.show()
	Ui_MainWindow.printActivity(SnifferBase,'Qt GUI is started!')
	sys.exit(app.exec_())
