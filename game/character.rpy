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
define sm = Character(kind=s, color="#595B5B", what_prefix='(', what_suffix=')', what_italic=True, namebox_background="gui/mind_namebox.png") #мысли Эммы


image sam face neitral:
    # "sam/neitral/sam neitral.png"  with dissolve
    # pause 1.5
    # "sam/neitral/sam neitral et.png"  with dissolve
    # pause 0.5
    # "sam/neitral/sam neitral bl2.png"  with dissolve
    # pause 0.2
    "sam/neitral/sam neitral.png"  with dissolve
    pause 0.5
    "sam/neitral/sam neitral el.png" with dissolve
    pause 1.5
    "sam/neitral/sam neitral.png"  with dissolve
    pause 0.5  
    "sam/neitral/sam neitral er.png"  with dissolve
    pause 1.5 
    "sam/neitral/sam neitral.png"  with dissolve
    choice:
        pause 1.0 
    choice:
        pause 2.5 
    choice:
        pause 5.0 
    "sam/neitral/sam neitral bl.png"  with dissolve
    pause 0.4
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

define d = Character('Отец', color="#dfad14", callback=name_callback, cb_name="dad")
image dad a_n = At('dad n', sprite_highlight('dad'))