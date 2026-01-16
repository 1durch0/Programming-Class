import requests
import json
import time

def get_weather_codes():
    return {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast", 45: "Fog", 48: "Depositing rime fog",
        51: "Drizzle: Light", 53: "Drizzle: Moderate", 55: "Drizzle: Dense intensity", 56: "Freezing Drizzle: Light",
        57: "Freezing Drizzle: Dense", 61: "Rain: Slight", 63: "Rain: Moderate", 65: "Rain: Heavy",
        66: "Freezing Rain: Light", 67: "Freezing Rain: Heavy", 71: "Snow fall: Slight", 73: "Snow fall: Moderate",
        75: "Snow fall: Heavy", 77: "Snow grains", 80: "Rain showers: Slight", 81: "Rain showers: Moderate",
        82: "Rain showers: Violent", 85: "Snow showers: Slight", 86: "Snow showers: Heavy", 95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    }

def fetch_and_save_weather(input_file, output_file):
    url = "https://api.open-meteo.com/v1/forecast"
    weather_codes = get_weather_codes()
    
    with open(input_file, "r") as f:
        capitals_list = json.load(f)

    final_output = {}

    for capital in capitals_list:
        print(f"Processing {capital['city']}...")
        
        params = {
            "latitude": capital["lat"],
            "longitude": capital["lon"],
            "current_weather": True,
            "hourly": ["temperature_2m", "precipitation_probability", "weathercode"],
            "timezone": "auto"
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # getting current weather
            current = data["current_weather"]
            
            # hourly forecast for next hours(i)
            hourly_list = []
            for i in range(1):  # change number to number of hours 
                hourly_list.append({
                    "time": data["hourly"]["time"][i],
                    "temperature": data["hourly"]["temperature_2m"][i],
                    "precipitation_probability": data["hourly"]["precipitation_probability"][i],
                    "weathercode": data["hourly"]["weathercode"][i]
                })

            # dictionary structure for output
            final_output[capital["city"]] = {
                "country": capital["country"],
                "coordinates": {
                    "latitude": capital["lat"],
                    "longitude": capital["lon"]
                },
                "current_weather": {
                    "temperature": current["temperature"],
                    "windspeed": current["windspeed"],
                    "weathercode": current["weathercode"],
                    "condition": weather_codes.get(current["weathercode"], "Unknown"),
                    "time": current["time"]
                },
                "hourly_forecast": hourly_list
            }

        except Exception as e:
            print(f"Failed to fetch {capital['city']}: {e}")
        
        time.sleep(0.7) # delay for rate limit

    # dump into json file
    with open(output_file, "w") as out_f:
        json.dump(final_output, out_f, indent=4)
    
    print(f"\nSuccess! Weather data saved to {output_file}")

# execute
input_path = "/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week11/eu_capitals.json"
output_path = "/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week11/eu_weather_data.json"
fetch_and_save_weather(input_path, output_path)