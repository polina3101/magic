define right_answer = _("Правильно! Отличная работа!")
define wrong_answer = _("Нет. Правильный ответ: ")

# Массив с фразами
define phrases = [
    _("Давай проверим, как мы усвоили этот урок."),
    # _("Пора пройти небольшой квиз."),  # Закомментировано, если не нужно
    _("Ты должен ответить на несколько вопросов."),
    _("Нужно немного позаниматься."),
    _("Надеюсь, вы готовы к проверке знаний!")
]


init python:

    import json
    import os
    import random
#     class Question:
#         def __init__(self, text, answers, correct):
#             self.text = text
#             self.answers = answers
#             self.correct = correct
            
#     # Список вопросов
#     questions = [
#         Question(
#             "Как сказать 'Привет' на английском?",
#             ["Hello", "Goodbye", "Thanks", "Sorry"],
#             0
#         ),
#         # Добавьте больше вопросов здесь
#     ]

# label quiz_start:
#     $ scors = 0
    
#     s "Давай проверим твои знания!"
    
#     python:
#         for q in questions:
#             renpy.say(s, q.text)
#             choics = renpy.display_menu([(a, i) for i, a in enumerate(q.answers)])
#             if choics == q.correct:
#                 scors += 1
#                 renpy.say(s, "Правильно!")
#             else:
#                 renpy.say(s, "Неправильно. Правильный ответ: " + q.answers[q.correct])
    
#     s "Твой результат: [score] из [len(questions)]"
    
#     return 


    ### квизы
    def load_quiz_texts():
        global quiz_texts

        base_directory = renpy.config.basedir
        filename = os.path.join(base_directory, "game/qtl/"+renpy.config.study_language+".json")
        with open(filename, "r", encoding="utf-8") as f:
            quiz_texts = json.load(f)        


    def get_quiz_translator(label):
        # Проверка, не является ли quiz_texts пустым
        if not quiz_texts:
            renpy.log("Warning: 'quiz_texts' is empty. Maks surs 'load_quiz_texts()' was called successfully.")
            return None

        # Перебираем элементы, пока не найдем квиз с указанной меткой
        for idx, q in enumerate(quiz_texts):
            renpy.log("Checking quiz at index {}: {}".format(idx, q))
            if q.get("label") == label:
                # Ищем правильный ответ
                correct_answer = next((answer['text'] for answer in q.get('answers', []) if answer.get('correct')), "")
                
                # Добавляем текст правильного ответа в результат
                q['correct_answer'] = correct_answer
                
                renpy.log("Found quiz with label '{}': {}".format(label, q))
                return q

        # Если ни один квиз не был найден, логируем и возвращаем None
        renpy.log("Quiz with label '{}' not found after checking all quizzes.".format(label))
        return None



    def show_quiz_screen(quiz_label, character):
        set_study_mode(False)
        
        
        # Выбор случайной фразы
        random_phrase = random.choice(phrases)
        renpy.say(character, random_phrase)

        # # Добавляем меню выбора: пропустить квиз или пройти
        # $ choice = renpy.display_menu([
        #     ("Пройти квиз", "proceed"),
        #     ("Пропустить квиз", "skip")
        # ])

        # if choice == "proceed":
        #     renpy.call(quiz_label)  # Переход к квизу
        # elif choice == "skip":
        #     s "Вы решили пропустить квиз."
        #     return  # Возврат к предыдущему экрану

        # Останавливаем музыку и звук на всех каналах с затуханием
        renpy.music.stop(channel="music", fadeout=2.0)  # Останавливает музыку
        renpy.music.stop(channel="sound", fadeout=2.0)  # Останавливает звуковые эффекты

        renpy.call(quiz_label)  # Переход к квизу
        # renpy.say(character, "Отлично")
        # set_study_mode(True)

    def load_quiz_data(quiz_label):
        qt = get_quiz_translator(quiz_label)
        question = qt.get('question', "")
        answers = qt.get('answers', [])
        correct_answer = qt.get('correct_answer', "")
        return question, answers, correct_answer


label quiz_s1scene1:
    # Получаем текст вопроса и ответы для текущего квиза
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_getting")

    menu:
        # "Our king is ___ married again?" (getting) Вставьте пропущенное слово.
        s "[question] Вставьте пропущенное слово."

        "[answers[0]['text']]" if len(answers) > 0:
            if answers[0]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[1]['text']]" if len(answers) > 1:
            if answers[1]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[2]['text']]" if len(answers) > 2:
            if answers[2]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."


label quiz_s1scene1_opportunities:
    # Вопрос: Переведи слово "возможности"
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_opportunities")
    
    menu:
        s "Переведи слово 'возможности'."
        "[answers[0]['text']]" if len(answers) > 0:
            if answers[0]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[1]['text']]" if len(answers) > 1:
            if answers[1]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."


label quiz_s1scene1_announce:
    # Вопрос: Переведи слово "to announce"
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_announce")

    menu:
        s "Переведи слово '[question]'."
        
        "предупреждать":
            s "[wrong_answer][correct_answer]."

        "объявлять":
            s "[right_answer]"

        "анексировать":
            s "[wrong_answer][correct_answer]."


label quiz_s1scene1_sentence_strange:

    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_sentence_strange")

    menu:
        # Вопрос: Переведи предложение "Разве это нестранно?"
        s "Переведи предложение 'Разве это нестранно?'"
        
        "[answers[0]['text']]" if len(answers) > 0:
            if answers[0]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[1]['text']]" if len(answers) > 1:
            if answers[1]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[2]['text']]" if len(answers) > 2:
            if answers[2]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."


#заменить на странный
label quiz_s1scene1_audio_announced:
    # Вопрос: Послушай аудио и напиши пропущенное слово 
    #Ths King has ____ (announced) his wedding to ths daughter of ths Minister of Economy.
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_audio_announced")

    play quiz "voice/{}/s1scene1_bdcacca9.mp3".format(renpy.config.study_language)

    $ answer = renpy.input("Послушай аудио и напиши пропущенное слово: ").strip().lower()
    if answer == str(correct_answer).lower():
        s "[right_answer]"
    else:
        s "[wrong_answer][correct_answer]."

label quiz_s1scene1_picture_wedding:
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_picture_wedding")

    # Показываем изображение, на основе которого нужно выбрать слово
    show screen quiz_image_screen("quiz/wedding.png")

 
    menu:
        # Вопрос: Выбери слово, которое соответствует картинке "свадьба"
        s "Выбери слово, которое соответствует картинке."
        "[answers[0]['text']]" if len(answers) > 0:
            if answers[0]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[1]['text']]" if len(answers) > 1:
            if answers[1]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[2]['text']]" if len(answers) > 2:
            if answers[2]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

    hide screen quiz_image_screen


label quiz_s1scene1_audio_married:
    # Вопрос: Послушай аудио и выбери соответствующее предложение 
    # Our king is getting married again?
    $ question, answers, correct_answer = load_quiz_data("quiz_s1scene1_audio_married")

    play quiz "voice/{}/s1scene1_eb0b201c.mp3".format(renpy.config.study_language)

    menu:
        # Вопрос: Послушай аудио и выбери соответствующее предложение
        s "Послушай аудио и выбери соответствующее предложение"
        
        "[answers[0]['text']]" if len(answers) > 0:
            if answers[0]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[1]['text']]" if len(answers) > 1:
            if answers[1]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

        "[answers[2]['text']]" if len(answers) > 2:
            if answers[2]['correct']:
                s "[right_answer]"
            else:
                s "[wrong_answer][correct_answer]."

    jump s1scene2