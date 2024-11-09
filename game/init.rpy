define pushrightSlow = PushMove(2.0, "pushright")

init:
    transform right:
        xalign 0.9 yalign 1.0

    transform left:
        xalign 0.1 yalign 1.0

    image black = Solid("#000")
    


    # Анимация движущегося фона с эффектом параллакса
    image bg highway:
        "images/bg/highway4.png" with pushrightSlow
        pause 2.0
        "images/bg/highway3.png" with pushrightSlow
        pause 2.0
        "images/bg/highway2.png" with pushrightSlow
        pause 2.0
        "images/bg/highway1.png" with pushrightSlow
        pause 2.0
        repeat

    # Определение композитной сцены с машиной
    image driving_scene:
        contains:
            "bg highway"
        contains:
            "images/car.png"
            ypos 0  # Начальная позиция по вертикали (подстройте под ваше изображение)
            zoom 1.2
            fit "cover"
            block:
                ease 0.5 ypos -50  # Движение вверх
                ease 1.5 ypos 0  # Движение вниз
                ease 1.1 ypos -25  # Движение вверх
                ease 2.0 ypos 0  # Движение вниз
                repeat

init python:
    # Инициализация переменных
    # current_language = "russian"
    
    # Настройки игры
    config.window_title = "Секрет королевской школы магии"
    
# Определение изображений
# image bg schoolyard1 = "images/backgrounds/schoolyard1.jpg"
# image bg room = "images/backgrounds/room.jpg"

# Определение аудио
# define audio.main_theme = "audio/main_theme.mp3"
# define audio.click = "audio/click.wav" 



