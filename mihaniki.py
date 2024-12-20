
from random import randint
from time import sleep
from infarmakiya import *
import infarmakiya 



def display_player():
    print(f'Игрок - {player["Name"]}')
    print(f'Здоровье - {player["HP"]}')
    print(f'Деньги - {player["Money"]}')
    print(f'Выносливость - {player['Stamina']}')  
    print(f'Урон - {player["DMG"]}')  
    print(f"удача - {player["Laki"]}")
    print(f"броня - {player["Armor"]}")
    print(f"победы - {player["win"]}")
    print(f"Зелья лечения - {player["healing potion"]}")
    
def display_inventory():
    print(f'У вас есть:')
    for value in player['Inventory']:
        print(value)
        sleep(1)
        if "Зелья четырёх листного клевера" in player["Inventory"]:
            vipit_vodka = input("""Хотите выприть зелье четырёх листного клевера чтобы повысить удачу?
                                (да\нет)
                                """)
            if vipit_vodka == "да":
                player["Inventory"].remove("Зелья четырёх листного клевера")
                player["Laki"] += 10
                sleep(1)
                print(f"""Ты чуствуешь что ты стал более удачливым
                        Теперь твоя удача равна - {player["Laki"]}""")
                sleep(1)


def forge():
    blacksmith = input("Привет путник, пришол за новым оружием или доспехами?    (да\нет)")
    if blacksmith == "да":
        blacksmith_gg = int(input("""
                               1 -- доспехи
                               2 -- оружие
                               """))
        if blacksmith_gg == 2:
                sleep(1)
                blacksmith_sword = int(input("""Ну тогда вот весь мой асортимент
                            1 -- Деревяный меч (+5 урон) 1000 утэнав
                            2 -- Бронзавый меч (+10 урон) 1500 утэнав
                            3 -- Железный меч (+15 урон) 2000 утэнав
                            4 -- Стальной меч (+20 урон) 2500 утэнав
                            5 -- Меч путешественника (+25 урона +20 выносливости) 4000 утэнав
                            6 -- Мифриловый меч (+35 урона) 5000 утэнав
                            7 -- Адамантивый меч (+40 урона) 7000 утэнав
                            
                            """))
                sleep(1)
                if blacksmith_sword == 0:
                    print("Ну раз не можешь определится то проваливай")
                elif blacksmith_sword == 1:
                    if player["Money"] >= 1000:
                        player["Money"] -= 1000
                        if "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Адамантивый меч" or "Цепной меч" in player['Inventory']:
                            print("У тебя уже есть более мощный меч")
                        player['Inventory'].append("Деревяный меч")
                        player["DMG"] += 5
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 2:
                    if player["Money"] >= 1500:
                        player["Money"] -= 1500
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Бронзавый меч")
                        player["DMG"] += 10
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 3:
                    if player["Money"] >= 2000:
                        player["Money"] -= 2000
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Железный меч")
                        player["DMG"] += 15
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 4:
                    if player["Money"] >= 2500:
                        player["Money"] -= 2500
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Стальной меч")
                        player["DMG"] += 20
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 5:
                    if player["Money"] >= 4000:
                        player["Money"] -= 4000
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Меч путешественника")
                        player["DMG"] += 25
                        player["Stamina"] += 20
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]} {player["Stamina"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 6:
                    if player["Money"] >= 5000:
                        player["Money"] -= 5000
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Мифриловый меч")
                        player["DMG"] += 35
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        print("Тебе не хватает денег на этот меч")

                elif blacksmith_sword == 7:
                    if player["Money"] >= 7000:
                        player["Money"] -= 7000
                        if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" in player['Inventory']:
                                forge_sword()
                        player['Inventory'].append("Адамантивый меч")
                        player["DMG"] += 40
                        sleep(1)
                        print(f"Теперь ваш урон равен {player["DMG"]}")
                    else:
                        sleep(1)
                        print("Тебе не хватает денег на этот меч")

        if blacksmith_gg == 1:
                sleep(1)
                blacksmith_Armor = int(input("""Ну тогда вот весь мой асортимент
                            1 -- Кожаные латы (+5 защиты) 1000 утэнав
                            2 -- Кожаные латы с железными вставками (+10 урон) 1500 утэнав
                            3 -- Кольчуга (+15 защиты) 2000 утэнав
                            4 -- Стальная кольчуга (+20 защиты) 2500 утэнав
                            5 -- Доспехи путешественника (+25 защиты +15 выносливости) 4000 утэнав
                            6 -- Мифриловая кольчуга (+30 защиты) 5000 утэнав
                            7 -- Адамантивая кольчуга (+35 защиты) 7000 утэнав
                            
                            """))
                sleep(1)
                if blacksmith_Armor == 0:
                    print("Ну раз не можешь определится то проваливай")
                elif blacksmith_Armor == 1:
                    if player["Money"] >= 500:
                        player["Money"] -= 500
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Кожаные латы")
                        player["Armor"] -= 0.6
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 2:
                    if player["Money"] >= 1000:
                        player["Money"] -= 1000
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Кожаные латы с железными вставками")
                        player["Armor"] -= 0.11
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 3:
                    if player["Money"] >= 1500:
                        player["Money"] -= 1500
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Железмечный ")
                        player["Armor"] -= 0.16
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 4:
                    if player["Money"] >= 2000:
                        player["Money"] -= 2000
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Стальная кольчуга")
                        player["Armor"] -= 0.21
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 5:
                    if player["Money"] >= 3000:
                        player["Money"] -= 3000
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Доспехи путешественника")
                        player["Armor"] -= 0.20
                        player["Stamina"] += 26
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 6:
                    if player["Money"] >= 4000:
                        player["Money"] -= 4000
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Мифриловая кольчуга")
                        player["Armor"] -= 0.31
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        print("Тебе не хватает денег на этот доспех")

                elif blacksmith_Armor == 7:
                    if player["Money"] >= 6000:
                        player["Money"] -= 6000
                        if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
                                Armor()
                        player['Inventory'].append("Адамантивая кольчуга")
                        player["Armor"] -= 0.36
                        sleep(1)
                        print(f"Теперь ваша защита равна {player["Armor"]}")
                    else:
                        sleep(1)
                        print("Тебе не хватает денег на этот доспех")
    else:
        print("Ну и проваливай раз не что ненужно")
def forge_sword():
    if "Адамантивый меч" or "Мифриловый меч" or "Меч путешественника" or "Стальной меч" or "Железный меч" or "Бронзавый меч" or "Деревяный меч" or "Кожаные латы" in player['Inventory']:
        if "Адамантивый меч" in player['Inventory']:
            player['Inventory'].remove("Адамантивый меч")
            player["DMG"] -= 40
        elif "Мифриловый меч" in player['Inventory']:
            player['Inventory'].remove("Мифриловый меч")
            player["DMG"] -= 35
        elif "Меч путешественника" in player['Inventory']:
            player['Inventory'].remove("Меч путешественника")
            player["DMG"] -= 25
        elif "Стальной меч" in player['Inventory']:
            player['Inventory'].remove("Стальной меч")
            player["DMG"] -= 25
        elif "Железный меч" in player['Inventory']:
            player['Inventory'].remove("Железный меч")
            player["DMG"] -= 15
        elif "Бронзавый меч" in player['Inventory']:
            player['Inventory'].remove("Бронзавый меч")
            player["DMG"] -= 10
        elif "Кожаные латы" in player['Inventory']:
            player['Inventory'].remove("Деревяный меч")
            player["DMG"] -= 5
def Armor():
    if "Мифриловая кольчуга" or "Доспехи путешественника" or "Стальная кольчуга" or "Кольчуга" or "Адамантивая кольчуга" or "Кожаные латы с железными вставками" or "Кожаные латы" in player['Inventory']:
        if "Адамантивая кольчуга" in player['Inventory']:
            player['Inventory'].remove("Адамантивая кольчуга")
            player["Armor"] += 0.36
        elif "Мифриловая кольчуга" in player['Inventory']:
            player['Inventory'].remove("Мифриловая кольчуга")
            player["Armor"] += 0.31
        elif "Доспехи путешественника" in player['Inventory']:
            player['Inventory'].remove("Доспехи путешественника")
            player["Armor"] += 0.26
        elif "Стальная кольчуга" in player['Inventory']:
            player['Inventory'].remove("Стальная кольчуга")
            player["Armor"] += 0.21
        elif "Кольчуга" in player['Inventory']:
            player['Inventory'].remove("Кольчуга")
            player["Armor"] += 0.16
        elif "Кожаные латы с железными вставками" in player['Inventory']:
            player['Inventory'].remove("Кожаные латы с железными вставками")
            player["Armor"] += 0.11
        elif "Кожаные латы" in player['Inventory']:
            player['Inventory'].remove("Кожаные латы")
            player["Armor"] += 0.6




def fight(current_enemy):
    rounds = randint(1, 2)
    enemi = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["HP"]
    print(f"Противник -- {enemi["Name"]}: {enemi["WORDS"]}")
    input('Нажмите |Enter| чтобы продолжить')
    print()
    while player["HP"] > 0 and enemy_hp > 0:
        if rounds % 2 == 1:
            if player["healing potion"] > 0:
                    atka_defend = input("защищатся , атакавать , использовать зелье:  ")
                    if atka_defend == "атакавать":
                        crit = randint(1, 100)  
                        instant_kill = randint(1, 100)

                        if player["instant_murder"] >= instant_kill:
                            print(f'{player["Name"]} атакует {enemi["Name"]}.')
                            print("Ты разрубаешь противника надвое")
                            enemy_hp -= player["DMG"] * 666

                        if crit < player["Laki"]:
                            print(f'{player["Name"]} атакует {enemi["Name"]}.')
                            print("Вы попадаете по слабому месту врага")
                            enemy_hp -= player["DMG"] * 3

                        else:
                            print(f'{player["Name"]} атакует {enemi["Name"]}.')
                            enemy_hp -= player["DMG"]
                    
                    if atka_defend == "защищатся":
                        uvarot = randint(1, 100)
                        if uvarot < player['Stamina']:
                            print(f"{enemi["Name"]} атакует {player["Name"]}")
                            print("Вы увернулись от атаки")
                            player["HP"] -= (enemi["DMG"] * 0)

                        else:
                            print(f"{enemi["Name"]} атакует {player["Name"]}")
                            enemy_hp -= (player["DMG"] / 2)
                            player["HP"] -= (enemi["DMG"] * player["Armor"]) * player["Armor"]

                    if atka_defend == "использовать зелье":
                            player["HP"] += 30
                            player["healing potion"] -= 1
                            print(f"""Ты випил зелье и исцелился 
                                Твоё здоровье равняется {player["HP"]}""")
            else:
                if player["healing potion"] <= 0:
                        atka_defend = input("защищатся , атакавать:  ")
                        if atka_defend == "атакавать":
                            crit = randint(1, 100)  
                            instant_kill = randint(1, 100)
                            if player["instant_murder"] >= instant_kill:
                                print(f'{player["Name"]} атакует {enemi["Name"]}.')
                                print("Ты разрубаешь противника надвое")
                                enemy_hp -= player["DMG"] * 666

                            if crit < player["Laki"]:
                                print(f'{player["Name"]} атакует {enemi["Name"]}.')
                                print("Вы попадаете по слабому месту врага")
                                enemy_hp -= player["DMG"] * 3
                            else:
                                print(f'{player["Name"]} атакует {enemi["Name"]}.')
                                enemy_hp -= player["DMG"]
                        
                        if atka_defend == "защищатся":
                            uvarot = randint(1, 100)
                            if uvarot < player['Stamina']:
                                print(f"{enemi["Name"]} атакует {player["Name"]}")
                                print("Вы увернулись от атаки")
                                player["HP"] -= (enemi["DMG"] * 0)
                            else:
                                print(f"{enemi["Name"]} атакует {player["Name"]}")
                                enemy_hp -= (player["DMG"] / 2)
                                player["HP"] -= (enemi["DMG"] * player["Armor"]) * player["Armor"]



            sleep(1)
        else:
            
            print(f"{enemi["Name"]} атакует {player["Name"]}")
            player["HP"] -= enemi["DMG"] * player["Armor"]
            sleep(1)
        print(f'''{player['Name']}: {player['HP']}
            {enemi['Name']}: {enemy_hp}''')
        print()
        sleep(1)
        rounds += 1
    if player["HP"] > 0 and enemy_hp <= 0:
            print(f'Противник - {enemi["Name"]}: {enemi["WIN"]}')
            player['Inventory'].append(enemi["LOOT"]["Name"])
            player["win"] += 1

    else:
        print(f'Противник - {enemi["Name"]}: {enemi["LOSS"]}')
    if player['HP'] <= 0:
     player['HP'] = 100
    print()
     
    return current_enemy
def wibor_fight():
        wibor = int(input("""Какое задание возмёшь?
                     1
                     2
                     3
                     4
                     5
                     6  """))
        if wibor == 1:
            current_enemy = "ENEMI_1"
        elif wibor == 2:
            current_enemy = "ENEMI_2"  
        elif wibor == 3:
            current_enemy = "ENEMI_3"
        elif wibor == 4:
            current_enemy = "ENEMI_4"
        elif wibor == 5:
            current_enemy = "ENEMI_5"
        elif wibor == 6:
            current_enemy = "ENEMI_6"
        current_enemy = fight(current_enemy)
        sleep(1)
def bulletin_board():
    print(f"1  Заказ на очистку сточных труб от тлизней - {enemies["ENEMI_1"]["Name"]}")
    print(f"2  Заказ на убийства гиблинов в северном лесу - {enemies["ENEMI_2"]["Name"]}")
    print(f"3  Заказ на зачистку подземелья оргов - {enemies["ENEMI_3"]["Name"]}")
    print(f"4  Заказ на разветку глубоких пищер Винтерхоума - {enemies["ENEMI_4"]["Name"]}")
    print(f"5  Заказ на сбор грибов - {enemies["ENEMI_5"]["Name"]}")
    print(f"6  Расчистка завала на дороге в город - {enemies["ENEMI_6"]["Name"]}")
    print("")
    sleep(1)




def rest():
    hpi = player["HP"]
    print("ты идёш заказывать комнату в гильдии")
    if hpi < 100:
        otduh = input("""Хочешь отдахнуть?
             (да\нет)""")
        sleep(1)
        if otduh == "да":
            print("Ты идёш в таверну заказываешь комнату и поднимаешся в свою комнату")
            sleep(1)
            print("Ложишься в кровать и моментально засыпаешь")
            sleep(1)
            print("Z...")
            sleep(0.7)
            print("Zz...")
            sleep(0.7)
            print("Zzz...")
            sleep(0.7)
            print("Zzzz...")
            player["HP"] = 100
        else:
            print("")

def treining():
    actions_3 = int(input('''Сколько будишь тренироваться
                             1 -- 1 час (100 уэнав)
                             2 -- 5 часов (150 утэнав)
                             3 -- 10 часов (350 утенав)
                             4 -- 30 часов (500 утенав)'''))
    sleep(1)
    if actions_3 == 1:
        if player["Money"] >= 400:
            player["Money"] -= 400
            player["Stamina"] += 5
            print("Вы начали тренироваться")
            sleep(1)
            print("Вы тренировались 1 час")
            sleep(1)
            print("Ваша выносливость выросла на 5")
    if actions_3 == 2:
        if player["Money"] >= 700:
            player["Money"] -= 700
            player["Stamina"] += 10
            print("Вы начали тренироваться")
            sleep(1)
            print("Вы тренировались 5 час")
            sleep(1)
            print("Ваша выносливость выросла на 10")
    if actions_3 == 3:
        if player["Money"] >= 1100:
            player["Money"] -= 1100
            player["Stamina"] += 15
            print("Вы начали тренироваться")
            sleep(1)
            print("Вы долго тренировались 10 час")
            sleep(1)
            print("Ваша выносливость выросла на 15")
            sleep(1)
    if actions_3 == 4:
        if player["Money"] >= 1400:
            player["Money"] -= 1400
            player["Stamina"] += 20
            print("Вы начали тренироваться")
            sleep(2)
            print("Вы в поте лица тренировались 30 час")
            sleep(1)
            print("Ваша выносливость выросла на 20")
            sleep(1)
def encyclopedia():
    print("это инцеклопедия всего и вся")
    vesi = int(input("""Выберете главу
                     1 -- монстры
                     2 -- придметы
                     3 -- мечи
                     4 -- доспехи
                                         """))
    if vesi == 1:
        vesi2 = int(input("""Про кого хотите узнать
                          1 -- Тлизень
                          2 -- Гиблин
                          3 -- Орг
                          4 -- Триоль
                          5 -- Странный человек
                          """))
        if vesi2 == 1:
            print(f"{enemies["ENEMI_1"]["Name"]}:")
            print(f"{enemies["ENEMI_1"]["DESCRIPTION"]}")
            print(f"Здоровье -- {enemies["ENEMI_1"]["HP"]}")
            print(f"Урон -- {enemies["ENEMI_1"]["DMG"]}")
            sleep(1)
        elif vesi2 == 2:
            print(f"{enemies["ENEMI_2"]["Name"]}:")
            print(f"{enemies["ENEMI_2"]["DESCRIPTION"]}")
            print(f"Здоровье -- {enemies["ENEMI_2"]["HP"]}")
            print(f"Урон -- {enemies["ENEMI_2"]["DMG"]}")
            sleep(1)
        elif vesi2 == 3:
            print(f"{enemies["ENEMI_3"]["Name"]}:")
            print(f"{enemies["ENEMI_3"]["DESCRIPTION"]}")
            print(f"Здоровье -- {enemies["ENEMI_3"]["HP"]}")
            print(f"Урон -- {enemies["ENEMI_3"]["DMG"]}")
            sleep(1)
        elif vesi2 == 4:
            print(f"{enemies["ENEMI_4"]["Name"]}:")
            print(f"{enemies["ENEMI_4"]["DESCRIPTION"]}")
            print(f"Здоровье -- {enemies["ENEMI_4"]["HP"]}")
            print(f"Урон -- {enemies["ENEMI_4"]["DMG"]}")
            sleep(1)
        elif vesi2 == 5:
            print(f"{enemies["ENEMI_5"]["Name"]}:")
            print(f"{enemies["ENEMI_5"]["DESCRIPTION"]}")
            print(f"Здоровье -- {enemies["ENEMI_5"]["HP"]}")
            print(f"Урон -- {enemies["ENEMI_5"]["DMG"]}")
            sleep(1)

    if vesi == 2:
        vesi2 = int(input("""Про кого хотите узнать
                          1 -- гель тлизня (Тлизень)
                          2 -- Ухо гиблина (Гиблин)
                          3 -- Мясо орга (Орг)
                          4 -- Зуб триоля (Триоль)
                          5 -- Страный гриб (Странный человек)
                          """))
        if vesi2 == 1:
            print(f"{items["item1"]["Name"]}:")
            print(f"{items["item1"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 2:
            print(f"{items["item2"]["Name"]}:")
            print(f"{items["item2"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 3:
            print(f"{items["item3"]["Name"]}:")
            print(f"{items["item3"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 4:
            print(f"{items["item4"]["Name"]}:")
            print(f"{items["item4"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 5:
            print(f"{items["item5"]["Name"]}:")
            print(f"{items["item5"]["DESCRIPTION"]}")
            sleep(1)

    if vesi == 3:
        vesi2 = int(input("""Про какой мечь хотите узнать
                            1 -- Деревяный меч
                            2 -- Бронзавый меч
                            3 -- Железный меч
                            4 -- Стальной меч
                            5 -- Меч путешественника
                            6 -- Мифриловый меч
                            7 -- Адамантивый меч
                            8 -- Цепной меч
                            """))
        if vesi2 == 1:
            print(f"{swords["swords_1"]["Name"]}:")
            print(f"{swords["swords_1"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 2:
            print(f"{swords["swords_2"]["Name"]}:")
            print(f"{swords["swords_2"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 3:
            print(f"{swords["swords_3"]["Name"]}:")
            print(f"{swords["swords_3"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 4:
            print(f"{swords["swords_4"]["Name"]}:")
            print(f"{swords["swords_4"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 5:
            print(f"{swords["swords_5"]["Name"]}:")
            print(f"{swords["swords_5"]["DESCRIPTION"]}")
        elif vesi2 == 6:
            print(f"{swords["swords_6"]["Name"]}:")
            print(f"{swords["swords_6"]["DESCRIPTION"]}")
        elif vesi2 == 7:
            print(f"{swords["swords_7"]["Name"]}:")
            print(f"{swords["swords_7"]["DESCRIPTION"]}")
        elif vesi2 == 8:
            print(f"{swords["swords_8"]["Name"]}:")
            print(f"{swords["swords_8"]["DESCRIPTION"]}")
        
    if vesi == 4:
        vesi2 = int(input("""1 -- Кожаные латы 
        2 -- Кожаные латы с железными вставками 
        3 -- Кольчуга 
        4 -- Стальная кольчуга 
        5 -- Доспехи путешественника 
        6 -- Мифриловая кольчуга 
        7 -- Адамантивая кольчуга
        8 -- C#$2%ой @#с&^х                  
                          """))
        if vesi2 == 1:
            print(f"{Armori["Armor_1"]["Name"]}:")
            print(f"{Armori["Armor_1"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 2:
            print(f"{Armori["Armor_2"]["Name"]}:")
            print(f"{Armori["Armor_2"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 3:
            print(f"{Armori["Armor_3"]["Name"]}:")
            print(f"{Armori["Armor_3"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 4:
            print(f"{Armori["Armor_4"]["Name"]}:")
            print(f"{Armori["Armor_4"]["DESCRIPTION"]}")
            sleep(1)
        elif vesi2 == 5:
            print(f"{Armori["Armor_5"]["Name"]}:")
            print(f"{Armori["Armor_5"]["DESCRIPTION"]}")
        elif vesi2 == 6:
            print(f"{Armori["Armor_6"]["Name"]}:")
            print(f"{Armori["Armor_6"]["DESCRIPTION"]}")
        elif vesi2 == 7:
            print(f"{Armori["swords_7"]["Name"]}:")
            print(f"{Armori["swords_7"]["DESCRIPTION"]}")
        elif vesi2 == 8:
            print(f"{Armori["Armor_8"]["Name"]}:")
            print(f"{Armori["Armor_8"]["DESCRIPTION"]}")


def buyer():
    sell = input("""Ну что голубчик готов чтонибудь продать?  да/нет
            """)
    if sell == "да":
        sell_oll = int(input("""Что ты хочешь продать?
                    1 -- гель тлизня
                    2 -- ухо гиблина
                    3 -- мясо орга
                    4 -- Зуб триоля
                    5 --Страный гриб
                    """))
        if sell_oll == 1:
            if items["item1"]["Name"] in player["Inventory"]:
                sell_yes = input(f"хочешь продать {items["item1"]["Name"]}?")
                if sell_yes == "да":
                    print("Тогда вот ваши утены")
                    player["Money"] += items["item1"]["Prise"]
                    player["Inventory"].remove(items["item1"]["Name"])
                else:
                    print("Тогда проваливай и не задерживай очередь")
                sleep(1)
            else:
                print("У тебя нет этого предмета")

        if sell_oll == 2:
            if items["item2"]["Name"] in player["Inventory"]:
                sell_yes = input(f"хочешь продать {items["item2"]["Name"]}?")
                if sell_yes == "да":
                    print("Тогда вот ваши утены")
                    player["Money"] += items["item2"]["Prise"]
                    player["Inventory"].remove(items["item2"]["Name"])
                else:
                    print("Тогда проваливай и не задерживай очередь")
                sleep(1)
            else:
                print("У тебя нет этого предмета")

        if sell_oll == 3:
            if items["item3"]["Name"] in player["Inventory"]:
                sell_yes = input(f"хочешь продать {items["item3"]["Name"]}?")
                if sell_yes == "да":
                    print("Тогда вот ваши утены")
                    player["Money"] += items["item3"]["Prise"]
                    player["Inventory"].remove(items["item3"]["Name"])
                else:
                    print("Тогда проваливай и не задерживай очередь")
                sleep(1)
            else:
                print("У тебя нет этого предмета")

        if sell_oll == 4:
            if items["item4"]["Name"] in player["Inventory"]:
                sell_yes = input(f"хочешь продать {"item4"["Name"]}?")
                if sell_yes == "да":
                    print("Тогда вот ваши утены")
                    player["Money"] += items["item4"]["Prise"]
                    player["Inventory"].remove(items["item4"]["Name"])
                else:
                    print("Тогда проваливай и не задерживай очередь")
                sleep(1)
            else:
                print("У тебя нет этого предмета")

        if sell_oll == 5:
            if items["item5"]["Name"] in player["Inventory"]:
                sell_yes = input(f"хочешь продать {items["item5"]["Name"]}?")
                if sell_yes == "да":
                    print("Тогда вот ваши утены")
                    player["Money"] += items["item5"]["Prise"]
                    player["Inventory"].remove(items["item5"]["Name"])
                else:
                    print("Тогда проваливай и не задерживай очередь")
                sleep(1)
            else:
                print("У тебя нет этого предмета")
        else:
            print("")

    else:
        print("")
def shop():
    shoper = input("""Привет хочешь купить зелья или что-то ещё?    
                   (да\нет)
                   """)
    if shoper == "да":
        sleep(1)
        shop_bey = int(input("""Ну тогда вот весь мой асортимент
                      1 -- Зелье личения 500 утенов
                      2 -- Зелья четырёх листного клевера (удачи) 1000 утенов
                      
                      
                      """))
        sleep(1)
        if shop_bey == 0:
           print("Ну раз не можешь определится то проваливай")
        elif shop_bey == 1:
            if player["Money"] >= 500:
                player["Money"] -= 500
                player["healing potion"] += 1
                sleep(1)
                print("Теперь в вашем инвенторе есть зелье личения")
            else:
                print("Тебе не хватает денег на зелье личения")

        elif shop_bey == 2:
            if player["Money"] >= 1000:
                if "Зелья четырёх листного клевера" in player['Inventory']:
                    print("Я НЕ ПРОДАМ ТЕБЕ БОЛЕЕ 1 ФЛАКОНА ЭТОГО ЗЕЛЬЯ!!!")
                player["Money"] -= 1000
                player['Inventory'].append("Зелья четырёх листного клевера")
                sleep(1)
                print("Теперь в вашем инвенторе есть зелья четырёх листного клевера")
            else:
                print("Тебе не хватает денег на зелья четырёх листного клевера")

        else:
            print("")

    else:
        print("")

        




def cosmadisantnik():
    print("Кто ты путник,")
    sleep(1)
    print("Хотя не важно, важно то что веришь ли ты в великого Бога Императара")
    yes_no = input("""да/нет
                   """)
    if yes_no == "да":

        if player["win"] >= 7:
              sword_armor = int(input("""Я могбы помоч и дать тебе оружие или браню которово ты точно дастоен
                               1 -- оружие   <--------(желательно начать с этого)
                               2 -- броня
                               """))
              if sword_armor == 1:
                if player["cosmadisantni"] <= 0:
                        print("""Вижу ты закалёный в боях воин""") 
                            
                        sleep(1)
                        print("Хочешь узнать мою историю? или предпочёшь взять это оружие и ринуться в бой")
                        yes_no2 = input("""да/зачем мне это?
                                        """)
                        if yes_no2 == "да":
                            print("""Вы слушаете очень долгую и интересную историю про войны в других мерах,
                            против все поглощающих ульев больших жуков именуемых Тераниды,
                            и железных армий называющихся Некроны   """)
                            sleep(1)
                            print("""После он рассказывает как очутился здесь,
                                    оказывается при одном из варп прыжков координаты точки назначения сбились и их корабль вылетели прямо в эту планету после чего разбился,
                                    выжл только он""")
                            sleep(1)
                            print(f"Ну ладно я отдам свой меч но за небольшую плату в {swords["swords_8"]["PRICE"]}")
                            player["cosmadisantni"] += 1
                            soglas =input("""Согласен? 
                                        (да\нет)
                                        """)
                            if soglas == "да":
                                if player["Money"] >= swords["swords_8"]["PRICE"]:
                                    player["Money"] -= swords["swords_8"]["PRICE"]
                                    player['Inventory'].append(swords["swords_8"]["Name"])
                                    player["DMG"] += swords["swords_8"]["DMG"]
                                    player["instant_murder"] += swords["swords_8"]["instant_murder"]
                                    
                                    sleep(1)
                                    print(f"Теперь ваш урон равен {player["DMG"]}")
                                else:
                                    print("Ну тогда иди и добуть эту сумму путник!") 


                else:
                        print("Ты вернулся и готов принять мой дар?")
                        soglas =input("""Согласен? 
                                        (да\нет)
                                        """)
                        if soglas == "да":
                                if player["Money"] >= swords["swords_8"]["PRICE"]:
                                    player["Money"] -= swords["swords_8"]["PRICE"]
                                    player['Inventory'].append(swords["swords_8"]["Name"])
                                    player["DMG"] += swords["swords_8"]["DMG"]
                                    player["instant_murder"] += swords["swords_8"]["instant_murder"]
                                    
                                    sleep(1)
                                    print(f"Теперь ваш урон равен {player["DMG"]}")
                                else:
                                    print("Ну тогда иди и добуть эту сумму путник!") 


              if sword_armor == 2:
                    if player["cosmadisantni_2"]  <= 0:
                        print("Я рад снова увидеть тебя путник.")
                        sleep(1)
                        print("""Оу я вижу что мой меч неподходит тебе по размеру но с этим поможет моя броня,
                            она усилит тебя и поможет справится с врагами""")
                        player["cosmadisantni_2"] += 1
                        vivibor = input("""НО я отдам её за небольшую симвалическую плату в 2000 утенов
                                        (да\нет)
                                        """)
                        if vivibor == "да":
                            if player["Money"] >= 2000:
                                print("Ну тогда вот держи, прям от сердца")
                                player["Money"] -= 2000
                                player["Armor"] -= 0.50
                                player["Stamina"] += 20
                                player["Inventory"].append("Силовой доспех")
                            else:
                                print("Прости но тебе не хватает денег")
                        
                        else:
                            print("Ну тогда удачи, заходи если передумаешь ")

                    else:
                        print("Я рад снова увидеть тебя путник.")
                        sleep(1)
                        print("Ну что передумал?")
                        sleep(1)
                        vivibor = input("Всётаки решил купит и заработал да?")
                        if vivibor == "да":
                            if player["Money"] >= 2000:
                                print("Ну тогда вот держи, прям от сердца")
                                player["Money"] -= 2000
                                player["Armor"] -= 0.50
                                player["Stamina"] += 20
                                player["Inventory"].append("Силовой доспех")
                            else:
                                print("Прости но тебе не хватает денег")
              else:
                  print("Я не могу продать тебе чтото другое")
        else:
                print(f"""Ты ещё не достоин иди и победи своих врагов
            
                  нужно победить ещё: {7 - player["win"]} врагов""")
    else:
        print("Тогда не буду тебя задерживать")
        sleep(0.5)