# import json
#
# output_file_path = ''
# # process_poems(input_file_path, output_file_path)
# f = open ('org_poem', 'w', encoding='utf-8')
# with open("poemtext", 'r', encoding='utf-8') as file:
#     poem_counter = 1
#     for line in file:
#         json_data = line
#         json_data_double_quotes = json.loads(json_data)
#         for d in json_data_double_quotes:
#             value = d[0]
#             poem_without_conter = {d : value}
#             poem_without_conter = f"{poem_without_conter}"
#             poem_dict = dict()
#             poem_dict = {poem_counter:poem_without_conter}
#             poem_dict = f"{poem_dict} + /n"
#             poem_counter += 1
#             print(poem_dict)
#         f.write(poem_dict)
#
# f.close()
import json

input_file_path = 'poemtext1.txt'  # Replace with the path to your input file
output_file_path = 'path_to_output_file'  # Replace with the path to your output file


# Read the input file, process each line, and write to the output file
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
    poem_counter = 1
    result_json = {}

    for line in input_file:
        try:
            # Try to load the JSON data from the line
            json_data = json.loads(line)
            # Add the JSON data to our result dictionary with an incrementing key
            result_json[poem_counter] = json_data

            poem_counter += 1
        except json.JSONDecodeError as e:
            print(f"Error processing line: {e}")

    # Write the result JSON dictionary to the output file
    json.dump(result_json, output_file, ensure_ascii=False, indent=2)

print(f"Processing complete. Output written to {output_file_path}")




#
# import json
#
# def convert_json(input_file_path, output_file_path):
#     # Read the original JSON data from the input file
#     with open(input_file_path, 'r', encoding='utf-8') as file:
#         original_json = json.load(file)
#
#     # Initialize a new list for the converted format
#     converted_json = []
#
#     # Iterate through each item in the original JSON
#     for index, item in enumerate(original_json, start=1):
#         # For each item, create a new dictionary with the index as a string key
#         new_item = {str(index): item}
#         # Add the new dictionary to the converted list
#         converted_json.append(new_item)
#
#     # Write the converted JSON to the output file
#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         json.dump(converted_json, file, indent=2, ensure_ascii=False)
#
# # Example usage
# input_file_path = 'poemtext'  # Replace with your input file path
# output_file_path = 'path/to/your/output.json'  # Replace with your desired output file path
#
# # Convert the JSON
# convert_json(input_file_path, output_file_path)
