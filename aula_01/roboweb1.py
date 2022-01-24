from selenium import webdriver # importa o webdriver
from selenium.webdriver.common.keys import Keys # importa as teclas
import time # importa o time

driver = webdriver.Chrome('C:/Users/ENGISA\Desktop/robos/chromedriver.exe') # abre o navegador
driver.get("https://registro.br/") # Abrindo o site

pesquisa = driver.find_element_by_id("is-avail-field") #pesquisa o campo de pesquisa
pesquisa.clear() # Limpa o campo
pesquisa.send_keys("robo.python.com.br")    # pesquisa o nome dentro do site digita o nome do site    
pesquisa.send_keys(Keys.RETURN) # aperta enter
time.sleep(5)   # Espera 5 segundos

time.sleep(8) # Espera 8 segundos
driver.close # Fecha o navegador
