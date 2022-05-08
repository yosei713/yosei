#!/usr/bin/env python
# coding: utf-8

# # APIとは
# Application Programming Interfaceの略。ソフトウェアからOSの機能を利用するための仕様またはインターフェースの総称で、アプリケーションの開発を容易にするためのソフトウェア資源のことをいう。「API」の重要な役割は、サービス提供者が公式に仕様を定義・管理している操作方法（インターフェース）を提供することである。 <br> 
# ## News API 演習
# 以下のコードを用いて記事を収集した。
# >!pip install -q newsapi-python  
# from newsapi import NewsApiClient  
# from pprint import pprint  
# api = NewsApiClient(api_key='912be33b20954296a300d65553920616')  
# top_headlines = api.get_top_headlines(q='アメリカ', language=None, country='jp')  
# pprint(top_headlines)  
# 
# 結果は以下の通りだった<br><br>
# {'articles': [{'author': None,
#                'content': None,
#                'description': 'ツイッター社の買収に向け、マスク氏がさらに一歩前進。アメリカ電気自動車大手「テスラ」のイーロン・マスクCEOが、ツイッター社の買収に向け、71億3,900万ドル、日本円でおよそ9,300億円を調達することが明らかになった。アメリカの証券取引委員会が公表した4日付の資料によると、ソフトウエア大手「オラクル」の共同創...',
#                'publishedAt': '2022-05-07T02:10:17Z',
#                'source': {'id': None, 'name': 'YouTube'},
#                'title': 'イーロン・マスク氏が買収費用9300億円調達 ツイッター社 暫定CEO就任へ - FNNプライムオンライン',
#                'url': 'https://www.youtube.com/watch?v=ghY0nzkUyu0',
#                'urlToImage': 'https://i.ytimg.com/vi/ghY0nzkUyu0/maxresdefault.jpg'}],
#  'status': 'ok',
#  'totalResults': 1}<br><br>
#  News APiにおいては言語日本語がなく、国からのみしか指定ができないと分かった。  
#  # webスクレイピング
#  インターネット上のデータから余分な情報を削り、抽出し、解析・加工処理を施し、新たな情報を生成すること。
#  
#  今回用いたコードは以下のもの
# ```
# from time import sleep
# 
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# 
# url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'
# 
# d_list = []
# for i in range(1,3):
#     print('d_listの大きさ：', len(d_list))
#     
#     target_url = url.format(i)
#     
#     print(target_url)
#     
#     r = requests.get(target_url)
#     
#     sleep(1)
# 
#     soup = BeautifulSoup(r.text)
# 
#     contents = soup.find_all('div', class_='cassetteitem')
# 
#     for content in contents:
#         
#         detail = content.find('div', class_='cassetteitem_content')
#         table = content.find('table', class_='cassetteitem_other')
# 
#         title = detail.find('div', class_='cassetteitem_content-title').text
#         address = detail.find('li', class_='cassetteitem_detail-col1').text
#         access = detail.find('li', class_='cassetteitem_detail-col2').text
#         age = detail.find('li', class_='cassetteitem_detail-col3').text
#         
#         tr_tags = table.find_all('tr', class_='js-cassette_link')
# 
#         for tr_tag in tr_tags:
#             
#             floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]
# 
#             fee, management_fee = price.find_all('li')
#             deposit, gratuity = first_fee.find_all('li')
#             madori, menseki = capacity.find_all('li')
#             
#             d = {
#               'title': title,
#               'address': address,
#               'access': access,
#               'age': age,
#               'floor': floor.text,
#               'fee': fee.text,
#               'management_fee': management_fee.text,
#               'deposit': deposit.text,
#               'gratuity': gratuity.text,
#               'madori': madori.text,
#               'menseki': menseki.text
#             }
# 
#             d_list.append(d)```
#            
#            
#            結果は以下の通りだった  
#            d_listの大きさ： 0
# https://suumo.jp/chintai/tokyo/sc_shinjuku/?page=1  
# d_listの大きさ： 147
# https://suumo.jp/chintai/tokyo/sc_shinjuku/?page=2

# In[ ]:




