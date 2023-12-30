import urllib.request
import json

def get_weather_data(api_key, location):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': location
    }

    # Construct the URL with parameters
    url = f"{base_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"

    try:
        # Make the API request
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.URLError as e:
        print(f"Error accessing the API: {e}")
        return None

def main():
    api_key = '7d0df2528f4e5ee40342621af1a07768'
    location = input("Enter the location: ")

    # Get weather data
    weather_data = get_weather_data(api_key, location)

    if weather_data:
        # Parse and display relevant information
        temperature = weather_data['current']['temperature']
        description = weather_data['current']['weather_descriptions'][0]
        print(f"The current temperature in {location} is {temperature}°C, and the weather is {description}.")
    else:
        print("Unable to retrieve weather information.")

if __name__ == "__main__":
    main()
