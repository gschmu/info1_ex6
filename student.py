from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grade = {}

        ######## CODE MISSING HERE

    def add_module(self,module):
        self.modules.append(module)
        self.grade[module] = Module.get_grade(module) #es muss über
        ######## CODE MISSING HERE

    def get_list_modules(self):
        for mod in self.modules:
            print("Modules of Student {}:".format(self.name))
            print ("\t {}".format(mod))
        ######## CODE MISSING HERE

    def get_grades(self):
        print("Grades of Student {}:".format(self.name))
        for key,value in self.grade.items():
            print("\t {}: {}".format(key,value))
            #print (key)
        ######## CODE MISSING HERE

### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1 #diese print funktion stimt so nicht! wir mussten die print für course mit course: definieren!


me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6

###################

#FRAGEN DAZU: Wie ist es möglich eine Note pro Student zu setzten?
#so wie wir es programmiert haben kann man nur eine Note pro Modul setzten, oder?

# Module.set_grade(math1,5.5)
# me.add_module(math1)
# me.get_grades()
#
# me.add_module(sem)
# me.get_grades()