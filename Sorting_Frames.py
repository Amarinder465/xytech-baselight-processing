import re
import csv
import argparse

name_path = []
whole_path = []
roles = []
# Define command-line arguments
parser = argparse.ArgumentParser(description='read data in')
parser.add_argument('xytech_file', type=str, help='input xytech_file')
parser.add_argument('baselight_file', type=str, help='input baselight_file')

# Parse command-line arguments
args = parser.parse_args()

with open(args.xytech_file, 'r') as Xytech:
    Content_Xytech = Xytech.read()
    # loop through the file Content and extract each path
    start_index = Content_Xytech.find("/")
    while start_index >= 0:
        end_index = Content_Xytech.find('\n', start_index)
        path = Content_Xytech[start_index:end_index]
        name_path.append(path)
        start_index = Content_Xytech.find("/", end_index)
    # following code is for outputting the people's names
    start_index = Content_Xytech.find(": ")
    while start_index >= 0:
        end_index = Content_Xytech.find('\n', start_index)
        path = Content_Xytech[start_index:end_index]
        roles.append(path)
        start_index = Content_Xytech.find(": ", end_index)
    # following code is for outputting the note
    notes_regex = r'notes:\s*(.*)'
    # Use the regular expression to extract the notes data
    notes_match = re.search(notes_regex, Content_Xytech, re.IGNORECASE | re.DOTALL)
    if notes_match:
        notes_data = notes_match.group(1)

with open(args.baselight_file, 'r') as Baselight_export:
    content_baselight = Baselight_export.read()
    # loop through the file Content and extract each path
    start_index = content_baselight.find("/starwars")
    while start_index >= 0:
        end_index = content_baselight.find('\n', start_index)
        path = content_baselight[start_index:end_index]
        whole_path.append(path)
        start_index = content_baselight.find("/starwars", end_index)

combineFile = []
for path1 in whole_path:
    path1_match = path1.split(' ')[0]  # Extracting only the path until the first space
    for path2 in name_path:
        path2_match = path2.split('/production')[1]  # Extracting the path after "production"
        if path1_match == path2_match:
            combineFile.append(path2 + path1.replace(path1_match, ''))

onlyNumbersCombineFile = []
for element in combineFile:
    elements = element.split()
    nums = [e for e in elements if e.isdigit()]
    onlyNumbersCombineFile.append(' '.join([elements[0]] + nums))


path_dict = {}

for s in onlyNumbersCombineFile:

    parts = s.split()
    path = parts[0]
    numbers = list(map(int, parts[1:]))
    if path in path_dict:
        path_dict[path].extend(numbers)
    else:
        path_dict[path] = numbers
roles = [d.replace(':', '').strip().replace(',', '') for d in roles]
notes = [notes_data]
alldata = roles + notes
output_list = []
for path, numbers in path_dict.items():
    numbers.sort()
    start = end = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if end is None or start == end:
                output_list.append([path, start])
            else:
                output_list.append([path, f"{start}-{end}"])
            start = end = numbers[i]
    if end is None or start == end:
        output_list.append([path, start])
    else:
        output_list.append([path, f"{start}-{end}"])

def num_order(item):
    if isinstance(item[1], int):
        return item[1]
    else:
        return int(item[1].split('-')[0])
# sort the list by the start number using the key function

output_list_sorted = sorted(output_list, key=num_order)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([alldata])
    csvfile.write(' \n\n')
    writer.writerows(output_list_sorted)