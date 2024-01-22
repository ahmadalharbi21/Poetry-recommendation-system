import json
import csv

input_file_path = 'poemtext1.txt'  # Replace with the path to your input file
output_file_path = 'output.csv'

with open(input_file_path, 'r', encoding='utf-8') as f, open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Poem', 'Metadata'])  # Writing the header

    for line_number, line in enumerate(f, start=1):
        try:
            poem = json.loads(line)
            # Assuming each JSON object has one key-value pair
            for text, metadata in poem.items():
                writer.writerow([text, metadata])
        except json.JSONDecodeError as e:
            print(f"Error on line {line_number}: {e}")
            print(f"Content: {line}")

print(f'CSV file "{output_file_path}" has been created.')
