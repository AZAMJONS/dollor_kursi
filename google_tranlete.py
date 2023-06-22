# import requests

# matn = str(input("Iltimos kerakli sozni kriting: "))

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# payload = {
# 	"q": f"{matn}",
# 	"target": "uz",
# 	"source": "en"
# }
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "b9a3481076msh7814fd8e8cfa382p1e5c44jsn6b2e2e99a31f",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

# response = requests.post(url, data=payload, headers=headers)

# natija = response.json() ['data']['translations'][0]['translatedText']
# print(natija)

# import requests

# url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/UZ/"

# headers = {
# 	"X-RapidAPI-Key": "b9a3481076msh7814fd8e8cfa382p1e5c44jsn6b2e2e99a31f",
# 	"X-RapidAPI-Host": "coronavirus-smartable.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# total_deaths = response.json()['stats']['totalDeaths']
# total_conf_cases = response.json()['stats']['totalConfirmedCases']
# total_rec_cases = response.json()['stats']['totalRecoveredCases']
# print("Ozbekistonda zaralanganlar soni: ",total_conf_cases)
# print("Ozbekistonda vafot etganlar soni: ",total_deaths)
# print("Ozbekistonda kasallanganlar soni: ",total_rec_cases)


# while True:
# 	import requests

# 	savol = str(input("Please enter your question: "))

# 	url = "https://chatgpt-open-ai-nlp.p.rapidapi.com/"

# 	payload = {
# 		"prompt": f"{savol}",
# 		"temperature": "0.7"
# 	}
# 	headers = {
# 		"content-type": "application/json",
# 		"Type": "chatgpt4",
# 		"X-RapidAPI-Key": "b9a3481076msh7814fd8e8cfa382p1e5c44jsn6b2e2e99a31f",
# 		"X-RapidAPI-Host": "chatgpt-open-ai-nlp.p.rapidapi.com"
# 	}

# 	response = requests.post(url, json=payload, headers=headers)

# 	javob = response.json()['answer']

# 	print(javob)


# from bs4 import BeautifulSoup
# import requests


# DOLLOR_UZS_LINK = 'https://www.google.com/search?q=usd+uzs&oq=usd+uzs&aqs=chrome.0.0i131i433i512j0i512l9.1032788695j0j15&sourceid=chrome&ie=UTF-8'
# my_user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# full_page = requests.get(DOLLOR_UZS_LINK, headers=my_user_agent)
# qirqib_olish = BeautifulSoup(full_page.content,'html.parser')

# natija = qirqib_olish.findAll('span',{'class':'DFlfde SwHCTb',"data-precision":2})
# print(f"Bugungi kunda 1 AQSH dollori {natija[0].text}somga teng")

# from bs4 import BeautifulSoup
# import requests


# WORLD_AHOLISI_LINK= 'https://www.worldometers.info/world-population/uzbekistan-population/'
# my_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# full_pages = requests.get(WORLD_AHOLISI_LINK,headers=my_agent)
# qirqib_olaman = BeautifulSoup(full_pages.content,'html.parser')

# natijam = qirqib_olaman.findAll('span', {'class': 'rts-counter'})
# print(f"Bugungi kunda Ozbekiston aholisi {natijam[0].text}odmani tashkil etadi")

# uyga vazifa toshkent uch kunlik ob_havo

from bs4 import BeautifulSoup
import requests


TOSHKENT_3_KUNLIK_OB_HAVO_LINK = 'https://www.accuweather.com/uz/uz/tashkent/351199/daily-weather-forecast/351199'
my_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

full_page = requests.get(TOSHKENT_3_KUNLIK_OB_HAVO_LINK,headers=my_agent)
qirqib_olmoqchiman = BeautifulSoup(full_page.content,'html.parser')

ishlatilish = qirqib_olmoqchiman.findAll('span',{'class':'high'})
ishlatilishi = qirqib_olmoqchiman.findAll('span',{'class':'high'})
ishlataman = qirqib_olmoqchiman.findAll('span',{'class':'high'})

sana1 = qirqib_olmoqchiman.findAll('span',{'class':'module-header sub date'})
sana2 = qirqib_olmoqchiman.findAll('span',{'class':'module-header sub date'})
sana3 = qirqib_olmoqchiman.findAll('span',{'class':'module-header sub date'})

print(f'Toshkent shahrida {sana1[0].text} kuni havo harorati {ishlatilish[0].text} boladishi kutilmoqda')
print(f'Toshkent shahrida {sana2[1].text} kuni havo harorati {ishlatilishi[1].text} boladishi kutilmoqda')
print(f'Toshkent shahrida {sana3[2].text} kuni havo harorati {ishlataman[2].text} boladishi kutilmoqda')    