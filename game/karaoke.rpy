init python:
### Караоке
    import random  # Добавьте импорт random

    all_songs_data = {}
    is_karaoke_active = False

    def format_timestamp(timestamp_str):
        try:
            # Разделяем строку на минуты и секунды
            minutes, seconds = map(float, timestamp_str.split(":"))
            total_seconds = minutes * 60 + seconds
            return total_seconds
        except ValueError:
            raise ValueError(f"Неверный формат временной метки: {timestamp_str}")


    def load_all_karaoke_data():
        global all_songs_data

        
        base_directory = renpy.config.basedir
        filename = os.path.join(base_directory, "game/songs", renpy.config.study_language + ".json")

       
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

                    
        if "songs" not in data:
            raise ValueError("No songs found in the JSON file.")
        
        # Инициализируем словарь для хранения всех песен
        all_songs_data = {}

        # Проходим по всем песням и сохраняем данные
        for song_id, song in data["songs"].items():
            study_lines = [entry["line"] for entry in song["lyrics"]]

            timings = [format_timestamp(entry["timestamp"]) for entry in song["lyrics"]]

            translation_lines = [
                next((t["text"] for t in entry["translations"] if t["lang"] == renpy.config.native_language), "")
                for entry in song["lyrics"]
            ]

            start_time = song.get("start", 0.0)
            end_time = song.get("end")  

            # Сохраняем данные для каждой песни в формате {study_lines, translation_lines, timings}
            all_songs_data[song_id] = {
                "study_lines": study_lines,
                "translation_lines": translation_lines,
                "timings": timings,
                "start": format_timestamp(start_time),
                "end": format_timestamp(end_time)
            }

        return all_songs_data

    def get_karaoke_song(song_id):
        # Возвращаем данные для конкретной песни
              
        song_data = all_songs_data.get(song_id)
        if not song_data:
            raise ValueError(f"Song with ID '{song_id}' not found.")

        return song_data["study_lines"], song_data["translation_lines"], song_data["timings"], song_data["start"], song_data["end"]


    def show_karaoke(song_id):

        _dismiss_pause = False

        renpy.music.stop()
        
        study_lines, translation_lines, timings, start_time, end_time = get_karaoke_song(song_id)

        renpy.hide_screen("say")

        # Найти первый `timing`, который находится в пределах `start_time` и `end_time`
        initial_pause = next((t for t in timings if start_time <= t <= (end_time or float('inf'))), 0.0)
        renpy.pause(initial_pause - start_time, hard=True)  # Пауза до первого подходящего тайминга

        for i in range(len(study_lines)):
            renpy.show_screen("karaoke_screen", study_line=study_lines[i], translation_line=translation_lines[i])
            renpy.restart_interaction()
            # Вычисляем интервал для паузы
            if i < len(study_lines) - 1:
                pause_duration = timings[i + 1] - timings[i]
            else:
                pause_duration = 2.0  # Пауза после последней строки (можно настроить)

            renpy.pause(pause_duration, hard=True)

        renpy.hide_screen("karaoke_screen")