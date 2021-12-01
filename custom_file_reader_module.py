class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0


class StudentFileReader:
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    def open(self):
        self._inputFile = open(self._inputSrc, 'r')  # open the file and set the status to read
        return self._inputFile

    def close(self):
        self._inputFile.close()  # close the connection
        self._inputFile = None  # return the inputFile status to None

    def fetchRecord(self):  # fetches the next line from the record
        line = self._inputFile.readline()
        if line == '':
            return None

        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student

    def fetchall(self):
        theRecords = list()
        student = self.fetchRecord()
        while student is not None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords
