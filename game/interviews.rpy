# label interview_start:
#     scene bg room
    
#     s "Давай познакомимся поближе."
    
#     menu:
#         "Как тебя зовут?"
        
#         "Представиться":
#             $ player_name = renpy.input("Введите ваше имя:")
#             s "Приятно познакомиться, [player_name]!"
            
#         "Пропустить":
#             $ player_name = "Ученик"
#             s "Ну что ж, будем называть тебя просто учеником."
    
#     return

# # Дополнительные метки для интервью с другими персонажами
# label interview_teacher:
#     # ... код интервью с учителем ...
#     return 