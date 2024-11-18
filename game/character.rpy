init python:
    # Список общих состояний
    states = [
        # "h", # = счастливые состояния
        "n",  # нейтральные состояния
        # "s",  # грустная
        # "sr",  # серьезные состояния
        # "che", "o", "xm"  # различные выражения чё, эм, О!, хм
    ]

    # Функция для создания изображений, необходима чтобы работал плагин для выделения говорящего персонажа
    def create_character_images(character, states):
        for state in states:
            renpy.image(f"{character} a_{state}", At(f"{character} {state}", sprite_highlight(character)))



################################################################################
# Персонажи
################################################################################

# для слов автора
define n = Character(callback=name_callback, cb_name=None)

################################################################################
# Сэм
################################################################################
init python:
    create_character_images("sam", states) #общие состояния
    
define s = Character('Сэм', color="#dbbf81", image="sam", callback=name_callback, cb_name="sam")

#мысли Сэма
define sm = Character(kind=s, color="#cac6b7", what_prefix='(', what_suffix=')', what_italic=True, namebox_background=Frame("gui/mind_namebox.png", Borders(100, 15, 100, 15)))


image sam face neitral:
    # "sam/neitral/sam neitral.png"  with dissolve
    # pause 1.5
    # "sam/neitral/sam neitral et.png"  with dissolve
    # pause 0.5
    # "sam/neitral/sam neitral bl2.png"  with dissolve
    # pause 0.2
    "sam/neitral/sam neitral.png"  with dissolve
    pause 1.5
    "sam/neitral/sam neitral el.png" with dissolve
    pause 1.0
    "sam/neitral/sam neitral.png"  with dissolve
    pause 0.5  
    "sam/neitral/sam neitral er.png"  with dissolve
    pause 1.0 
    "sam/neitral/sam neitral.png"  with dissolve
    choice:
        pause 1.0 
    choice:
        pause 2.0 
    choice:
        pause 3.0 
    "sam/neitral/sam neitral bl.png"  with dissolve
    pause 0.3
    repeat


# сборка слоев - тела, прически и лица
layeredimage sam:

    always:
        "sam body"

    group body:
        attribute b default:
            "sam body"

    group emotion:
        # attribute h:
        #     "sam face happy"
        attribute n:
            "sam face neitral"
        # attribute s:
        #     "sam face sad"
        # attribute sr:
        #     "sam face seriously"


################################################################################
# Отец
################################################################################

define d = Character('Отец', color="#e1d2b8", callback=name_callback, cb_name="dad", namebox_background=Frame("gui/sec_namebox.png", Borders(100, 15, 100, 15)))
image dad a_n = At('dad n', sprite_highlight('dad'))


################################################################################
# Директор школы
################################################################################
default ds_name = "Незнакомец"
define ds = Character("[ds_name]", color="#e1d2b8", callback=name_callback, cb_name="ds", namebox_background=Frame("gui/sec_namebox.png", Borders(100, 15, 100, 15)))
image ds a_n = At('ds n', sprite_highlight('ds'))

#Сын президента
################################################################################

define ps = Character('Сын президента', color="#e1d2b8", callback=name_callback, cb_name="president_son", namebox_background=Frame("gui/sec_namebox.png", Borders(100, 15, 100, 15)))
image president_son a_n = At('president_son n', sprite_highlight('president_son'))




### Второстепенные 

################################################################################
# Практикантка
################################################################################

define trainee = Character('Практикантка', color="#e1d2b8", callback=name_callback, cb_name="trainee")
image trainee a_n = At('trainee n', sprite_highlight('trainee'))


################################################################################
# Учитель   
################################################################################

define teacher = Character('Учитель', color="#e1d2b8", callback=name_callback, cb_name="teacher")
image teacher a_n = At('teacher n', sprite_highlight('teacher'))  


################################################################################
# Ученица школы 1
################################################################################

define schoolgirl1 = Character('Ученица школы 1', color="#e1d2b8", callback=name_callback, cb_name="schoolgirl1")
image schoolgirl1 a_n = At('schoolgirl1 n', sprite_highlight('schoolgirl1'))


#   Ученица школы 2
################################################################################

define schoolgirl2 = Character('Ученица школы 2', color="#e1d2b8", callback=name_callback, cb_name="schoolgirl2")
image schoolgirl2 a_n = At('schoolgirl2 n', sprite_highlight('schoolgirl2'))

# Ученик 1
################################################################################

define student1 = Character('Ученик', color="#e1d2b8", callback=name_callback, cb_name="student1")
image student1 a_n = At('student1 n', sprite_highlight('student1'))


