import customtkinter as ctk
import requests
from PIL import Image
# Example API Key: 9afca9cbadeedaaaa12abcf2c8d397cd

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()
app.geometry("440x480")
app.title("Goofy Weather App")

logo = ctk.CTkImage(light_image=Image.open("./images/logo-light.png"),
                                  dark_image=Image.open("./images/logo-dark.png"),
                                  size=(100, 100))
logo_label = ctk.CTkLabel(app, image=logo, text="")  # display image with a CTkLabel
logo_label.place(relx=0.38, rely=0.03)

def city():
    city = city_entry.get()
    print(city)

def forecast():
    api_key = api_entry.get()
    city = city_entry.get()
    units = units_menu.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        if units == "Metric":
            output.configure(state="normal")
            output.delete('0.0', 'end')
            output.insert('end', f'🌡️ Temperature: {temp}C')
            output.insert('end', f'\n🗨️ Description: {desc}')
            output.configure(state="disabled")
        elif units == "Imperial":
            output.configure(state="normal")
            output.delete('0.0', 'end')
            output.insert('end', f'🌡️ Temperature: {temp}F')
            output.insert('end', f'\n🗨️ Description: {desc}')
            output.configure(state="disabled")
        elif units == "Standard":
            output.configure(state="normal")
            output.delete("0.0", 'end')
            output.insert('end', f'🌡️ Temperature: {temp}K')
            output.insert('end', f'\n🗨️ Description: {desc}')
            output.configure(state="disabled")
    else:
        output.delete("0.0", "end")
        output.insert('0.0', 'Error fetching weather data')
        output.configure(state="disabled")

output = ctk.CTkTextbox(app, width=250, height=150)
output.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)
output.insert('0.0', 'Welcome to the Goofy Weather App!\n\nInsert your OpenWeatherMap API Key')

units_menu = ctk.CTkOptionMenu(app, values=["Metric", "Imperial", "Standard"])
units_menu.set("Set unit of measurement")
units_menu.place(relx=0.5, rely=0.299, anchor=ctk.CENTER)

api_entry = ctk.CTkEntry(master=app, width=250, placeholder_text="Insert API Key")
api_entry.place(relx=0.5, rely=0.38, anchor=ctk.CENTER)

city_entry = ctk.CTkEntry(master=app, width=250, placeholder_text="Insert City Name")
city_entry.place(relx=0.5, rely=0.46, anchor=ctk.CENTER)

forecast_button = ctk.CTkButton(master=app, text="Show Forecast", command=forecast)
forecast_button.place(relx=0.5, rely=0.54, anchor=ctk.CENTER)

app.mainloop()