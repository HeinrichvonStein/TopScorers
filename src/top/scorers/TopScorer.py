from top.scorers.ParseCSV import ParseCsv


def getTopScorer(csv_file, containsHeader):
    data = ParseCsv(csv_file, containsHeader)
    data.parse_csv()
    dataDict = data.getDataDict()

    names = []

    for name, student in dataDict.items():
        if student.getScore() == data.getMaxScore():
            names.append(name)

    names.sort()
    for name in names: print(name)

    print(f"Score: {data.getMaxScore()}")
