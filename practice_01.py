# average score of the class
def average(l):
    sum = 0
    cnt = 0
    for i in l:
        sum += i
        cnt += 1
    avg = sum/cnt
    print("Total marks are: ", sum)
    print("Average marks are:{:.2f} ".format(avg))

def Maximum(l):
    Max = l[0]
    for i in range(len(l)):
        if l[i] >Max:
            Max = l[i]
    return Max

#count of student who were absent
def absentCnt(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] != -999:
            cnt += 1
    return cnt

def Minimum(l):
    for i in range(len(l)):
        if l[i] != -999:
            Min = l[i]
            break
    for j in range(i + 1, len(l)):
        if l[j] != -999 and l[j] < Min:
            Min = l[j]
    return Min

#display marks with higher frequency
def maxFrequency(l):
    i = 0
    Max = 0
    print("Marks ------> frequency count")
    for ele in l:
        if l.count(ele) > Max:
            Max = l.count(ele)
            mark = ele
        if l.index(ele) == i:
            print(ele, "---->", l.count(ele))
        i += 1
    return mark, Max

#input the number of student and average
marksInFDS = []
noStudent = int(input("Enter number of students: "))
for i in range(noStudent):
    marks = int(input("Enter marks of student " + str(i+1) + ": "))
    marksInFDS.append(marks)

flag = 1
while flag == 1:
    print("/**********MENU********/")
    print("1. The average score of the class")
    print("2. Higher score and lower score of the class")
    print("3. Count of students who were absent for the test")
    print("4. Display marks with higher frequency")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        average(marksInFDS)
    elif choice == 2:
        print("Higher score in the class is: ", Maximum(marksInFDS))
        print("Lowest score in the class is: ", Minimum(marksInFDS))
    elif choice == 3:
        print("Count number of students who are absent: ", absentCnt(marksInFDS))
    elif choice == 4:
        marks, count = maxFrequency(marksInFDS)
        print("Maximum frequency of marks {0} is {1}".format(marks, count))
    elif choice == 5:
        flag = 0
    else:
        print("wrong choice!")
