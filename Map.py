import io
import folium
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from City import *

class Ui_Map(QWidget):
    def __init__(self, city: City):
        super().__init__()
        self.setWindowTitle(city.name)
        self.window_width, self.window_height = 500, 300
        self.setMaximumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        data, coordinate = city.get_map()
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=10,
            location=coordinate
        )
        for i in data:
            station = i["station"]["name"]
            aqi = i["aqi"]
            folium.Marker(location=[i["lat"], i["lon"]], popup=station, tooltip=aqi).add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
