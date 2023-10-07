import xml.etree.ElementTree as ET
import csv
import json
import os
f = open("./files/example.txt")
print(f)
txt = f.read(1)
print(txt)

txt = f.readlines()
print(txt)

txt = f.readline()
print(txt)

txt = f.read().splitlines()
print(txt)
f.close()


with open('./files/example.txt', 'a') as file:
    file.write("This line is appended.")

with open('./files/writing_file_example.txt', 'w+') as fw:
    fw.write("This line will added to newly created file.")

# os.remove('./files/writing_file_example.txt')

if os.path.exists('./files/writing_file_example.txt'):
    os.remove('./files/writing_file_example.txt')
else:
    print("file not exists")

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


person_dct_to_json = json.dumps(person_dct, indent=8)
print(person_dct_to_json)
print(type(person_dct_to_json))

with open('./files/json_example.json', 'w', encoding='utf-8') as json_file:
    json.dump(person_dct, json_file, ensure_ascii=False, indent=6)

with open('./files/csv_example.csv') as csv_f:
    # w use, reader method to read csv
    csv_reader = csv.reader(csv_f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print(root)
print(root.attrib)

for child in root:
    print(child.text)
