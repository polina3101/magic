define pushrightSlow = PushMove(2.0, "pushright")

init:
    transform right:
        xalign 0.9 yalign 1.0

    transform left:
        xalign 0.1 yalign 1.0

    transform right1:
        xalign 0.5 yalign 1.0

    transform right2:
        xalign 0.75 yalign 1.0

    transform right3:
        xalign 1.0 yalign 1.0

    transform left1:
        xalign 0.01 yalign 1.0

    transform left2:
        xalign 0.2 yalign 1.0

    transform left3:
        xalign 0.3 yalign 1.0

    transform quiz_img:
        xalign 0.93 yalign 0.4

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

    renpy.music.register_channel("quiz", loop=False, mixer="quiz")
    renpy.music.register_channel("karaoke", loop=False, mixer="karaoke")

########################################################################################    
# Переключение языка
########################################################################################

    # Делаем переменные глобальными для использования в движке Ren'Py
    renpy.config.native_language = "english"
    renpy.config.study_language = "spanish"
    renpy.config.translation_on = False # при false реплика отображается на изучаемом языке, при включении - на родном

    renpy.config.study_mode = True # при включении этого режима реплики на изучаемом языке и их можно перевести 

    def set_study_mode(value):
        renpy.config.study_mode = value  # value должен быть True или False

    def restart_current_dialogue():
        # Получаем текущий идентификатор перевода (translation identifier).
        current_identifier = renpy.exports.get_translation_identifier()
        
        # Если идентификатор не найден, просто перезапускаем взаимодействие.
        if not current_identifier:
            renpy.exports.restart_interaction()
            return
        
        # Находим узел перевода, используя текущий идентификатор.
        translate_node = renpy.game.script.translator.lookup_translate(current_identifier)
        
        # Если узел найден, то используем Jump для перехода к нему.
        if translate_node:
            # renpy.exports.clean_data()
            raise renpy.game.JumpException(translate_node.name)

    def toggle_language():
        renpy.config.translation_on = not renpy.config.translation_on

        restart_current_dialogue()


########################################################################################    
# Словари
########################################################################################

    import json
    import os

    ### словари

    def show_vocabulary_screen(label):
        set_study_mode(False)
        vocabulary = get_vocabulary(label)
        renpy.show_screen("vocabulary_screen", vocabulary=vocabulary)

        # Массив фраз для выбора
        phrases = [
            _("Давайте познакомимся с новыми терминами!"),
            _("Пришло время изучить новые слова!"),
            _("Как насчет изучения новых слов?"),
            _("Не упустите шанс расширить свой словарный запас!"),
            _("Готовы к изучению новых слов?"),
            _("Изучение новых слов — это всегда интересно!"),
            _("Давайте откроем для себя новые слова!"),
        ]
        random_phrase = renpy.random.choice(phrases)

        renpy.say(None, random_phrase)

        renpy.hide_screen("vocabulary_screen")
        set_study_mode(True)


    vocabulary_data = []
    translations_data = []
    full_vocabulary = {}

    def load_vocabulary():
        global vocabulary_data, translations_data, full_vocabulary

        # Загружаем все наборы слов и транскрипции
        base_directory = renpy.config.basedir
        filename = os.path.join(base_directory, "game/vcb/"+renpy.config.study_language+".json")
        with open(filename, "r", encoding="utf-8") as f:
            vocabulary_data = json.load(f)

        filename = os.path.join(base_directory, "game/vcb/"+renpy.config.native_language+".json")
        with open(filename, "r", encoding="utf-8") as f:
            translations_data = json.load(f)

        # Создаем словарь для хранения всех наборов слов по метке
        full_vocabulary = {}

        # Преобразуем данные перевода в словарь для быстрого доступа по ключу
        translations_dict = {}
        for item in translations_data:
            label = item["label"]
            translations_dict[label] = {entry["key"]: entry["word"] for entry in item["vocabulary"]}

        # Формируем полный словарь с объединёнными данными по каждому label
        for item in vocabulary_data:
            label = item["label"]
            combined_vocabulary = []

            # Для каждого слова добавляем его перевод на родной язык
            for entry in item["vocabulary"]:
                combined_entry = {
                    "word": entry["word"],
                    "transcription": entry["transcription"],
                    "translation": translations_dict.get(label, {}).get(entry["key"], "Перевод недоступен")
                }
                combined_vocabulary.append(combined_entry)

            # Сохраняем результат в full_vocabulary по метке label
            full_vocabulary[label] = combined_vocabulary

        return full_vocabulary

    def get_vocabulary(label):
        # Возвращаем конкретный набор слов по метке
        return full_vocabulary.get(label)



