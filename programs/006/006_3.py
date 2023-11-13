import requests
import json
import matplotlib.pyplot as plt
#↑追加する

#httpリクエストを送りたいリンク
url ='https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m&start_date=2023-07-08&end_date=2023-07-08'
#アクセスして返答データを取得
#サイトなどの規約をしっかり読み自己責任で！！
response = requests.get(url)
weather = response.json()
weather = weather["hourly"] #時間と気温を抽出
time = weather["time"] #時間を抽出
temp = weather["temperature_2m"] #気温を抽出（グラフの縦軸）
x = range(len(time)) #時間の要素数（グラフの横軸になる）

plt.plot(x, temp) #折れ線グラフを作成
plt.xticks(x, time) #横軸のラベルにtimeを
plt.show() #グラフ表示