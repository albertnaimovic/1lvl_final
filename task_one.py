# Create class that woud represent weather. This class takes several parameters (wind speed (km/h) and temperature(F))
# This class should be able to return weather conditions:
# 1) Weather temperature in K , C , F
# 2) Wind speed in m/s , km/h , miles/h
# 3) Weather conditions : good (wind speed < 5m/s,  temp > 0C < 25 C) ,normal (wind speed < 10m/s,  temp > -15C < 28 C), bad (wind speed > 10m/s,  temp < -15C or > 30 C),
# savere (wind speed > 15m/s,  temp < -25C or > 40 C)
# Use inheritance, private/protected methods/attributes if needed.


class WeatherConversion:
    def __init__(self, wind_speed_kmph: float, temperature_fahrenheit: float) -> None:
        self.__wind_speed_kmph = wind_speed_kmph
        self.__temperature_fahrenheit = temperature_fahrenheit

    def temperature_celsius(self) -> float:
        return round(((self.__temperature_fahrenheit - 32) * 5) / 9, 2)

    def temperature_kelvin(self) -> float:
        return round(273.5 + ((self.__temperature_fahrenheit - 32) * (5 / 9)), 2)

    def temperature_fahrenheit(self) -> float:
        return self.__temperature_fahrenheit

    def wind_speed_mps(self) -> float:
        return round((self.__wind_speed_kmph * 1000) / 3600, 2)

    def wind_speed_mph(self) -> float:
        return round((0.6214 * self.__wind_speed_kmph), 2)

    def wind_speed_kmph(self) -> float:
        return self.__wind_speed_kmph


class WeatherCondition(WeatherConversion):
    def __init__(self, wind_speed_kmph: float, temperature_fahrenheit: float) -> None:
        super().__init__(wind_speed_kmph, temperature_fahrenheit)

    def get_weather_condition(self) -> str:
        temp_celsius = self.temperature_celsius()
        wind_speed_mps = self.wind_speed_mps()
        if wind_speed_mps < 5.0 and (0 < temp_celsius < 25.0):
            return "Weather condition is good"
        elif wind_speed_mps < 10.0 and (-15.0 < temp_celsius < 30.0):
            return "Weather condition is normal"
        elif wind_speed_mps > 10.0 or ((-25.0 < temp_celsius < -15.0) or (30.0 < temp_celsius < 40.0)):
            return "Weather condition is bad"
        elif wind_speed_mps > 15.0 or (temp_celsius < -25.0 or temp_celsius > 40.0):
            return "Weather condition is savere"
        else:
            return "You are in Lithuania"


weather = WeatherCondition(wind_speed_kmph=15.0, temperature_fahrenheit=70.0)

if __name__ == "__main__":
    try:
        print(f"Wind speed in m/s: {weather.wind_speed_mps()}")
        print(f"Temperature in celsius: {weather.temperature_celsius()}")
        print(weather.get_weather_condition())
    except Exception as err:
        print(f"You got an error: {err}")
