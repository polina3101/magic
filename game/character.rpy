init python:
    # Список общих состояний
    states = [
        # "h", # = счастливые состояния
        "n",  # нейтральные состояния
        # "s",  # грустная
        "sr",  # серьезные состояния,
        "magic"
    ]

    # Функция для создания изображений, необходима чтобы работал плагин для выделения говорящего персонажа
    def create_character_images(character, states):
        for state in states:
            renpy.image(f"{character} a_{state}", At(f"{character} {state}", sprite_highlight(character)))
            renpy.image(f"{character} sch a_{state}", At(f"{character} sch {state}", sprite_highlight(character)))



################################################################################
# Персонажи
################################################################################

# для слов автора
define n = Character(callback=name_callback, cb_name=None)

################################################################################
# Сэм
################################################################################
init python:

    # Список доп состояний  Эммы
    states_sam = [
        "tt", "uuu", "wink", "smirk", "eb", "evil", "xm"  #различные выражения м, мм(задумчиво,мечтательно), nm - нейтрально, nju - смущение
    ]   

    create_character_images("sam", states) #общие состояния
    create_character_images("sam", states_sam) #общие состояния

    
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

image sam face eyebrow:
    "sam/eyebrow/sam eyebrow0.png"  with dissolve
    pause 0.8
    "sam/eyebrow/sam eyebrow1.png"  with dissolve
    pause 2.0
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

image sam face seriously:
    "sam/seriously/sam seriously0.png"  with dissolve
    pause 0.8
    "sam/seriously/sam seriously1.png"  with dissolve
    pause 1.5
    "sam/seriously/sam seriously2.png"  with dissolve
    pause 0.8
    "sam/seriously/sam seriously3.png"  with Dissolve(0.3)
    pause 1.5
    "sam/seriously/sam seriously4.png"  with Dissolve(0.2)
    pause 1.8
    repeat

image sam face smirk:
    "sam/smirk/sam smirk0.png"  with dissolve
    pause 1.2
    "sam/smirk/sam smirk1.png"  with dissolve
    pause 1.8
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


image sam face temptation:
    "sam/temptation/sam temptation3.png"  with dissolve
    pause 1.0
    # "sam/temptation/sam temptation1.png"  with dissolve
    # pause 1.5
    "sam/temptation/sam temptation0.png"  with dissolve
    pause 0.7
    "sam/temptation/sam temptation2.png"  with dissolve
    pause 1.2
    "sam/neitral/sam neitral.png"  with dissolve
    choice:
        pause 1.6 
    choice:
        pause 2.2 
    choice:
        pause 3.5 
    "sam/neitral/sam neitral bl.png"  with dissolve
    pause 0.5
    repeat


image sam face uuu:
    "sam/uuu/sam uuu0.png"  with dissolve
    pause 2.8
    # "sam/uuu/sam uuu1.png"  with dissolve
    # pause 1.5
    "sam/neitral/sam neitral.png"  with dissolve
    choice:
        pause 1.6 
    choice:
        pause 2.2 
    choice:
        pause 3.5 
    "sam/neitral/sam neitral bl.png"  with dissolve
    pause 0.5
    "sam/neitral/sam neitral.png"  with dissolve
    pause 1.5
    repeat

image sam face wink:
    "sam/wink/sam wink0.png"  with dissolve
    pause 0.5
    "sam/wink/sam wink1.png"  with dissolve
    pause 1.5
    "sam/wink/sam wink2.png"  with dissolve
    pause 0.5
    "sam/wink/sam wink3.png"  with dissolve
    pause 1.5
    "sam/wink/sam wink4.png"  with dissolve
    pause 0.5
    repeat

image sam face xm:
    "sam/different/sam xm0.png"  with dissolve
    pause 1.2
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

image sam face lsmile:
    "sam/different/sam xm0.png"  with dissolve
    pause 1.2
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

    # always:
    #     "sam body"

    group body:
        attribute b default:
            "sam body"
        attribute sch:
            "sam schoolbody"

    group emotion:
        attribute n:
            "sam face neitral"
        attribute sr:
            "sam face seriously"
        attribute tt:
            "sam face temptation"
        attribute uuu:
            "sam face uuu"
        attribute wink:
            "sam face wink"
        attribute smirk:
            "sam face smirk"
        attribute eb:
            "sam face eyebrow"
        attribute evil:
            "sam face evil"
        attribute xm:
            "sam face xm"
        attribute lsmile:
            "sam face lsmile"
        attribute magic:
            "sam face magic"    

        


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


