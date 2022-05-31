# Google STEP Class 4 Homework

## 課題内容

### 1. Wikipediaのグラフを使ってなにか面白いことをしてみよう

- 必須："Google"から"渋谷"までをたどる方法をDFSとBFSで探す
- その他なんでも
    - 例：孤立している隠されたページを探す
    - 例：ページランクの高いものを探す

### 2. 他の人の書いたコードを自分の環境で実行してレビューする

- スライド参照

## 準備

[wikipedia_data.zip](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view?usp=sharing) をダウンロードして解凍し、以下のようなディレクトリ構成にしてください。

```
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── .gitignore
├── README.md
└── wiki_run.py
```

## グラフデータ

`data/` に含まれるファイルで、実際に使うものは以下の2つです。

- pages.txt：各ページのidとタイトルのリスト
- links.txt：各リンクのリンク元とリンク先のリスト

以下の3つはテスト用の小さなグラフを表すデータです。

- pages_small.txt
- links_small.txt
- graph_small.png

詳細はスライドを参照してください。

数年前のデータを使っているため、最新の Wikipedia とは異なるリンク構造になっていることに注意してください。

### 実行方法

#### Python

テスト環境: Python 3.9.2

```shell
python3 wiki_run.py
```
と入力してください

次に、
```
small txt(input 1 ) or normal one(input 2)? : 
```
の文が出たら１か２を入力する、１：links_small.txt pages_small.txtを使って実行し、2：links.txt pages.txtを使って実行する

次に以下の文が現れます：

```
whose id you want to know?(name or 'no') : 
```
調べたいidがありましたら調べたい文字列を入力し、なかったらnoを入れる。

次に、
```
end the program?(yes or no): 
```
という文が出ますが、実行を続きたいならyesでプログラムを終了したかったらnoを入れる。

そして、始点のidと終点のidをそれぞれ入力する
```
from(id):
```
```
to(id):
```

始点と終点を入れ終わったら、１か２か３を入力し、使いたい探索方法で実行する。
```
dfs or dfs_recursion or bfs？(please input 1 or 2 or 3): 
```
この後、ルートが書かれているリストが出力される。