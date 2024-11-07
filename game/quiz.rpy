# init python:
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
#     $ score = 0
    
#     s "Давай проверим твои знания!"
    
#     python:
#         for q in questions:
#             renpy.say(s, q.text)
#             choice = renpy.display_menu([(a, i) for i, a in enumerate(q.answers)])
#             if choice == q.correct:
#                 score += 1
#                 renpy.say(s, "Правильно!")
#             else:
#                 renpy.say(s, "Неправильно. Правильный ответ: " + q.answers[q.correct])
    
#     s "Твой результат: [score] из [len(questions)]"
    
#     return 