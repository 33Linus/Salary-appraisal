# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:45:42 2022

@author: Linus
"""

import pandas as pd
import copy

emp = pd.read_excel('salary_appraisal.xlsx',sheet_name='employee')
updated_emp = copy.deepcopy(emp)
app = pd.read_excel('salary_appraisal.xlsx',sheet_name='appraisal')

today=pd.to_datetime('today')

updated_emp['doj'] = pd.to_datetime(updated_emp['doj'],format='%d-%m-%Y')

updated_emp['experience'] = round(((today-updated_emp['doj']).dt.days)/365.2425)

up_si = updated_emp.set_index('emp_id')
up_emp_dict = up_si.T.to_dict('list')

app_si = app.set_index('emp_id')
app_dict = app_si.T.to_dict('list')

emp_id = []
name = []
designation = []
updated_salary = []
doj = []
age =[]
department = []
experience = []

for k,v in up_emp_dict.items():
    emp_id.append(k)
    if k in app_dict.keys():
        if (20 <= v[4] < 30) & (v[6] < 4):
            v[2] = v[2] * 1.085
        elif (30<= v[4] < 40) & (v[6] < 6):
            v[2] = v[2] * 1.08
        elif (40 <= v[4] <= 50) & (8 <= v[6] <= 10):
            v[2] = v[2] * 1.09
        elif (v[4] > 55):
            v[2] = v[2] * 1.05
        elif (v[6] > 10):
            v[2] = v[2] * 1.105
        else:
            v[2] = v[2] * 1.02
    
    name.append(v[0])
    designation.append(v[1])
    updated_salary.append(v[2])
    doj.append(v[3])
    age.append(v[4])
    department.append(v[5])
    experience.append(v[6])
target_dict = {'emp_id':emp_id,
               'name':name,
               'designation':designation,
               'updated_salary':updated_salary,
               'doj':doj,
               'age':age,
               'department':department,
               'experience':experience
              }
df = pd.DataFrame(target_dict)
df.to_csv('updated_salary.csv',index=False)