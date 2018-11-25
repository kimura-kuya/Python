enemyname = "スライム"
playername = "ゆうしゃ"
enemyhp = 20
playerhp = 35
import random as rd
print("あ！",enemyname,"が現れた！")
while 1:
     action = input("どうする？ 1:攻撃 2:防御 ")
     if action == "":
          continue
     
     action = int(action)
     if action != 1 and action != 2:
          continue
     
     if action == 1:
          enemydamage = rd.randint(3,10)
          print(playername,"の攻撃！",enemyname,"に",enemydamage,"のダメージ！")
          enemyhp = enemyhp - enemydamage
          
     if enemyhp <= 0:
          print(playername,"は",enemyname,"を倒した！")
          break
     
     elif not enemyhp <= 0 and action != 2:
          print("残りHP",enemyhp,"!")
     
     playerdamage = rd.randint(5,7)
     if action == 2:
          playerdamage = playerdamage -4
          
     print(enemyname,"の攻撃！",playername,"に",playerdamage,"のダメージ！")
     playerhp = playerhp - playerdamage
     if playerhp <= 0:
          print(playername,"は倒れてしまった！")
          break
     
     print("残りHP",playerhp,"!")         
    
          
