import requests
from tkinter import *

api_key = 'Here is your API Key from openweather map'

root = Tk()
root.title('Weather App')
root.geometry('340x330')

average = {
    'temp': [],
    'feels_like': [],
    'temp_min': [],
    'temp_max': [],
    'pressure': [],
    'humidity': [],
    'wind_speed': [],
}

def submit(city):
    url = "http://api.openweathermap.org/data/2.5/find?q=" + str(city.get()) + "&units=metric&appid=" + api_key
    response = requests.get(url)
    data = response.json()

    if len(data['list']) == 1:
        main = data['list'][0]['main']
        wind = data['list'][0]['wind']

        # INFORMATION
        temp = str(main['temp']) + '°C'
        feels_like = str(main['feels_like']) + '°C'
        temp_min = str(main['temp_min']) + '°C'
        temp_max = str(main['temp_max']) + '°C'
        pressure = str(main['pressure']) + 'hPa'
        humidity = str(main['humidity']) + '%'
        wind_speed = str(round(wind['speed']*3.6, 2)) + 'km/h'

    elif len(data['list']) > 1:
        for dict in range(len(data['list'])):
            main = data['list'][dict]['main']
            wind = data['list'][dict]['wind']
            weather = data['list'][dict]['weather'][0]

            average['temp'].append(main['temp'])
            average['feels_like'].append(main['feels_like'])
            average['temp_min'].append(main['temp_min'])
            average['temp_max'].append(main['temp_max'])
            average['pressure'].append(main['pressure'])
            average['humidity'].append(main['humidity'])
            average['wind_speed'].append(wind['speed'])
        
        # AVERAGE OF ALL NUMERIC DATA
        temp_average = 0
        feels_like_average = 0
        temp_min_average = 0
        temp_max_average = 0
        pressure_average = 0
        humidity_average = 0
        wind_speed_average = 0

        for num in average['temp']:
            temp_average += num
        temp_average /= len(average['temp'])
        
        for num in average['feels_like']:
            feels_like_average += num
        feels_like_average /= len(average['feels_like'])
        
        for num in average['temp_min']:
            temp_min_average += num
        temp_min_average /= len(average['temp_min'])
        
        for num in average['temp_max']:
            temp_max_average += num
        temp_max_average /= len(average['temp_max'])
        
        for num in average['pressure']:
            pressure_average += num
        pressure_average /= len(average['pressure'])
        
        for num in average['humidity']:
            humidity_average += num
        humidity_average /= len(average['humidity'])
        
        for num in average['wind_speed']:
            wind_speed_average += num
        wind_speed_average /= len(average['wind_speed'])

        # INFORMATION
        temp = str(round(temp_average, 2)) + '°C'
        feels_like = str(round(feels_like_average, 2)) + '°C'
        temp_min = str(round(temp_min_average, 2)) + '°C'
        temp_max = str(round(temp_max_average, 2)) + '°C'
        pressure = str(round(pressure_average, 2)) + 'hPa'
        humidity = str(round(humidity_average, 2)) + '%'
        wind_speed = str(round(wind_speed_average*3.6, 2)) + 'km/h'

    weather = data['list'][0]['weather'][0]
    description = str(weather['description']).capitalize()

    # INFORMATION LABELS
    temp_result = Label(root, text=temp, font=('comicsans', 12))
    temp_result.grid(row=2, column=1, padx=10, pady=(10,0), sticky=W)
    
    feels_like_result = Label(root, text=feels_like, font=('comicsans', 12))
    feels_like_result.grid(row=3, column=1, padx=10, sticky=W)
    
    temp_min_result = Label(root, text=temp_min, font=('comicsans', 12))
    temp_min_result.grid(row=4, column=1, padx=10, sticky=W)
    
    temp_max_result = Label(root, text=temp_max, font=('comicsans', 12))
    temp_max_result.grid(row=5, column=1, padx=10, sticky=W)
    
    pressure_result = Label(root, text=pressure, font=('comicsans', 12))
    pressure_result.grid(row=6, column=1, padx=10, sticky=W)
    
    humidity_result = Label(root, text=humidity, font=('comicsans', 12))
    humidity_result.grid(row=7, column=1, padx=10, sticky=W)
    
    wind_speed_result = Label(root, text=wind_speed, font=('comicsans', 12))
    wind_speed_result.grid(row=8, column=1, padx=10, sticky=W)
    
    description_result = Label(root, text=description, font=('comicsans', 12))
    description_result.grid(row=9, column=1, padx=10, sticky=W)
    
    city.delete(0, END)
    

# TITLE
title = Label(root, text='Weather App', font=('comicsans', 20))
title.grid(row=0, column=0, columnspan=2, pady=10, padx=80)

# ASK FOR CITY
city_label = Label(root, text='City Name: ', font=('comicsans', 12))
city_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

city = Entry(root)
city.grid(row=1, column=1, ipady=3, sticky=W)

# SUBMIT BUTTON
submit_btn = Button(root, text='Submit', command=lambda : submit(city))
submit_btn.grid(row=1, column=1, columnspan=2, sticky=E)

# INFORMATION LABELS
temp_label = Label(root, text='Temperature: ', font=('comicsans', 12))
temp_label.grid(row=2, column=0, padx=10, pady=(10,0), sticky=W)

feels_like_label = Label(root, text='Feels Like: ', font=('comicsans', 12))
feels_like_label.grid(row=3, column=0, padx=10, sticky=W)

min_temp_label = Label(root, text='Min Temperature: ', font=('comicsans', 12))
min_temp_label.grid(row=4, column=0, padx=10, sticky=W)

max_temp_label = Label(root, text='Max Temperature: ', font=('comicsans', 12))
max_temp_label.grid(row=5, column=0, padx=10, sticky=W)

pressure_label = Label(root, text='Pressure: ', font=('comicsans', 12))
pressure_label.grid(row=6, column=0, padx=10, sticky=W)

humidity_label = Label(root, text='Humidity: ', font=('comicsans', 12))
humidity_label.grid(row=7, column=0, padx=10, sticky=W)

wind_label = Label(root, text='Wind Speed: ', font=('comicsans', 12))
wind_label.grid(row=8, column=0, padx=10, sticky=W)

decription_label = Label(root, text='Description: ', font=('comicsans', 12))
decription_label.grid(row=9, column=0, padx=10, sticky=W)

root.mainloop()