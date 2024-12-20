from random import randint
from time import sleep
from mihaniki import *
from infarmakiya import *

print("Этот мир находится на пороге паровых мехонизмов так что люди не сильно удивляются разным технологиям")
sleep(1)
print("""Так же этот мир находится на перепутье нескольких реальностей так что 
некоторые предметы или даже живые существа могут случайным образом попасть в этот мир""")
sleep(1)
player["Name"] = input("Ваше имя путник:   ")
print("""Вы обычный искатель прикльчений которому очень нужно попасть в сталицу
Но беда путь в сталицу заблокировал завал""")
sleep(1)


current_enemy = "ENEMI_1"

while True:
    a = 1
    b = 1
    actions = int(input('''Ваши действия
                     1 -- Ваша статистика
                     2 -- Пойти на торговую площадь
                     3 -- Идти тренироватся
                     4 -- Пойти в гильдию
                     5 -- Пойти к гильд мастеру за разришением на выезд из города
                        
                        '''))
    
    if actions == 1:
        display_player()
        display_inventory()
    
    
    if actions == 2:
         actions_2 = int(input('''Вкакой магазин: 
         1 -- Кузня
         2 -- Скупщик
         3 -- Магазин разных бездилушек
         
         '''))
         if actions_2 == 1:
            forge()
         elif actions_2 == 2:
            buyer()
         elif actions_2 == 3:
            shop()
         

    if actions == 3:
         treining()
     

    
    if actions == 4:
         actions_4 = int(input('''Куда подойти?  
         1 -- Доска заказов
         2 -- отдохнуть
         3 -- взять заказ
         4 -- Страный рыцарь в страных доспехах
         5 -- енциклопедия
         

                              '''))
         if actions_4 == 1:
            bulletin_board()

         elif actions_4 == 2:
            rest()

         elif actions_4 == 3:
            wibor_fight()

               
         elif actions_4 == 4:
            cosmadisantnik()

         elif actions_4 == 5:
            encyclopedia()
         

    if actions == 5:  
        actionssss = input("Ну что пришол за разришением? (да\нет)")  
        sleep(0.8)
        if actionssss == "да":
            if "камень с развалин чегото" in player["Inventory"]:
                print("Ты протягиваешь ему каменьс того завала")
                sleep(1)
                print("""Ладно верю, вот тебе твой пропуск
                       иди ты уже не мешай""")
                sleep(1)
                print("!!!!!!!!!!!!!ПОЗДРАВЛЯЮ ТЫ ПРОШОЛ ИГРУ!!!!!!!!!!!!!!")
                break
            else:
                print("Принеси доказательства, тогда и дам тебе пропуск")
                sleep(0.8)
        else:
            print("Тогда не задержива")
            sleep(0.8)
    else:
        print("")