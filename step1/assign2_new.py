from operator import truediv

# medium, largeの点数がちょっとおかしい

SCORE = [1,3,2,2,1,3,3,1,1,4,4,2,2,1,1,3,4,1,1,1,2,3,3,4,3,4]

# string => int
def score(w):#w: string
    count = 0
    for i in w:
        n = ord(i)-ord('a')
        if n>=0 and n<26:
            count += SCORE[n]
    return count

# make the score list of dictionary
# list[] => list[][]
def score_list(l):
    l1 =[(word,score(word)) for word in l]
    l1.sort(key=lambda x:x[1],reverse= True)
    return l1

# string => list[26]
def alpha_count(w):
    c = [0]*26
    for i in w:
     if ord(i)-97>=0 and ord(i)-97<26:
      c[ord(i)-97]+=1
    return c

# string,string => Boolean
# check whether the word(w) is the anagram of given word(given_w)
def check(given_w,w):
    given_wc = alpha_count(given_w)
    wc = alpha_count(w)
    for i in range(26):
        if given_wc[i] < wc[i]:
            return False
    return True

#  (string,二次元リスト） => string
def anagram2(w,l):
    ws = score(w) #int : the score of w
    for x in l:
        if check(w,x[0]):
            return x[0]


def main():
    file_name = input("ファイル名を入力してください（txtなし）")
    test_filename = file_name + ".txt"
    answer_filename = file_name + "_answer1.txt"

    with open("words.txt") as f :
        dictionary = [word.strip() for word in f]
    dictionary_with_score = score_list(dictionary)
    
    with open(test_filename) as testfile, open(answer_filename,'w') as fout :
        for word in testfile:
            answer = anagram2(word,dictionary_with_score)
            fout.write(f'{answer}\n')

main()