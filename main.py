from MenuPage import *
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
