import requests
import datetime

# LIVE WEATHER API SETUP
api_key = 'place_api_key_here'
city = 'London'
country = 'United Kingdom'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}'
response = requests.get(url)
data = response.json()
temperature_fahrenheit = str(data['current']['temp_f'])
weather_condition_text = data['current']['condition']['text']
api_response_string = data
current_time = datetime.datetime.now()
prompt = (
    f"Today's Temperature {temperature_fahrenheit} degrees, "
    f"weather condition of {weather_condition_text} and the current "
    f"date and time {current_time} in London, UK."
)


print("COMMAND LINE ASSISTANT")
print('\'q\' or \'quit\' to exit')
print('\'w\' or \'weather\' for weather')
print(prompt)

while True:
  user_input = input('> ')
  if user_input.lower() == '':
    pass
  elif user_input.lower() in ['q', 'quit']:
    print("Bye!")
    break
  else:
    print(f"You've inputted: {user_input}, anything else?")
