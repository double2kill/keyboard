import keyboard
from datetime import datetime
import ast

try:
    with open("count.log", "r") as count_file:
        key_count = ast.literal_eval(count_file.read())
except FileNotFoundError:
    key_count = {}

write_counter = 0
write_frequency = 10

current_time_str = datetime.now().strftime("%Y%m%d%H%M%S")
result_file_name = f"result_{current_time_str}.log"

def on_any_key_up_event(e):
    global write_counter, key_count
    key = e.name
    event_type = e.event_type

    if event_type == 'up':
        key_count[key] = key_count.get(key, 0) + 1

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = f"{current_time} - e: {e} Key: {key}, Count: {key_count[key]}\n"

        with open(result_file_name, "a") as log_file:
            log_file.write(log_data)

        write_counter += 1
        if write_counter >= write_frequency:
            write_counter = 0

            sorted_key_count = {k: v for k, v in sorted(key_count.items(), key=lambda item: item[1], reverse=True)}
            with open("count.log", "w") as count_file:
                count_file.write(str(sorted_key_count))

keyboard.on_release(callback=on_any_key_up_event)
keyboard.wait('esc')
