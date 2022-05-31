#! /usr/bin/python3

def read_number(line, index):
  number = 0
  ########### while 文をまとめられるといいですね。
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    decimal = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * decimal
      decimal /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def read_plus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def read_minus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1


def read_times(line, index):
  token = {'type': 'TIMES'}
  return token, index + 1



def read_divide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1

def read_open_p(line, index):
  token = {'type': 'OPENP'}
  return token, index + 1

def read_close_p(line, index):
  ######### ”と’どちらに統一した方がいい
  token = {"type": 'CLOSEP'}
  return token, index + 1

######### 関数の間のempty lineの数は統一した方が綺麗に見える
def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = read_number(line, index)
    elif line[index] == '+':
      (token, index) = read_plus(line, index)
    elif line[index] == '-':
      (token, index) = read_minus(line, index)
    elif line[index] == '*':
      (token, index) = read_times(line, index)
    elif line[index] == "/":
      (token, index) = read_divide(line, index)
    elif line[index] == "(":
      (token, index) = read_open_p(line, index)
    elif line[index] == ")":
      (token, index) = read_close_p(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


############################
######   以下は変更部分　#####
############################


def take_p(tokens):
  plist = []
  pcount = 0
  index = 0
  store = 0 ###storeはif句のなかでのみ使っているので、ここで宣言しなくてもいい
  # 使う場所で宣言する方が変数の名前が被るなどの間違いが減らせます

  while index < len(tokens):
    if tokens[index]['type'] == "OPENP":
      plist.append(index)
      pcount += 1
    if tokens[index]['type'] == "CLOSEP":
      pcount -= 1
      # print(plist,pcount)
      ###########
      # Open parenthesis を stack に入れるのはいい工夫ですね。
      # また、Python の list は pop メソッドがあるので、
      # 以下の二行は次のように書くといいでしょう。
      # 最後の要素にのみ注目すればいいので、pcount はこの場合必要ありません。
      ###########
      open_p_index = plist[pcount]
      del plist[pcount]
      store = evaluate(tokens[open_p_index+1:index])
      del tokens[open_p_index+1:index+1]
      tokens[open_p_index]= {'type': 'NUMBER', 'number': store}
      index = open_p_index +1    ####　!!!!!!!!!ここ大事
    else: index +=1
  return tokens





##############################
######## 以上です ##############
##############################


# 宿題1 
# 前の数字を記憶する変数が必要　=> store
# ＊/と会ったら、計算してtokens[index][number]にする
def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  store = 0
  # clear（）
  #########
  # times/divide と plus/minus を分けて処理しているのはいいと思います。これらはまとまったブロックなので、
  # それぞれ別の関数に分けてあげるといいと思います。
  #########
  # # at first cycle, clear * and /
  while index < len(tokens):
    if tokens[index]['type'] == "TIMES":
      store = tokens[index-1]['number']*tokens[index+1]['number']
      tokens[index-1]={'type': 'NUMBER', 'number': store}
      del tokens[index:index+2]
    elif tokens[index]['type'] == "DIVIDE":
      store = tokens[index-1]['number']/tokens[index+1]['number']
      tokens[index-1]={'type': 'NUMBER', 'number': store}
      del tokens[index:index+2]
    else :
      index += 1 
  index = 1 #first index at the second cycle
  # do while at second cycle
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer



def test(line):
  tokens = tokenize(line)
  tokens = take_p(tokens)  ##################　tokensを(,)のフィルターを通す
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
###########
# テストする場合には、
# 1: 単純なテストで単体の機能がカバーされているか、
# 2: 複雑なケース、エッジケースがカバーされているか、
# を確認するといいでしょう。
# 今回の場合には、
# 1.1 等の小数点つきの数
# -*/ の単純なケース (数が2つ)
# マイナスのハンドリング ("-1", "3*-2", etc)
# 等を追加するといいかと思います。
# できるだけ systematic に追加してやると、テストとしての網羅性が確認できるので、尚いいと思います。
############
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("1+1*1+2*8/4+4/2-1")
  test("0.4/1*2/1/2/1")
  test("1*2*3/4/5+1")
  test("((1+2)/3+1)+2*7")
  test("(1-2+5/1.0)*((4+4)*6)")
  test("(1.0+2.3)*(3.1-1.1)/((2.4+0)*1+2)")
  print("==== Test finished! ====\n")

run_test()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
