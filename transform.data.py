import json

# Load data from JSON file
with open('feedbacks.json', 'r', encoding='utf-8') as json_file:
    data_list = json.load(json_file)

# Convert documents to human-bot conversation format
human_assistant_data = []
for data in data_list:
    human_assistant_data.append({
        "human": data["feedback"],
        "assistant": data["label"]
    })

# Save transformed data to a new JSON file
with open('human_assistant_feedbacks.json', 'w', encoding='utf-8') as json_file:
    json.dump(human_assistant_data, json_file, indent=4, ensure_ascii=False)

print(f'Data saved to human_assistant_feedbacks.json')
