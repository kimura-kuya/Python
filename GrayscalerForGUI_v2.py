import tkinter
import tkinter.filedialog
from PIL import Image #PIL(Pillow)のインポート
import os

root = tkinter.Tk()
root.title("Grayscaler")

var = tkinter.StringVar()

label = tkinter.Label(root,textvariable=var)
label.pack()

def fileselect():
    global file
    file = tkinter.filedialog.askopenfilename()
    var.set("File:" + file)
    
def grayscaling():   
    image = Image.open(file)
    gray = image.convert("L") #グレイスケール化
    gray.show()
    if bl.get():
        gray.save(file)
    else:
        filename,kakuchousi = os.path.splitext(file)
        gray.save(filename + "_gray" + kakuchousi)

filebtn = tkinter.Button(root,text="ファイル選択",command=fileselect)
filebtn.pack()

bl = tkinter.BooleanVar()
uwagaki = tkinter.Checkbutton(root,variable=bl,text="上書き保存するか")
uwagaki.pack()

btn = tkinter.Button(root, text="グレイスケール化する", command=grayscaling)
btn.pack()

root.mainloop()
