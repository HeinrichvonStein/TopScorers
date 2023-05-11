from top.scorers.Student import Student


class ParseCsv:
    # Use a dictionary to allow faster student lookups
    data = {}
    max_score = 0

    def __init__(self, file, contains_header):
        self.file = file
        self.contains_header = contains_header

    def parse_csv(self):
        with open(self.file, "r") as f:
            if self.contains_header:
                line = f.readline()
            while True:
                line = f.readline().rstrip('\n')
                if line == "":
                    break
                row = line.split(",")
                name = f"{self.getStudentFirstName(row)}  {self.getStudentSecondName(row)}"
                self.data[name] = Student(self.getStudentFirstName(row),
                                                     self.getStudentSecondName(row),
                                                     self.getStudentScore(row)
                                                     )
                self.checkMaxScore(self.getStudentScore(row), self.max_score)

    def getStudentFirstName(self, line):
        return line[0]

    def getStudentSecondName(self, line):
        return line[1]

    def getStudentScore(self, line):
        return int(line[2])

    def getDataDict(self):
        return self.data

    def checkMaxScore(self, studentScore, maxScore):
        if studentScore > maxScore:
            self.max_score = studentScore

    def getMaxScore(self):
        return self.max_score