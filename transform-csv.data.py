import json
import csv

def convert_to_csv(input_file, output_file):
    # Load data from JSON file
    with open(input_file, 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)

    # Convert documents to single-row human-bot conversation format
    conversations = []
    for data in data_list:
        conversation = f'### Human: {data["human"]}### Assistant: {data["assistant"]}'
        conversations.append([conversation])

    # Save transformed data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
       
        writer.writerows(conversations)

    print(f'Data saved to {output_file}')

# Example usage
input_file = 'human_assistant_feedbacks.json'
output_file = 'human_assistant_feedbacks.csv'
convert_to_csv(input_file, output_file)
