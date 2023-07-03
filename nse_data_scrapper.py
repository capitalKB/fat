import requests
from io import BytesIO, StringIO, TextIOWrapper
import json
import zipfile
import csv
import pandas as pd


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': 'nsit=K56TrkXXTpAAXpndqHz79qty; AKA_A2=A; defaultLang=en; ak_bmsc=FE15B0558794E7A82913E7EE7005BC01~000000000000000000000000000000~YAAQh7YRYFHIVRWJAQAAd2g1HBTgxw2IF52o22k8eVJs+SXQvhaQQngE5YU1vERctNi2jNp4tL1l7JyGTDayABQnwcNk0lQ9Bdk/CeZPjc2AfVJmpUfLvS9hBTUPhaxs9nstyvwq22JB839VHCbyfX0CrplaFZtxQ4Ry3M/HjBKbBcNkEduyLMKvCogU3YAsamKC4pJXOZ+t/04wzyLfDWJDdf5ezzXLByoRZr6shUnyFV+3OH7bOC+yNztMna4aSVZA2jAjYaQ1GfpbCIPWMmiNgj5/v1YAXFIQpxu3P4Ou5TJ/wh9f3h76HwZmKaTYqrPxHkf9h9ntfgq/VQ4lJsVCMZJFC9aMBSzt6vDlUKhxfwlFx3njYxvfsD7v475yL6yP1h+TcQ3cG7ZowFYfcJ6H4/OXqXz67mZOdoepVFMJHwXHhhaN7+eQskoLpp7qiFRkBHPt5ETzZe55beaJAGt742CXY4iEiL39bqffUmMSQ5n3LStXRJrvppA=; _gid=GA1.2.186878474.1688395416; nseQuoteSymbols=[{"symbol":null,"identifier":null,"type":"equity"}]; _ga=GA1.1.856782746.1684876562; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY4ODM5NTc0MiwiZXhwIjoxNjg4NDAyOTQyfQ.y0Ujh5h9OIbVEUQ4USRyGm7AQQHuzlkcfIkg0Kk3Daw; _ga_PJSKY6CFJH=GS1.1.1688395409.2.1.1688395769.28.0.0; bm_sv=0AE642657C538BFA9674618C9E7FEA02~YAAQh7YRYAHtVRWJAQAAjeg6HBQX4dLPUzoJ1XhCMp35aj3OBEaGHgYe5U1/O9L6Tsx2T7IpT2Fc8J95G//oLvCV/Ogb8whebXcsWcCJLR2ZU3CDFGbX20ZFs6cLd04qgDhxjdVd9ledUuhEC/UpZPCzwDTcUT9SSxlQ0zThnxI+SvT5SiHXVsL3gkuRLpuJvtXhMbdCfbunrgCXK6hoZjOxmK94nfou+AROYLEPkEPULpG+TttqPh5IawM1e5uvMdl6~1; RT="z=1&dm=nseindia.com&si=764c1cef-fb1d-4f45-879f-6abe6dc6b684&ss=ljmz12gl&sl=b&se=8c&tt=fp9&bcn=%2F%2F684d0d46.akstat.io%2F&ld=7brz&nu=kpaxjfo&cl=83jb"',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

bhav_url = 'https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22CM%20-%20Bhavcopy(csv)%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date=10-Jun-2022&type=equities&mode=single&type=csv'
# response = requests.get(url='https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22CM%20-%20Bhavcopy(csv)%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date=30-Jun-2023&type=equities&mode=single&type=csv', headers=headers)
# response = requests.get(url='https://www.nseindia.com/api/historical/cm/equity?symbol=TCS&series=[%22EQ%22]&from=03-06-2023&to=03-07-2023&csv=true', headers=headers)
# print(response.content)
# data = pd.read_csv(StringIO(response.content.decode('latin-1')))
# data=pd.read_csv(response.content, compression='zip')

resp = requests.get(bhav_url, headers=headers)
resp.raise_for_status()
zfile = zipfile.ZipFile(BytesIO(resp.content))
# I only had one file, so calling zfile.namelist
export_file = pd.read_csv(zfile.open(f'{zfile.namelist()[-1]}'))

print(export_file)

# z = zipfile.ZipFile(BytesIO(response.content))


# from io import StringIO
# import pandas as pd
# s=str(response)

# data = StringIO(s) 
# print(data)
# df=pd.read_csv(data)
# print(df.head())




# df=pd.read_csv(data)
