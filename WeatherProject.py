# This python program finds the current weather forecast of any city
# Using openweathermap.org API

print("This program searches for current weather data of any City.")
def main():
  # Import module
  import json, requests

  base_url = "https://api.openweathermap.org/data/2.5/weather"
  api_key = "39513b4d96eab8c7fa975552350ca28e"

  print()
  try:
    city_name = input("Enter the city name or zip code: ")
    # Base URL with API key
    url = f"{base_url}?q={city_name}&units=imperial&APPID={api_key}"
    print(f"Connecting to: {url}")
    print()

    response = requests.get(url)
    unformated_data = response.json()

    #print(unformated_data)
    
    print("Connection to webservice successful.")
    print(f"Showing weather forecast for: {city_name.title()}")
    # Formated data to be printed below
    temp = unformated_data["main"]["temp"]
    print(f"\nThe current temperature is: {temp}")

    temp_max = unformated_data["main"]["temp_max"]
    print(f"The maximum temperature is: {temp_max}")

    feels_like = unformated_data["main"]["feels_like"]
    print(f"The current temperature feels like: {feels_like}")

    humidity = unformated_data["main"]["humidity"]
    print(f"The current humidity is {humidity}%")

  except: # If entered city name is not recognized.
    print(f'\nAn unexpected error occured - "{city_name}" not found. Please try again.')
    main()
main()
# End Function asking if user wants to initiate another search.
def End():
  new_search = input('\nWould you like to start a new search? Enter "yes" or "no": ')
  if new_search == 'yes' or new_search == 'Yes' or new_search == 'YES' or new_search == 'y':
    main()
    End()
  else:
    print("Ending the program. Thank you and have a good day.")

End()