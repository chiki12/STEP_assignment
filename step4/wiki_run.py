import collections
import sys

sys.setrecursionlimit(60000)

def main():
  pages = {}
  links = {}
  
  p = input("small txt(input 1 ) or normal one(input 2)? : ")

  if p=='1':
    file_name ='_small'
  else:
    file_name = ''

  with open('data/pages'+file_name +'.txt') as f:
    #dfs,bfs実装の時にはpagesのこと考えなくても大丈夫です。
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  with open('data/links'+file_name +'.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
    # print(links)

  p = ''
  while p!='no':
    p= input("whose id you want to know?(name or no) : ")
    if p == 'no':
      break
    for k, v in pages.items():
      if v == p:
        print(p,k)
      # elif v == 'Google':
      #   start_node = k
      #   print('Google', k) #k is id of 'Google'
      # elif v == '渋谷' :
      #   target_node = k
      #   print('渋谷', k)
      

  while input('end the program?(yes or no): ')!='yes':
    start_node = input('from(id):')
    target_node = input('to(id):')
  
    p = input('dfs or dfs_recursion or bfs？(please input 1 or 2 or 3): ')

    if p=="1":
      #dfs の実行
      route_dfs_run = dfs_route(start_node,target_node,links)
      route_dfs_name = route_dfs_run
      if route_dfs_run != 'no route found':
        route_dfs_name = [pages[i] for i in route_dfs_run]
      print(route_dfs_name)
    elif p=='2':
      ### dfs recursionの実行
      route_dfs_run = dfs_saiki_route(start_node,target_node,links)
      oute_dfs_name = route_dfs_run
      if route_dfs_run != 'no route found':
        route_dfs_name = [pages[i] for i in route_dfs_run]
      print(route_dfs_name)
    elif p=='3':
      # bfs
      route_bfs_run = bfs_route(start_node,target_node,links)
      route_bfs_name = route_bfs_run
      if route_bfs_run != 'no route found':
        route_bfs_name = [pages[i] for i in route_bfs_run]
      print(route_bfs_name)
    else:
      print('wrong input')

######################
######################
######## dfs #########

# see if there is any route existed from start node to target node
def dfs(start,target,node):
  container = collections.deque()
  container.append(start)
  global check
  check = {}
  check[start]= True

  # while container is not empty
  while container:
    v = container.pop()
    if v == target:
      return True
    elif v in node:
      for follow in node[v]:
        if not check.get(follow):
          check[follow] = v
          container.append(follow)
  return False

def dfs_route(start,target,node):
  global check
  check = {} #checkを初期化する
  if dfs(start,target,node):#dfsの関数が実行すると同時にcheck辞書も焼き込まれてる
    # print(check)
    route_dfs_adjt = [] #put the route node into this list
    index = target  #targetから探索します
    while index != start:
      route_dfs_adjt.append(index)
      index = check[index]
    route_dfs_adjt.append(index) #startnodeもリストに追加
    route_dfs_adjt.reverse() #逆順にする
    return route_dfs_adjt
  return 'no route found'

########### dfs #########
#########################
#########################


######################
######################
######## dfs回帰版 ###
route_dfs = []
def dfs_saiki(start,target,node,clist): #clistに入ってるものは探索済みのもの
  # print(start)
  global route_dfs
  if start == target:
    # route.append(start)
    return True
  else:
    #＿＿ node_follow = node.copy()
    #＿＿ node_follow[start]={} #nodeからfollowの要素を空にしたdict
    if start in node:
      for follow in node[start]:
        #＿＿ dfs_saiki(follow,target,node_follow))
        if not clist.get(follow): 
          clist[follow] = True
          if dfs_saiki(follow,target,node,clist):
            route_dfs.append(follow)
            # 再帰だからfollowは逆順に出てくる
            return True
  return False


def dfs_saiki_route(start,target,node):
  global route_dfs
  route_dfs=[]
  check_list ={}
  check_list[start]= True
  if not dfs_saiki(start,target,node,check_list):
    return 'no route found'
  route_dfs.append(start)
  route_dfs.reverse()
  return route_dfs

########### dfs回帰版 ###
#########################
#########################
    

#########################
#########################
############ bfs ########

def bfs(start,target,node):
  container = collections.deque()
  # print(container)
  container.append(start)
  check = {}
  check[start]= True
  global route_bfs 

  # while container is not empty
  while container:
    v = container.popleft()
    if v == target:
      return True
    elif v in node:
      for follow in node[v]:
        if not check.get(follow):
          check[follow] = True
          route_bfs[follow] = v
          container.append(follow)
  return False

def bfs_route(start,target,node):
  global route_bfs
  route_bfs = {}
  if bfs(start,target,node):
    # print(route_bfs)
    route_bfs_adjt = []
    index = target
    while index != start:
      route_bfs_adjt.append(index)
      index = route_bfs[index]
    route_bfs_adjt.append(index)
    route_bfs_adjt.reverse()
    return route_bfs_adjt
  return 'no route found'

############ bfs ########
#########################
#########################

def test_1():
  test_list ={}
  test_list[1]={2,5}
  test_list[2]={4}
  test_list[3]={5}
  test_list[4]={2,3}
  test_list[5]={1,2,3}
  for i in range(1,6):
    for j in range(1,6):
      # print("dfs result of {} to {} is {}".format(i,j,bfs(j,i,test_list)))
      # print("the route from {} to {} is {}".format(i,j,bfs_route(i,j,test_list)))
      # print("dfs result of {} to {} is {}(original) and {}(saiki)"
      # .format(i,j,dfs(j,i,test_list),dfs_saiki(j,i,test_list,{})))
      # print("the route from {} to {} is {}".format(i,j,dfs_saiki_route(i,j,test_list)))
      print("dfs result of {} to {} is {} and route is {}"
      .format(i,j,dfs(i,j,test_list),dfs_route(i,j,test_list)))
      
def test_2():
  test_list = {}
  test_list['1']={'2'}
  test_list['2']={'3'}
  test_list['3']={'4'}
  test_list['4']={'5'}
  test_list['5']={}
  for i in test_list:
    for j in test_list:
      print("the route from {} to {} is {}".format(i,j,dfs_saiki_route(i,j,test_list)))
      # print("the route from {} to {} is{} and is {}".format(i,j,bfs(i,j,test_list),bfs_route(i,j,test_list)))

if __name__ == '__main__':
  main()
  # test_1()
  # test_2()