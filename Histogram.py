from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import Qt
from City import *


class UI_Histogram(QMainWindow):
    def __init__(self, city: City):
        super().__init__()
        self.resize(450, 300)
        self.setWindowTitle(city.name)

        seto3 = QBarSet('O3')
        setpm10 = QBarSet('PM10')
        setpm25 = QBarSet('PM2.5')

        days, o3, pm10, pm25 = self.get_forecaste_info(city)

        seto3.append(o3)
        setpm10.append(pm10)
        setpm25.append(pm25)

        series = QBarSeries()
        series.append(seto3)
        series.append(setpm10)
        series.append(setpm25)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Forecast Histograms")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        time_period = days

        axisX = QBarCategoryAxis()
        axisX.append(time_period)

        axisY = QValueAxis()
        maximum = 0
        for i in range(5):
            tmp = max(o3[i], pm10[i], pm25[i])
            if tmp > maximum:
                maximum = tmp

        axisY.setRange(0, maximum)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        self.setCentralWidget(chartView)

    def get_forecaste_info(self, city: City):
        days = list()
        o3 = list()
        pm10 = list()
        pm25 = list()
        for i in range(5):
            days.append(str(city.forecast["o3"][i]["day"][5:]))
            o3.append(float(city.forecast["o3"][i]["avg"]))
            pm10.append(float(city.forecast["pm10"][i]["avg"]))
            pm25.append(float(city.forecast["pm25"][i]["avg"]))
        return days, o3, pm10, pm25