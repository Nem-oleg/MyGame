player = { 
    "Name": 'fgh',
    "HP": 90,
    "DMG": 10,
    "Money": 1000,
    "Inventory": [],
    "Stamina": 10,
    "Armor": 0.95,
    "Laki": 10,
    "win": 0,
    "healing potion": 1,
    "instant_murder": 10,
    "cosmadisantni": 0,
    "cosmadisantni_2": 0
}


items ={

"item1" : 
{
    "Name":"гель тлизня",
    "Prise":300,
    "DESCRIPTION":"Почти прозрачная голубовато-зелёная жидкасть не имеющая запаза, чуть сладкая на вкус. Используется в касметологии за счёт силы омалаживать кожу"
},

"item2" : 
{
    "Name":"Ухо гиблина",
    "Prise":500,
    "DESCRIPTION":"Можно сдать в гиль дию или продать алхимикам ( Алхимики используют уши гиблинов для алхимических экспереметов так как в ушах гиблинов бальшая канцентрация маны )"
},

"item3" : 
{
    "Name":"Мясо орга",
    "Prise":650,
    "DESCRIPTION":"Мясо орга ценится их вкусом и текстурой ( даже жареное мясо орга на кастре, очень нежное )"
},

"item4" : 
{
    "Name":"Зуб триоля",
    "Prise":1000,
    "DESCRIPTION":"Зубы триоля часто используется в производстве инструментав ( зубы триоля более крепкий и надёжный материал чем сталь )"
},

"item5" : 
{
    "Name":"Страный гриб",
    "Prise":1500,
    "DESCRIPTION":"Навид ОЧЕНЬ страный гриб. Мажно продоть алхимику ( Гриб который вызывает сидьнейшие галюцинации, используется в медицине как абезболивательное и успокаительное)"
},

"item6" : 
{
    "Name":"камень с развалин чегото",
    "Prise":100000,
    "DESCRIPTION":"на самом деле обычный камень"
},
}



enemies = {
"ENEMI_1" : 
{
    "Name":"Тлизинь",
    "HP":50,
    "DMG":10,
    "WORDS":"блёблёб",
    "WIN":"Тлизинь привращается в лужу геля",
    "LOSS":"Тлизинь уже был готов поглотить вас но тут он отвликается на упавшую шишку",
    "LOOT": items["item1"],
    "DESCRIPTION": """Выглядит как полупрозрачная желеобразная капля.
    Физические атаки проходят лишь по так называемому ядру твёрдому образованию внутри его тела. 
    Вся органика поглащёная Тлизью начинает постеренно растворятся"""
 },

"ENEMI_2" : 
{
    "Name":"Гиблин",
    "HP":70,
    "DMG":15,
    "WORDS":"СВЕЖЕЕ МЯЯЯЯЯСОО!!!!!!!",
    "WIN":"НЕЕЕЕЕЕТ ПОЩАДИ",
    "LOSS":"На Гиблина падает шишка и вам удаётся сбижать",
    "LOOT": items["item2"],
    "DESCRIPTION": """Выглядит как не дорослый человек имеющий зелёнаватый оттенок кожи.
    Гиблин евляется одним из самых слабых человекообразных монстров,
    имеющих средний рост в 145см.
    Владеют знаниями в создания каменых инструментах и развидения огня.
    Представляют опасность лишь в группе"""
},

"ENEMI_3" : 
{
    "Name":"Орг",
    "HP":150,
    "DMG":20,
    "WORDS":"ШИСАТ ТАР РАТ ХАК ",
    "WIN":"Орг падает замертво не проранив ни слова",
    "LOSS":"Орг отвлекается на звук упавшей шишки и ты тихо сбегаешь",
    "LOOT": items["item3"],
    "DESCRIPTION": """Высокий кобанообразный двуногий почти прямоходящий монстр  имеющий толстый шерстиной покровю
    примерный средний рост ровняется 350см.
    Из-за рациона Орга их мясо становится нежным и сочным и даже евляется дилекотесом.
    Тагже как и гиблины имеют познание в создание каменых инструментов.
    Евляется средним по опасности протимвником""",
},

"ENEMI_4" : 
{
    "Name":"Триоль",
    "HP":300,
    "DMG":50,
    "WORDS":"ТЫ кто такой? Я вас не звать. Иди ты лесом!",
    "WIN":"АААААААА ПОМОГИТЕЕЕ",
    "LOSS":"Триоль отвлекается на спасительную шишку и тебет удаётся сбежать",
    "LOOT": items["item4"],
    "DESCRIPTION": """Высокий человекообразный монстр имеющий толстый шерстеной покров
    на центральной голве возвышается мощьный рог,
    имеют средний рост в 530см
    Триоли хорошо приспособлены к проживании в северных горах Винтерхоум.
    Евляется опасным и не предсказуемым врагом изза трёх головы имеющии самоосознание"""
},

"ENEMI_5" : 
{
    "Name":"Странный человек",
    "HP":200,
    "DMG":100,
    "WORDS":"ЭЭЭЭ ОТОЙДИ ЭТО МОЙ ГРИБ!!!! ЭТО МОЙ ГРИБ!! НЕ ВИДИШЬ Я ЕГО ЕМ!!",
    "WIN":"ЭТО МОЙ ГРИБ ВИДИШЬ ОН НАДКУСАН",
    "LOSS":"ЛААДНО ОН ТВОЙ",
    "LOOT": items["item5"],
    "DESCRIPTION":"""Этот старик недавно поевился около этого города и сильно пугает всех лесников из-за его вида
    корый НЕВОЗМОЖНО описать или запомнить.
    Этот человек предположительно евляется хозяином лесом
    так что просим НАСТОЯТЕЛЬНО не влезать с ним в конфликт и вести себя уважительн."""
},

"ENEMI_6" : 
{
    "Name":"!!!!!!КАМЕНЬ!!!!!!!",
    "HP":666,
    "DMG":10,
    "WORDS":".-.-  -.- .- -- . -. -..-  ..  .-.-  -. .  ..- .--- -.. ..- -.-.-- -.-.-- -.-.--",
    "WIN":"Ты разгребаешь завал вместе с другими путишествениками",
    "LOSS":"На тебя падает камень и ты теряешь сознание",
    "LOOT": items["item6"]
}
}



swords = {

 "swords_1" :
 {
    "Name": "Деревяный меч",
    "DMG" : 5,
    "PRICE": 1000,
    "DESCRIPTION":"""Очень искустно сделаный деревяный мечь.
    Немного повысит шансы победы над врагом
    """
 },

 "swords_2" :
 {
    "Name": "Бронзавый меч",
    "DMG" : 10,
    "PRICE": 1500,
    "DESCRIPTION":"""Меч сделаный из сплава алюминия и меди.
    Искустно заточен и закалён
    """
 },

 "swords_3" :
 {
    "Name": "Железный меч",
    "DMG" : 15,
    "PRICE": 2000,
    "DESCRIPTION":"""Обычный железный меч
    """
 },

 "swords_4" :
 {
    "Name": "Стальной меч",
    "DMG" : 20,
    "PRICE": 2500,
    "DESCRIPTION":"""Очень надёжный стальной меч
    """
 },

 "swords_5" :
 {
    "Name": "Меч путешественника",
    "DMG" : 25,
    "Stamina": 20,
    "PRICE": 1000,
    "DESCRIPTION":"""Страный меч из не известного материала и причудривой формы.
    Как говорят некоторые из владельцев, при использования этого меча ты чуствуешь необычайный прилив сил,
    сним чуствуется что ты можешь пабедить даже дракона, в общем клинок воодушевляет владельца на приключения, но
    постепено все владельцы начинали чуствовать что он предназначен не для них а для когото более важного
    """
 },

 "swords_6" :
 {
    "Name": "Мифриловый меч",
    "DMG" : 35,
    "PRICE": 5000,
    "DESCRIPTION":"""Меч сделаный из одного из самых редких материалов.
    Очень лёгкий и в тоже время прочный меч, выкованый хорошим мастером
    """
 },

 "swords_7" :
 {
    "Name": "Адамантивый меч",
    "DMG" : 40,
    "PRICE": 7000,
    "DESCRIPTION":"""Меч сделаный из самого реткого и трудно добываемого материала Адамантия
    Адамантия руда добываемая на такой глубине на которо ты начинаешь слышать крики грешьников из самого ада
    """
 },

 "swords_8" :
 {
    "Name": "Цепной меч",
    "DMG" : 80,
    "instant_murder": 35,
    "PRICE": 10000,
    "WIN": 10,
    "DESCRIPTION":"""Меч по виду очень тихнологичный для нашего мира 
    Это оружие представляет собой меч с двыжущемеся зубьями, 
    благодоря которым при попадание по врагу и нажатие кнопки (курка) 
    этот меч просто распиливает своего противника надвое не довая и шанса противнику выжить.
    Для его использования требуется необычайное мастерство и сила изза его размеров,
    тагже держать его можно толь двумя руками
    """
 },

}



Armori = {

"Armor_1":
{

    "Name": "Кожаные латы",
    "Armor": "5 защиты",
    "DESCRIPTION": "Обычные кожаные доспехи сделаные из хорошей кожи ",
    
},

"Armor_2":
{

    "Name": "Кожаные латы с железными вставками",
    "Armor": "10 защиты",
    "DESCRIPTION": "Обычные кожаные доспехи с вставками из железа которые закрывают руки ноги и грудь ",
    
},

"Armor_3":
{

    "Name": "Кольчуга",
    "Armor": "15 защиты",
    "DESCRIPTION": "Броня сделаная из множества железных колец благодоря этому не сковывает движения",
    
},

"Armor_4":
{

    "Name": "Стальная кольчуга",
    "Armor": "20 защиты",
    "DESCRIPTION": """Броня сделаная из множества стальных колец благодоря этому не сковывает движения.
    Стальная кольчуга более надёжная и лёгкая чем железная кольчуга""",
    
},

"Armor_5":
{

    "Name": "Доспехи путешественника",
    "Armor": "25 защиты",
    "DESCRIPTION": """Доспехи путешественника похожи на кожаные латы с железными вставками
    метал из которого сделаны вставки не похож на любой другой известный метал,
    он поглащает инерцию и помогает быстрей перемещатся в пространстве.
    На этом матереке находятся примерно 30 таких даспехов 
    а кожа неизвестного зверя находящаяся между листов метала не подвергается какой-либо карозии""",
    
},

"Armor_6":
{

    "Name": "Мифриловая кольчуга",
    "Armor": "30 защиты",
    "DESCRIPTION": """Кольчуга сделаная из множества мифриловыхчушуек и колец, 
    благодаря этому кольчуга не сковывает движения
    Сделаная из мефрила кольчуга имеет невероятную лёгкость и надёжность""",
    
},

"Armor_7":
{

    "Name": "Адамантивая кольчуга",
    "Armor": "35 защиты",
    "DESCRIPTION": """Адамантивая кольчуга дополненая цельными листами адамантия имеет хорошую защиту от огня и холода
    она очень надёжная и крепкая""",
    
},

"Armor_8":
{

    "Name": "Силовой доспех",
    "Armor": "50 защиты",
    "Stamina":"20 выносливости",
    "DESCRIPTION": """ОЧЕНЬ тихнологичный доспех оснащёный системой жизнеобеспечения
    климот контролем и системой фильтрации воздуха.
    Силовой доспех сильно повышает физические возможности человека находящевося внутри доспехов.
    На материке было зарегестрированы только 3 таких доспехов""",
    
},


}