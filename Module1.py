import module3
from module2 import state
from module2 import major
from module2 import semester


class Inter_App:
    def _init_(self, state, major, semester):
        self.state = state
        self.major = major
        self.semester = semester

    def state_app(self):
        for stat in state:
            if state == "California" or "Florida":
                print("For this State your chance of acceptance  is high")
            else:
                print("Chance very low")

    def major_app(self):
        for maj in major:
            if major == "Computer Science" or "Civil Engineering":
                print("For this major your chance of acceptance  is high")
            else:
                print("Chance very low")

    def semester_app(self):
        for sem in semester:
            if semester == "Sping" or "Fall":
                print("For this semester your chance of acceptance  is high")
            else:
                print("Chance very low")


student1_data = Inter_App()
student1_data.state_app
student1_data.major_app
student1_data.semester_app
