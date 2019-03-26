import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "edytor.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button_open.clicked.connect(self.file_dialog)

    def file_dialog(self):
        self.editor_window.setText('aaaaaaaaaaaa')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())