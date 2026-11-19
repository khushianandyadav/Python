class Student:

    __nname="Khushi"

    @property
    def name_change(self):
        return self.__nname

    @name_change.setter
    def name(self, new_name):
        self.__nname = new_name

s = Student()
print(s.name_change)
s.name = "Sakshi"
print(s.name_change)