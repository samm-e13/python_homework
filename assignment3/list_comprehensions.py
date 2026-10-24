import csv

with open('../csv/employees.csv', 'r') as file:
    read_file = csv.reader(file)
    list_of_lists = list(read_file)

parsed_list = [element[1] + " " + element[2] for element in list_of_lists if list_of_lists[1:]]
with_e = [element for element in parsed_list if "e" in element]

print(parsed_list)
print(with_e)