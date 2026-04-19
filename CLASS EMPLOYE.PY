class Employee:
    def _init_(self):
        print('Emplyee created.')
    def _del_(self):
        print('Destructur called,Employee deleted')
oby = Employee()
del oby