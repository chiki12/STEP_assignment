# Travelling Salesman Problem

## greedy algorithm で基本のルートを作って、交わってるルートが存在すれば頂点を交換するという方針でコードを書きました。

### 使った関数

-  read_input(filename) ファイル入力用
-  output(list,filename)　ファイル出力用

-  distance(v1,v2)　二つの座標の距離を求める
        
-  neighborhood(cities,start_vertex,list)　listのなかにstart_vertexと一番近い点を求める

-  create_vertexlist(cities)　ルート（頂点からなるリスト）を生成する　（greedy algorism）

- create_routelist(vertex_list)　エッジのリストを頂点のリストのもとで生成する

- crossed(cities,route1,route2)　二つのエッジが交わってるかどうかを判定する

- route_crossed(cities,vertex_list)　ルートのなかに交わってるエッジが存在するか判定する

- change(route1, route2, vertex_list)　交わってる二つのエッジを変える

- route_change(cities,vertex_list)　一番最初に見つけた二つ交わってるエッジを変えてからのルート
        
- check_and_change(cities,vertex_list)　交わってるエッジが全てなくなるようなルート

- route_length(cities,vertex_list)　ルートの距離を求める

### 感想
最初の時に無向グラフをどう表したら手間かからないか結構考えてましたが、vertexのリストのために何個か例を紙で書いてみたら、vertexのリストだけで済ませることに気付きました。
関数を割と細かく書いたら、頭がはっきりして、エラーも関数ごとにチェックすることができるので、デバッグは順調でしたが、全てコードを書き終わって振り替えてみたら、関数が多すぎではないかと思い始めました。

### how much better can I do?

greedy algorithm のとこで、一番近い点を選ぶのではなく、一番近い点から一番外側の点を選んだらどうなるかなと思いました。（すみませんが実装はしてません）
