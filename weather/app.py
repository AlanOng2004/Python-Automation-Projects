import requests

api_key = 'CcW30lM7QQYjmpZrH3Q5JsUC0B4rKLcA'
city_name = 'Singapore'

# Use f-string for formatting the URL
location_url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city_name}'

response = requests.get(location_url)

def findLocation():
    if response.status_code == 200:
        data = response.json()

        if data:
            location_key = data[0]["Key"]
            print(f"Location Key for {city_name}: {location_key}")
            return location_key

        else:
            print("No data found for the location.")
    else:
        print("Error fetching location data:", response.status_code)


def findWeather(location_key):    

    weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}'
            
    weather_response = requests.get(weather_url)

    if weather_response.status_code == 200:
        weather_data = weather_response.json()

        if weather_data:
            # Extract and print relevant weather information
            temperature = weather_data[0]["Temperature"]["Metric"]["Value"]
            weather_text = weather_data[0]["WeatherText"]
            print(f"Current temperature in {city_name}: {temperature}°C")
            print(f"Weather conditions: {weather_text}")
    else:
        print("Error fetching weather data:", weather_response.status_code)

def forecastWeather(location_key):
    forecast_url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey={api_key}'

    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()

        if forecast_data:
            minTempFahrenheit = forecast_data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
            minTemperature = fahrenheitToCelsius(minTempFahrenheit)
            print(f"Tomorrow's minimum temperature in {city_name}: {minTemperature}°C")

            maxTempFahrenheit = forecast_data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
            maxTemperature = fahrenheitToCelsius(maxTempFahrenheit)
            print(f"Tomorrow's maximum temperature in {city_name}: {maxTemperature}°C")

        else:
            print("No forecast data available.")
    else:
        print("Error fetching forecast data:", forecast_response.status_code)

def fahrenheitToCelsius(temperature):
    celsiusTemp = (temperature - 32) * 5/9
    return round(celsiusTemp, ndigits = 1)

location = findLocation()
findWeather(location)
forecastWeather(location)

