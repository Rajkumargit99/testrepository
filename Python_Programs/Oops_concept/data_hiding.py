
class school:
    school_fname = "fathima convent"

    def __init__(self, name, area, type):
        self.name = name
        self._area = area
        self.__type = type

    def school_details(self):
        print("School name:", self.name)
        print("School address:", self._area)
        print("School type:", self.__type)

    def _school_full_name(cls):
        print("school full name:", cls.school_fname)

    def __school_type(self):
        print("school type", self.__type)

    def _school_medium(self):
        print("school medium:", self._area)
        print("school type", self.__type)

obj = school("fathima", "kzr", "english")
obj.school_details()
print("-----------------------")
obj._school_full_name()
print("-----------------------")
obj._school__school_type()
print("-----------------------")
obj._school_medium()