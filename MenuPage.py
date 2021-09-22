from Forecast import *
from RealTime import *
from Map import *
from Histogram import *


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("mainWindow")
        main_window.setEnabled(True)
        main_window.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 150, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 200, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 250, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 300, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 50, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("mainWindow", "Air Quality"))
        # Please put address of Background_Image.png from your computer here "address in your computer"
        main_window.setStyleSheet("#mainWindow{border-image:url(/address in your computer/Backgrounsd_Image.png)}")
        self.pushButton.setText(_translate("mainWindow", "London"))
        self.pushButton.clicked.connect(lambda: self.open_city_page("London"))
        self.pushButton_2.setText(_translate("mainWindow", "Madrid"))
        self.pushButton_2.clicked.connect(lambda: self.open_city_page("Madrid"))
        self.pushButton_3.setText(_translate("mainWindow", "Moscow"))
        self.pushButton_3.clicked.connect(lambda: self.open_city_page("Moscow"))
        self.pushButton_4.setText(_translate("mainWindow", "Paris"))
        self.pushButton_4.clicked.connect(lambda: self.open_city_page("Paris"))
        self.pushButton_5.setText(_translate("mainWindow", "Ankara"))
        self.pushButton_5.clicked.connect(lambda: self.open_city_page("Ankara"))
        self.label.setText(_translate("mainWindow", "Please choose city:"))

    def open_city_page(self, city_name):
        city = City(city_name)

        # Forecast Window
        self.Forecast = QtWidgets.QMainWindow()
        self.ui_forecast = Ui_Forecast()
        self.ui_forecast.setupUi(self.Forecast, city)
        self.Forecast.show()

        # Real Time Window
        self.RealTime = QtWidgets.QMainWindow()
        self.ui_real = Ui_RealTime()
        self.ui_real.setupUi(self.RealTime, city)
        self.RealTime.show()

        # Map Window
        self.map = Ui_Map(city)
        self.map.show()

        # Histogram Page
        self.histogram = UI_Histogram(city)
        self.histogram.show()

