# Create a Student class which contains the student's
#   first name,
#   second name, and
#   score
# The student class makes extending and sub-classing simpler
class Student:

    def __init__(self, firstName, lastName, score):
        self.firstName = firstName
        self.lastName = lastName
        self.score = score

    def getScore(self):
        return self.score
