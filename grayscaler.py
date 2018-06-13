import sys
from PIL import Image #PIL(Pillow)のインポート
image_name = sys.argv[1] #コマンドライン引数(ファイルのパス)の取得

image = Image.open(image_name)
gray = image.convert("L") #グレイスケール化
gray.show() #表示

gray.save(image_name) #保存
