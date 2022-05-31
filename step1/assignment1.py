#finding the anagram of the word in the file

##########　先生コメント
#メイン関数などを入れるといい


# input the name of the word file
fileName = input("anagramのファイル名を入力してください（txtなし）")

# make the new dictionary
def makeDictionary(dictionary):
    ##########　先生コメント
    # new_dictionary = [(sorted(word),word) for word in dictionary]
    new_dictionary = []
    #sort the word in the dictionary
    for word in dictionary:
        new_dictionary.append((sorted(word),word))
        # if new_dictionary[-1][0][0]
    #sort the new list with the first factor
    new_dictionary.sort(key=lambda x:x[0])
    return new_dictionary

#open the words file
with open("./words.txt") as f:
    ##########　先生コメント
    # 入出力周りはわかりにくいかもしれませんが、このときは 'f' にはファイル object が入ってる。
    # 文字列の処理をするには、以下のように各行を取り出すといい。
    # words = [word.strip() for word in f]


    ##########　先生コメント
    # nd, n 等は global 変数になるので、できるだけ避けたほうが conflict 等が起こりにくい
    # global 変数にする際には、変数名を大文字にする等して、conflict を避ける工夫ができる
    
    # nd is the sorted dictionary
    nd = makeDictionary(f)
    n= len(nd)
    #write the sorted dictionary list into new_dictionary.txt
      # with open("new_dictionary.txt",mode= 'w') as fout:
      #     print(makeDictionary(f),file=fout)

    ##########　先生コメント
    # 以下のcloseはwith句がハンドルしてくれるので必要ない
    f.close



#二分探索でanagramを探して、左と右のインデックス(ll,rr)を返す 
# list(ll+1)~(rr-1)はsのanagramに対応する項である

def binary_search(s ,list ):
    # ll,rlは一番leftのindexを求めるための変数
    ll: int = -1
    # rl: int = len(list)
    rl: int = n
    # lr,rrは一番rightのindexを求めるための変数
    lr: int = -1
    # rr: int = len(list)
    rr: int = n
    while rl-ll>1 :
        indexl: int =(ll+rl)//2
        if list[indexl][0]< s :
            ll=indexl
        else:
            rl=indexl
    ######### 先生コメント
    # 探索空間は ll よりも右になるので、lr を ll の値にして始めてもいいかもしれません。
    while rr-lr>1 :
        indexr: int =(lr+rr)//2
        if list[indexr][0]<= s :
            lr=indexr
        else:
            rr=indexr
    return (ll,rr)


# find the (random_word)'s anagram in the given list
# if no anagram return"no_anagram
# else return the list of the anagram of the give word
def better_solution(random_word):
    (x,y) = binary_search(sorted(random_word), nd )
    if y-x==1 :
      return "no_anagram"
    else :
      l=[np[i][1] for i in range(x+1,y)]
    #   for i in range(x+1,y):
    #     l.append(nd[i][1])
      return l




with open(fileName+".txt") as l:
    for word in l:
        print(better_solution(word))
        # with open("anagram.txt",mode='w') as fo:
        #    print(better_solution(word),file="fo")


