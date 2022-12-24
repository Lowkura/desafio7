from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import math

options = Options()
options.add_argument('windowns-size=400,800')

url_base = 'https://br.indeed.com/jobs?'


def search_indeed(keyword):
  #cria urls (usando o range)
  urls = []

  for n_page in range(20):
    url = f"{url_base}q={keyword}&start={n_page * 10}&sort=date"
    urls.append(url)


    #envia as urls para scrapping
  return scrapping_indeed (urls,keyword)

def scrapping_indeed(urls,keyword):
  all_jobs = []
  contador=0
  #para cada url recebina faça:
  for url in urls:
    print('-----------------------------')
    print("começando uma url...")

    #Erro 403
    #header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    #Alterando módulo para cfscrape
    time.sleep(1)
    browser = webdriver.Chrome(options=options)
    time.sleep(1)
    browser.get(url)

    time.sleep(5)
    #faz a sopa
    html_indeed = BeautifulSoup(browser.page_source, 'html.parser')

    cards = html_indeed.find_all('div', attrs={'class':'job_seen_beacon'})

    for card in cards:
        job={}

        title_job = card.find('a', attrs={'class':'jcs-JobTitle'})
        title_job=title_job.text



        if bool(card.find('span', attrs={'class':'companyName'}))==True:
            company = card.find('span', attrs={'class':'companyName'})
            company=company.text

        else:
            company = "Não encontrada"



        if bool(card.find('div', attrs={'class':'companyLocation'}))==True:
            location = card.find('div', attrs={'class':'companyLocation'})
            location=location.text

        else:
            location = "Não encontrada"



        if bool(card.find('span', attrs={'class':'date'}))==True:
            how_old = card.find('span', attrs={'class':'date'})
            how_old=how_old.text

        else:
            how_old = "Não encontrada"



        if bool(card.find('a').get('data-jk'))==True:
            link = card.find('a').get('data-jk')
            link = f"{url_base}q={keyword}&l=&vjk={link}"

        else:
            link = "Não encontrada"



        job = {
          'title':title_job,
          'company': company,
          'location': location,
          'how_old': how_old,
          'link': link
        }
         #add o job na lista all_jobs
        all_jobs.append(job)
        #retorna a lista com todos os jobs
        #return all_jobs
        contador=contador+1

  print(contador)
    #retorna a lista com todos os jobs

  return all_jobs

    #url + request
    #r_indeed = browser.get('https://br.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=c1bff9b1b6a00771')
    #print(r_indeed.status_code)
    #salva o html no html_indeed
    #html_indeed = r_indeed.text

    #soup = BeautifulSoup(html_indeed, 'html.parser')

    #print(cards)

    #filtrar os card. criar lista de cards
    #cards = soup.find_all('div', class_="result")
    #for card in cards:
      #monta o job
      #print(card)
      #company = card.find('span', class_='companyName')
      #if company == None:
        #company = "Não encontrada"
      #else:
        #company = company.get_text().strip()
      #job = {
        #'title': card.find('a').find('span').get('title'),
        #'company': company,
        #'location': card.find('div', class_='companyLocation').string,
        #'how_old': card.find('span', class_='date').get_text(),
        #'link': f"https://br.indeed.com{card.find('a').get('href')}"
      #}
       #add o job na lista all_jobs
      #all_jobs.append(job)
  #retorna a lista com todos os jobs
  #return all_jobs
