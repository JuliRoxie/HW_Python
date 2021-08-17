'''
Создать сотрудника Mary, пользуясь классом
Employee и перенести его в другую программу,
используя модуль Pickle и файловую систему.
Узнать про + и - модуля Pickle.
'''

import pickle


class Employee:

    def __init__(self):
        self.name = "name"
        self.id = 0000
        self.department = "department"
        self.profession = "profession"
        self.mail = "mail"

    def set_params(self, name_, id_, department_, profession_, mail_):
        self.name = name_
        self.department = department_
        self.profession = profession_
        self.mail = mail_

    def get_params(self):
        print('name:', self.name)
        print('id:', self.id)
        print('department:', self.department)
        print('profession:', self.profession)
        print('mail:', self.mail)


emp = Employee()
#name, id, department, profession, mail
emp.set_params('Mary', 1, 'support', 'engineer', 'nomail')
with open('myfile', 'wb') as handle:
    pickle.dump(emp, handle, protocol=pickle.HIGHEST_PROTOCOL)


