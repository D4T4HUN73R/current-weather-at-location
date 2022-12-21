import requests

def get_weather(api_key, location):
    # Set the API endpoint and parameters
    endpoint = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": "metric",
        "appid": api_key
    }

    # Make the API call
    response = requests.get(endpoint, params=params)

    # Check the status code
    if response.status_code == 200:
        # Get the weather data from the response
        data = response.json()

        # Extract the weather conditions
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Print the weather conditions
        print(f"The weather in {location} is {weather} with a temperature of {temperature}°C and a humidity of {humidity}%.")
    else:
        print("Error:", response.status_code)

def main():
    # Prompt the user for the API key and location
    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter the location: ")

    # Get the weather for the location
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
