from selenium import webdriver # importa o webdriver
from selenium.webdriver.common.keys import Keys # importa as teclas
import time # importa o time

driver = webdriver.Chrome('C:/Users/ENGISA\Desktop/robos/chromedriver.exe') # abre o navegador
driver.get("https://registro.br/") # Abrindo o site

pesquisa = driver.find_element_by_id("is-avail-field") #pesquisa o campo de pesquisa
pesquisa.clear() # Limpa o campo
dominio = "roboscompython.com.br" # pesquisa se o dominio está disponivel 
pesquisa.send_keys(dominio)    # pesquisa o nome dentro do site digita o nome do site    
pesquisa.send_keys(Keys.RETURN) # pesquisa e retorna
time.sleep(2)   # Espera 2 segundos

driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')
print("Dominio %s %s" % (dominio, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))

time.sleep(5) # Espera 5 segundos
driver.close() # Fecha o navegador
