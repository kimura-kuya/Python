import requests
import tkinter as tk

root = tk.Tk()
root.title("天気予報")
var = tk.StringVar()
var.set("天気取得")

label = tk.Label(root, textvariable=var)
label.pack()
def update(event):
     url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=130010"
     r = requests.get(url)
     weather = r.json()["forecasts"][0]["telop"]
     var.set(weather)
     #天気取得

label.bind("<ButtonPress-1>", update)
root.mainloop()
