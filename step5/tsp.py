# ここで大体どんなもの書きたいかの概略を書く
# 入力：　＝＞　入力の関数
# 入力の順番で都市をラベル付け、位置を入力する、入力ごとに距離を計算してリストに入れた方がいいかも（メモリ量大変そうけど）　
# 　＝＞　距離を計算する関数
# 始点は何でしょう？？？？　とりあえず０にする
# 未探索リストから距離が一番近い点を選びルートを作る　　＝＞　リストから距離が一番小さいvertexを探す関数を作る
# 探索済みリストと未探索のリストを作って、探索済みになったら探索済みリストに追加で、未探索リストから消す
# ルートのリスト　→ 無向 ->　ルート変更の時に二つのvertexの間のvertexを逆にしたら大丈夫なので無方向グラフもいらない
# ルートの見直し：ルートが互いに交わってるものがあったら変更する　→　交わってるかを判断する関数が必要　＝＞　何ならルートの表からまだ決めてない
# 交わってるなら始点と始点、終点と終点をつなぐ　（方向付きリストだとルートの順番も考えなきゃ）　＝＞　ルートを変える変数（引数は多分ルートのリストと交換する必要があるルート）
# 出力の関数
import math
from numpy import true_divide
def main():
    filename=input('enter the filename you want to use: ')
    cities = read_input('./input_'+filename+'.csv')
    vertex_list = create_vertexlist(cities)
    vertex_list = check_and_change(cities,vertex_list)
    output(vertex_list,'./output_'+filename+'.csv')
    print(route_length(cities,vertex_list))



def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities



def output(list,filename):
    with open(filename,'w') as w:
        print('index',file =w)
        for i in list:
            print(i,file =w)


def distance(v1,v2):
    dist =(v1[0]-v2[0])*(v1[0]-v2[0])+(v1[1]-v2[1])*(v1[1]-v2[1])

    return math.sqrt(dist)
        
def neighborhood(cities,start_vertex,list):
    min = float('inf')
    for i in list:
        d = distance(cities[start_vertex],cities[i])
        if d<min:
            min = d
            vertex = i
    return vertex

def create_vertexlist(cities):
    index = 0
    explored_vertex = []
    unexplore_vertex= [i for i in range(len(cities))]
    unexplore_vertex.remove(index)
    explored_vertex.append(index)
    while unexplore_vertex:
        next_index =  neighborhood(cities,index,unexplore_vertex)
        index = next_index
        unexplore_vertex.remove(index)
        explored_vertex.append(index)
    return explored_vertex


"""
def create_route(cities):
    index = 0
    route_list =[[-1]for _ in cities]
    explored_vertex = []
    unexplore_vertex= [i for i in range(len(cities))]
    unexplore_vertex.remove(index)
    explored_vertex.append(index)
    while unexplore_vertex:
        next_index =  neighborhood(cities,index,unexplore_vertex)
        route_list[index].append(next_index)
        route_list[next_index].append(index)
        index = next_index
        unexplore_vertex.remove(index)
        explored_vertex.append(index)
    route_list[index].append(0)
    route_list[0].append(index)
    for i in route_list:
        i.remove(-1)
    return route_list 
"""

#  [0,1,2,3,4]  => [(0,1),(1,2),(2,3),(3,4),(4,0)]
def create_routelist(vertex_list):
    route_list = []
    for i in range(len(vertex_list)-1):
        route_list.append((vertex_list[i],vertex_list[i+1]))
    route_list.append((vertex_list[i+1],0))
    return route_list

def crossed(cities,route1,route2):
    (x1,y1) = cities[route1[0]]
    (x2,y2) = cities[route1[1]]
    (x3,y3) = cities[route2[0]]
    (x4,y4) = cities[route2[1]]
    
    a = x2-x1
    b = y2-y1
    c = x4-x3
    d = y4-y3
    if (a*(y3-y2)-b*(x3-x2))*(a*(y4-y2)-b*(x4-x2))<=0 and (c*(y1-y4)-d*(x1-x4))*(c*(y2-y4)-d*(x2-x4))<=0 :
        return True
    else:
        return False

def route_crossed(cities,vertex_list):
    route_list = create_routelist(vertex_list)
    for i in range(len(route_list)):
        for j in range(i+2,len(route_list)):
            if crossed(cities,route_list[i],route_list[j]) == True:
                # print(route_list[i],route_list[j])
                return True
    return False

def change(route1, route2, vertex_list):
    (v1,v2) = route1
    (v3,v4) = route2
    
    for i in range(len(vertex_list)):
        if vertex_list[i]==v2: 
            i1=i
        if vertex_list[i] == v3:
            i2=i
    list = vertex_list[i1:i2+1]
    list.reverse()
    vertex_list = vertex_list[:i1]+list+ vertex_list[i2+1:]
    return vertex_list 


def route_change(cities,vertex_list):
    if route_crossed(cities,vertex_list)==False:
        return 'ERROR'
    route_list = create_routelist(vertex_list)
    for i in range(len(route_list)):
        for j in range(i+1,len(route_list)):
            if crossed(cities,route_list[i],route_list[j]) == True:
                return change(route_list[i],route_list[j],vertex_list)
    return vertex_list
        
def check_and_change(cities,vertex_list):
    list = vertex_list
    while route_crossed(cities,list): 
        list = route_change(cities,list)
        # print(route_change(cities,vertex_list))
    return list

def route_length(cities,vertex_list):
    dist = 0
    for i in range(len(vertex_list)-1):
        v1 = vertex_list[i]
        v2 = vertex_list[i+1]
        dist += distance(cities[v1],cities[v2])
    dist += distance(cities[v2],cities[0])
    return dist

'''
def vertexlist(route_list):
    index = 0
    vertexlist=[0]
    next_index = 1 #not 0 is ok
    checked_index = []
    while next_index != 0 :
    # for i in range(len(route_list)):
        if route_list[index][0] in vertexlist :  
            if route_list[index][1] in vertexlist :
                break
            else:
                next_index = route_list[index][1]
        else:
            next_index = route_list[index][0]
        vertexlist.append(next_index)
        checked_index.append(next_index)
        index = next_index
    return vertexlist
'''


if __name__ == '__main__':
  main()