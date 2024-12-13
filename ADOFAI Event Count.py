import json

file_path = input("Enter ADOFAI Path: ")

try:
    with open(file_path, encoding='utf-8-sig') as file:
        contents = file.read()
        data = json.loads(contents)
        event_counts = {}
        total_events = 0
        decoration_count = 0
        if 'actions' in data:
            actions = data['actions']
            for action in actions:
                event_type = action.get('eventType')
                if event_type not in ['setspeed', 'twirl']:
                    total_events += 1
                    if event_type in event_counts:
                        event_counts[event_type] += 1
                    else:
                        event_counts[event_type] = 1
        print(f"Total Events: {total_events}")
        for event_type, count in event_counts.items():
            print(f"{event_type}: {count}")
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file. Please check the file content.")