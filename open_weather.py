import requests
from tkinter.simpledialog import *


api_key = "337aac7fc8858ecb0ce4d3c167bcbb6d"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# user_input = "tel aviv"
# city_name = input("Enter city name : ")

# while True:
window = Tk()
# window.geometry("+1000+600") # +position right + position down
# back = Frame(master=window, width=1500, height=1500, bg='white')
# back.pack()
window.withdraw()
# photo = PhotoImage(file = "weather.png")
# window.iconphoto(False, photo)
# window.minsize(550, 550)
user_input = askstring(title="Weather App",
                       prompt="enter city name",
                       initialvalue="please enter a city")
# n=n+1
while user_input == "" or not user_input:
    print("ERROR! - Cannot continue without a user input.")
    window = Tk()
    window.withdraw()

    user_input = messagebox.showerror(title="Weather App"
                                      ,message = "you did not enter any text")

complete_url = base_url + "appid=" + api_key + "&q=" + user_input
# weather_url = urllib.request.urlopen(complete_url)


response = requests.get(complete_url)
json_file = response.json()
if json_file["cod"] != "404":
    temp_location_in_json = json_file['main']['temp'] - 273.15   # turn Kelvin into Celzius (-273.15)

    window = Tk()
    window.withdraw()
    nl = '\n'
    if int(temp_location_in_json) < 10:
        output = messagebox.showinfo(title="Weather App"
                                     ,message=('The temperature in {0} is: {1}°C degrees {2}take a coat'
                                               .format(user_input.title(),
                                                       str(round(temp_location_in_json))
                                                       ,nl)))
    else:
        output = messagebox.showinfo(title="Weather App"
                                     ,message=('The temperature in {0} is: {1}°C degrees {2}no need for a coat'
                                               .format(user_input.title(),
                                                       str(round(temp_location_in_json))
                                                       ,nl)))

else:
    window = Tk()
    window.withdraw()
    output = messagebox.showerror(title="Weather App"
                                  ,message="City not found , try again")


# TODO: add a while loop to the Dialog
    # TODO: add a tray icon
        # TODO: define default,max, min window size
          # exe is here : https://drive.google.com/drive/u/0/folders/186ty_dCdMXVumnuLPs_7OlUGN5ajtsGa
      
