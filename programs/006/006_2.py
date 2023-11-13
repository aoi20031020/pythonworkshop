import requests

#httpリクエストを送りたいリンク
#コピペするとリンク壊れる
url ='https://www.chuo-u.ac.jp/'

#アクセスして返答データを取得
#サイトなどの規約をしっかり読み自己責任で！！
response = requests.get(url)

#htmlテキストを表示
print(response.text)