#Program that plots companies by marketcap by scraping data from a certain website 
#using beautifulsoup library and squarify
#pip install beautifulsoup4(web scraping lib),request, matplotlib, squarify 
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 
import squarify

url='https://companiesmarketcap.com/india/largest-companies-in-india-by-market-cap/'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

rows= soup.findChildren('tr')

symbols = []
market_caps = []
sizes = []

for row in rows:
    try:
        symbol = row.find('div',{'class':'company-code'}).text
        market_cap = row.findAll('td')[2].text
        market_caps.append(market_cap)
        symbols.append(symbol)

        #Trillion and billions balancing

        if market_cap.endswith('T'):
            sizes.append(float(market_cap[1:-2]) *10**12)
        elif market_cap.endswith('B'):
            sizes.append(float(market_cap[1:-2]) *10**9)

    except AttributeError:
        pass


labels=[f'{symbols[i]}\n ({market_caps[i]})' for i in range(len(symbols))]
colors= [plt.cm.Spectral(i/float(len(symbols))) for i in range(len(symbols))]


squarify.plot(sizes=sizes, label=labels, color=colors, bar_kwargs={'linewidth':0.5, 'edgecolor':'#111111'}, text_kwargs={'fontsize':6})

plt.show()