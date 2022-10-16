from fastapi import FastAPI
import requests
import datetime

app = FastAPI()


@app.get('/weather')
def get_weather(city):
    try:
        API_key = "b646c06a4b45966cd21d98a9275e488c"
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=ru")

        w_c = r.json()

        city_rn = w_c["name"]
        temp_c = w_c["main"]["temp"]
        weather_c = w_c["weather"][0]["description"]
        humidity = w_c["main"]["humidity"]
        wind = w_c["wind"]["speed"]
        pressure = w_c["main"]["pressure"]
        sunrise = datetime.datetime.fromtimestamp(w_c["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(w_c["sys"]["sunset"])

        return{f"Погода в {city_rn}: {weather_c}\nТемпература: {temp_c}°C\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм рт.ст.\n"
              f"Скорость ветра: {wind}м/с\nРассвет: {sunrise}\nЗакат: {sunset}"}

    except Exception as ex:
        return{ex}

@app.post('/')
def city(city):
    return get_weather(city)

if __name__ == "__main__":
    city()