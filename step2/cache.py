from contextlib import nullcontext
from re import X
import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.
class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    self.n_ = n
    #### comment by teacher
    #  dicなどの一般的な名前よりは、このdictには何が入っているかを表す名前を使った方が読みやすくなる
    # 今回の場合は、self.url_to_cache_data
    # self.old self.newも同様です    oldest_url,newest_urlの方が何が入っているのが分かりやすい
    self.dic = {}
    self.old = '' # キャッシュの一番古いサイトを記憶する変数
    self.new = '' # キャッシュの一番新しいサイトを記憶する変数

    # これは出題者が書いた placeholder なので、消してください。pass は、関数などの code block が何もしない時に使います。
    # pass

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL

  #### comment by teacher
  # このようなコメントを書いておくのはいいですね。
  # おそらく self.dic に関するコメントだと思うので、
  # その変数を定義している場所 (__init__ 関数) に書いておくといいでしょう。

  #　変数を定義している場所の中身の説明のコメントを書くといい
  # 辞書の中身 key = url, value = [contentes, older_url, newer_url]
  def access_page(self, url, contents):
    # 存在する時
    if url in self.dic:
      #### ocmment by teacher
      # Python ではインデントでブロックを表すので
      # 、インデントする文字数は固定してください
      # 。他の場所では2文字でインデントしているので
      # 、この下の if 句も2文字でインデントしてください。

     if url != self.new:
      #  connect between the before url.newer and older
       if url != self.old:


         # インデックスで要素をアクセスすると、そのインデックスが指すものが分かりにくくなります。簡単なデータクラスを作ってあげると、読みやすくなると思います。例えば、
        # class CacheData(object):  //objectはなんだろう //継続するもの
        #   def __init__(self, contents, older_url, newer_url):
        #.    self.contents = contents
        #.    self.older_url = older_url
        #     self.newer_url = newer_url
        #
        #. target_data = self.dic[url]　　
        #. self.dic[target_data.older_url].newer_url = target_data.newer_url
        #
        # もしくは、dict を使ってもいいかもしれません。


        self.dic[self.dic[url][1]][2] = self.dic[url][2]
       else:
        self.old = self.dic[url][2]
       self.dic[self.dic[url][2]][1] = self.dic[url][1]
      #  make url the newest

      # いくつか共通の処理があるので、それらはまとめてif句のそとに出してもいいかもしれません

       self.dic[self.new][2] = url
       self.dic[url][1] = self.new
       self.dic[url][2] = ''
       self.new = url
      
    # 存在しない時
    else :
      if len(self.dic)<self.n_:
        if len(self.dic)==0 :

          # dict の要素追加は、self.dic[url] = [contents, '', ''] としても良いです。
          self.dic.update({url:[contents, '', '']})
          self.old = url
          self.new = url
        else:
          self.dic[self.new][2]=url
          self.dic.update({url : [contents, self.new , ''] })
        # self.dic[url][1] = self.new
        self.new = url
      else:
        # delete the oldest from the dictionary
        self.old = self.dic[self.old][2]
        self.dic.pop(self.dic[self.old][1])
        self.dic[self.old][1]=''
        # make url the newest
        self.dic.update({url : [contents, self.new, '']})
        self.dic[self.new][2] = url
        self.new = url
    

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    page = []
    u = self.new
    while u!='' :
        page.append(u)
        u= self.dic[u][1]
    return page
    


# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "f.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "f.com", "a.com", "c.com"])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "e.com", "f.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "e.com", "f.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)

if __name__ == "__main__":
  cache_test()
