from array2D_ADT import Array2D
from array_ADT import Array

myArray = Array(10)
myArray.clear(None)

for i in range(len(myArray)):
    myArray[i] = 10-i

for i in range(len(myArray)):
    print(myArray[i])


filename = "grades.txt"
gradeFile = open(filename ,'r')

numStudents     = int(gradeFile.readline())
numExams  = int(gradeFile.readline())

print("numExams = " + str(numExams))
print("numStudents = " + str(numStudents))

examGrades = Array2D(numStudents, numExams)

i = 0
for student in gradeFile:
    grades = student.split()
    for j in range(numExams):
        examGrades[i,j] = int(grades[j])
    i += 1
gradeFile.close()

for i in range( numStudents ) :
    total = 0
    for j in range( numExams ) :
        total += examGrades[i,j]
    examAvg = total / numExams
    print( "%2d: %6.2f" % (i+1, examAvg) )