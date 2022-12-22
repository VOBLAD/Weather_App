from pyowm import OWM
from pyowm.utils.config import get_default_config
from tkinter import *

def weather():
   config_dict = get_default_config()
   config_dict['language'] = 'ru'
   place = ci.get()
   owm = OWM('642612a158a6d2e9b4f6fae63737dbac')
   mgr = owm.weather_manager()
   observation = mgr.weather_at_place(place)
   w = observation.weather
   status = w.detailed_status
   w.wind()
   humidity = w.humidity
   temp = w.temperature('celsius')['temp']
   lbl.config(text="В городе " + str(place) + " сейчас " + str(status) + ":" +
          "\nТемпература " + str(round(temp)) + " градусов по цельсию:" +
          "\nВлажность составляет " + str(humidity) + "%:" +
          "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду:")




root = Tk()
root.geometry("500x450")
root.config(bg="orange")
root.title("Погода")
root.resizable(False, False)
icon = PhotoImage(file="1.png")

lbl1 = Label(root, text="Введите свой город", bg="orange", font="Arial 15 bold")
lbl1.pack(pady=40)

lbl = Label(root, bg="orange", font="Arial 15 bold")
lbl.pack(side=BOTTOM, pady=30)

ci = Entry(root, width=25, font="Arial 17 bold")
ci.pack()

btn = Button(root, command=weather, image=icon, relief=FLAT, bg="orange")
btn.pack(pady=40)


root.mainloop()
