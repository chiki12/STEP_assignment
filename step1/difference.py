filename = input("what file do you want to use(without .txt")
testfile_1 = filename + "_answer.txt"
testfile_2 = filename + "_answer1.txt"

X = [1,3,2,2,1,3,3,1,1,4,4,2,2,1,1,3,4,1,1,1,2,3,3,4,3,4]

# string => int
def score(w):#w: string
    count = 0
    for i in w:
        n = ord(i)-ord('a')
        if n>=0 and n<26:
            count += n
    return count

with open(testfile_1) as f1, open (testfile_2) as f2:
    list1 = [word.split() for word in f1]
    list2 = [word.split() for word in f2]
    for i in range(len(list1)):
        if score(list1[i])!=score(list2[i]):
            print(i,list1[i],score(list1[i]),list2[i],score(list2[i]))