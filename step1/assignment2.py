
# score付きの辞書を作って、関数名とか注意しながらもう一回コード書きましょう
# global変数とか、ファイルの処理方法などにも注意する　with open() ....



# the common method

# the score of a word
def score(word):
    #######　先生コメント
    # この変数は毎回定義することになるので、コノようなものはscoreに渡すか、
    # global変数として持つ方が効率的
    x = [1,3,2,2,1,3,3,1,1,4,4,2,2,1,1,3,4,1,1,1,2,3,3,4,3,4]
    count = 0
    for i in word:
      if ord(i)-ord('a')>=0 and ord(i)-ord('a')<26:
        count += x[ord(i)-ord('a')]
    return count
        

 

# len>13 => 単語一個ずつチェックする
# name : anagram_over 


# alphabeit count of a word
def count(word):
    c = [0]*26
    for i in word:
     if ord(i)-97>=0 and ord(i)-97<26:
      c[ord(i)-97]+=1
    return c
#######　先生コメント
# 変数名はより具体的にした方がいいかもしれない　check_sub_anagramなど

#check whether the random_word is "belong" to the given word
def check(w, random_word):
    wordc = count(w)
    c = count(random_word)
    check = 1

    for i in range(26) :
        if c[i]>wordc[i] :
            return False
    return True
    # for i in range(26):
    #     if c[i]<=wordc[i]:
    #         check *= 1
    #     else :
    #         return 0
    # return check


#######　先生コメント
# list は Python で使われているので、変数名で使うのは避けてください。
# 事前に list の中身を score が大きい順に sort しておくと
# 、当てはまったものが見つかった際にループから抜けることができるので効率的です。
# また、この score は何回も計算することになるので
# 、list 中にスコアを同時に持っておくといいでしょう。


#found the best anagram of w in the list 
def anagram_over(w,list):
    point = 0
    answer_over = ""
    for word in list:
        if check(w,word):#if word is the anagram of w
            if score(word) > point:
                point = score(word)
                answer_over = word
    return(answer_over,point)
    #スコアが高かったら更新する

# len < 13 => 可能な2^len の列を二分探索で辞書で探す

#checked => ok
def word_create( sorted_word, int):
    l = []
    for i in range(len(sorted_word)):
        if((int >> i)%2):
            l.append(sorted_word[i])
    return l



# make the new dictionary
def makeDictionary(dictionary):
    new_dictionary = []
    #sort the word in the dictionary
    for word in dictionary:
        new_dictionary.append((sorted(word),word))
        # if new_dictionary[-1][0][0]
    #sort the new list with the first factor
    new_dictionary.sort(key=lambda x:x[0])
    return new_dictionary

# binary_search
def binary_search(s ,list ):
    # ll,rlは一番leftのindexを求めるための変数
    ll: int = -1
    # rl: int = len(list)
    rl: int = len(nd)
    # lr,rrは一番rightのindexを求めるための変数
    lr: int = -1
    # rr: int = len(list)
    rr: int = len(nd)
    while(rl-ll>1):
        indexl: int =(ll+rl)//2
        if list[indexl][0]< s :
            ll=indexl
        else:
            rl=indexl
    while(rr-lr>1):
        indexr: int =(lr+rr)//2
        if list[indexr][0]<= s :
            lr=indexr
        else:
            rr=indexr
    return (ll,rr)


def anagram_under(w):
    max = 0
    answer_under=""
    sorted_word = sorted(w)
    n = len(sorted_word)
    for i in range(1,2**n):
      s = word_create(sorted_word,i)
      if score(s)<=max:
            continue
      else:
        (x,y) = binary_search(s,nd)
        if y-x == 1:
            break
        else:
            max = score(s)
            answer_under = nd[x+1][1]
            # 答えがあればいいので全ての可能性を考えなくて良い
            # for j in range(x+1,y):
            #     if score(nd[j][0])>max:
            #         max = score
            #         answer_under = nd[j][1]
    return (answer_under,max)
                    




# 
# 実行コード
# 

file_name = input("ファイル名を入力してください（txtなし）")

wfile = open("./words.txt")
wordfile = wfile.read().split()
tfile = open(file_name + ".txt")
testfile = tfile.read().split()
fout = open(file_name+"_answer.txt",mode = "w")
nd = makeDictionary(wfile)

for w in testfile:
    # if len(w)>=13:
        x,y = anagram_over(w,wordfile)
    # else:
    #     (x,y) = anagram_under(w)
        fout.write(x+"\n")#write the anagram into the answer file


# ######## 先生コメント
# このメイン部分を以下のようにして、24=>26 にすれば動くようになりました。入出力周りは言語によって異なるため、わかりづらかったかもしれません。
# def main():
#   file_name = input("ファイル名を入力してください（txtなし）")

#   with open("./words.txt") as f:
#     wordlist = [word.strip() for word in f]
#   test_filename = file_name + ".txt"
#   answer_filename = file_name+"_answer.txt"

#   with open(test_filename) as testfile, open(answer_filename, 'w') as fout:
#     for word in testfile:
#       answer, answer_score = anagram_over(word,wordlist)
#       fout.write(f'{answer}\n')

# main()