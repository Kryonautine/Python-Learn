class Student:
    # Initializing the details
    def __init__(self):
        self.stdN = input("Name : ")
        self.stdAN = input("Admission Number : ")
        self.subject = int(input("Enter the number of subjects : "))
        self.stdM = [
            int(input("Enter the subject mark : ")) for i in range(self.subject)
        ]

    # Changing name of a given student
    def setStdDetails(self, name):
        self.stdN = name

    # Printing the details of a student
    def getStdDetail(self):
        print(self.stdN)
        print(self.stdAN)
        print(self.stdAvg())

    # Calculating the average of their marks
    def stdAvg(self):
        markAvg = sum(self.stdM) / self.subject
        return markAvg


if __name__ == "__main__":

    # Creating an array to store details of 5 students
    totstudent = []
    for i in range(5):
        var = Student()
        totstudent.append(var)

    # Displaying the details of each student
    for i in range(5):
        totstudent[i].getStdDetail()
