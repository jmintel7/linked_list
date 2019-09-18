from linked_list import linked_list
from student import Student
import pandas as pd
import memory_profiler as mem_profile

my_list = linked_list()

dataset = pd.read_excel('student.xlsx', header = 0, sheet_name = 0)

for index,row in dataset.iterrows():
    data = Student(row['Rollno'], row['Name'], row['Gender'], row['Marks'])
    my_list.append(data)

print('Length of list : ',my_list.length())

rollno = 1
data = my_list.get_rollno(rollno)
if data:
    data.display()
rollno = 1
data = my_list.erase(rollno)
data = my_list.get_rollno(rollno)
if data:
    data.display()

print(my_list.length())
print('Memory used: ', mem_profile.memory_usage()[0])
