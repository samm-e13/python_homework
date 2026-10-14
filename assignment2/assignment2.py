#Task2:
import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    emp_dict = {}
    emp_list = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            csv_file = csv.reader(file)

            for i, line_item in enumerate(csv_file):
                if i == 0:
                    emp_dict['fields'] = line_item
                else:
                    emp_list.append(line_item)
            emp_dict['rows'] = emp_list
        return emp_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
#Task3: 
def column_index(index_string):
    return employees['fields'].index(index_string)

employee_id_column = column_index('employee_id')
print(employees['fields'])
print(employees['rows'][0])

#Task4: insert row, returns employee first name
def first_name(row_here):
    return employees['rows'][row_here][column_index('first_name')]

#Task5: 
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task6: 
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task7:
def sort_by_last_name():
    #pull dictionary -> find last name -> apply sort to last name
    employees['rows'].sort(key = lambda row: row[column_index('last_name')])
    return employees['rows']

#Task8:
def employee_dict(employee_row):
    dictionary = {}
    for i in range(1,4):
        dictionary[employees['fields'][i]] = employee_row[i]
    return dictionary

print(employee_dict(employees['rows'][6]))

#Task9:
def all_employees_dict():
    all_dict = {}
    for element in employees['rows']:
        all_dict[element[0]] = employee_dict(element)
    return all_dict
print(all_employees_dict())

#Task10:
def get_this_value():
    return os.getenv('THISVALUE')

#Task11:
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret('magic_man')
print(custom_module.secret)

#Task12:
def read_minutes():
    with open('../csv/minutes1.csv', 'r') as min1, open('../csv/minutes2.csv', 'r') as min2:
        def loop_helper(file_here):
            minutes = {}
            min_list = []
            for i, row in enumerate(file_here):
                if i == 0:
                    minutes['fields'] = row
                else:
                    min_list.append(tuple(row))
            minutes['rows'] = min_list
            return minutes

        min1_csv = csv.reader(min1)
        min2_csv = csv.reader(min2)

        minutes1 = loop_helper(min1_csv)
        minutes2 = loop_helper(min2_csv)

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

#Task13:
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    unioned_set = set1.union(set2)
    return unioned_set

minutes_set = create_minutes_set()

#Task14:
def create_minutes_list():
    min_set = list(minutes_set)
    #convert each element in the list to a tuple 
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),min_set))

minutes_list = create_minutes_list()
print(minutes_list)

#Task15:
def write_sorted_list():
    minutes_list.sort(key = lambda x: x[1])
    minutes_listv2 = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open('./minutes.csv', 'w') as file: 
        written = csv.writer(file)
        written.writerow(minutes1['fields'])
        for row in minutes_listv2:
            written.writerow(row) 
    return minutes_listv2

write_sorted_list()
        
        


