import requests


class City:
    real_aqi: int
    real_iaqi: dict
    forecast: dict

    def __init__(self, name):
        self.name = name
        self.get_info()

    def get_info(self):
        url = "https://api.waqi.info/feed/" + self.name + "/?token=d8a7e6c3562fb9f79c6b5f7294f61ec6177a739d"
        response = requests.get(url)
        data: dict = response.json()

        self.real_aqi = data["data"]["aqi"]
        self.real_iaqi = data["data"]["iaqi"]
        self.forecast = data["data"]["forecast"]["daily"]

    def get_map(self):
        if self.name == "London":
            latlng = "51.543372,-0.205819,51.470503,-0.029694"
            coordinate = (51.509865, -0.118092)
        elif self.name == "Madrid":
            latlng = "40.494810,-3.795586,40.358385,-3.566933"
            coordinate = (40.416775, -3.703790)
        elif self.name == "Moscow":
            latlng = "55.897720,37.341498,55.591614,37.830390"
            coordinate = (55.751244, 37.618423)
        elif self.name == "Paris":
            latlng = "48.898125,2.2584810,48.816580,2.4081697"
            coordinate = (48.864716, 2.349014)
        elif self.name == "Ankara":
            latlng = "40.006456,32.536164,39.857977,32.997590"
            coordinate = (39.922252494443676, 32.85820138051686)

        url = "https://api.waqi.info/map/bounds/?latlng=" + latlng + "&token=d8a7e6c3562fb9f79c6b5f7294f61ec6177a739d"
        response = requests.get(url)
        data: dict = response.json()
        data = data["data"]
        return data, coordinate

    def get_real_aqi(self) -> str:
        return str(self.real_aqi)

    def get_real_co(self) -> str:
        return str(self.real_iaqi["co"]["v"])

    def get_real_no2(self) -> str:
        return str(self.real_iaqi["no2"]["v"])

    def get_real_o3(self) -> str:
        return str(self.real_iaqi["o3"]["v"])

    def get_real_so2(self) -> str:
        return str(self.real_iaqi["so2"]["v"])

    def get_real_pm10(self) -> str:
        return str(self.real_iaqi["pm10"]["v"])

    def get_real_pm25(self) -> str:
        return str(self.real_iaqi["pm25"]["v"])

    def get_forecast_o3(self) -> list:
        return self.forecast["o3"]

    def get_forecast_pm10(self):
        return self.forecast["pm10"]

    def get_forecast_pm25(self):
        return self.forecast["pm25"]
