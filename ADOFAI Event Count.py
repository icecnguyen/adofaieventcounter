import tkinter as tk
from tkinter import filedialog
import json

def open_file():
    file_path = filedialog.askopenfilename(
        title="Chọn tệp ADOFAI",
        filetypes=(("ADOFAI files", ".adofai"), ("All files", ".*"))
    )
    if file_path:
        with open(file_path, encoding='utf-8-sig') as file:
            contents = file.read()
            data = json.loads(contents)
            event_counts = {}
            total_events = 0
            decoration_count = 0
            if 'actions' in data:
                actions = data['actions']
                for action in actions:
                    event_type = action.get('eventType', 'Unknown')
                    if event_type not in ['setspeed', 'twirl']:
                        total_events += 1
                        if event_type in event_counts:
                            event_counts[event_type] += 1
                        else:
                            event_counts[event_type] = 1
                    if event_type == 'decoration':
                        decoration_count += 1
            result_text = f"Total Event: {total_events}\n"
            result_text += "Event Count:\n"
            for event_type, count in event_counts.items():
                result_text += f"{event_type}: {count}\n"
            result_label.config(text=result_text)

root = tk.Tk()
root.title("ADOFAI Event Counter")

open_button = tk.Button(root, text="Choose ADOFAI File", command=open_file)
open_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
