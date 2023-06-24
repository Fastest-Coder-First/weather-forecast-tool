import urllib.parse
import urllib.request
import json
import sys

API_KEY = "4aa4b037f465e791a3d97dbe89e3bdda"

def get_weather_forecast(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    query_params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    url = base_url + "?" + urllib.parse.urlencode(query_params)

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data
    except urllib.error.HTTPError as e:
        print(f"Failed to retrieve weather forecast for {city}. Error: {e}")
    except urllib.error.URLError as e:
        print(f"Failed to connect to the weather service. Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse weather data. Error: {e}")

def display_weather_forecast(city, data):
    if data:
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} km/h")
    else:
        print("No weather data available.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_forecast.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    data = get_weather_forecast(city)
    display_weather_forecast(city, data)

if __name__ == "__main__":
    main()
