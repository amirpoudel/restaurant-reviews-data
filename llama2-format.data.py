import csv

# Define a function to read the CSV file and transform the data
def process_csv(input_file):
    conversations = []
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for row in reader:
            conversation_text = row[0]
            segments = conversation_text.split('###')

            reformatted_segments = []

            # Iterate over pairs of segments
            for i in range(1, len(segments) - 1, 2):
                human_text = segments[i].strip().replace('Human:', '').strip()

                # Check if there is a corresponding assistant segment before processing
                if i + 1 < len(segments):
                    assistant_text = segments[i+1].strip().replace('Assistant:', '').strip()

                    # Apply the new template
                    reformatted_segments.append(f'<s>[INST] {human_text} [/INST] {assistant_text} </s>')
                else:
                    # Handle the case where there is no corresponding assistant segment
                    reformatted_segments.append(f'<s>[INST] {human_text} [/INST] </s>')

            conversations.append(''.join(reformatted_segments))

    return conversations

# Write the transformed data to a CSV file
def write_to_csv(output_file, conversations):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['text'])  # Write header
        for conversation in conversations:
            writer.writerow([conversation])

# Example usage
input_file = 'human_assistant_feedbacks.csv'
output_file = 'llama2_transformed_data.csv'
conversations = process_csv(input_file)
write_to_csv(output_file, conversations)
