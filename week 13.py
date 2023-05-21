import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.billboard.com/charts/hot-100',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('.o-chart-results-list-row')

for song in songs:
    rank = songs.select_one('.o-chart-results-list_item > .a-front-primary-bold-1').text.strip()
    songs_info = song.select_one('.o-chart-results-list_item > h3')
title = song_info.text.strip()
singer = songs_info.parent.select_one('span').text.strip()
print(rank, '/', title, '/', singer)