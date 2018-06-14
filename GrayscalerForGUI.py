from tkinter import *
from PIL import Image #PIL(Pillow)のインポート

tk = Tk()
tk.title("Grayscaler")

label = Label(tk, text="画像のパスを入力してください")
label.pack()

Editbox = Entry()
Editbox.pack()

def grayscaling():
     filename = Editbox.get()
     image = Image.open(filename)
     gray = image.convert("L") #グレイスケール化
     gray.show()
     gray.save(filename) #保存

btn = Button(tk, text="グレイスケール化する", command=grayscaling)
btn.pack()

     
