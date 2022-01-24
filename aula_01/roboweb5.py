from selenium import webdriver # importa o webdriver
from selenium.webdriver.common.keys import Keys # importa as teclas
import time # importa o time
import xlrd # importa o xlrd


print ("Iniciando o programa \n")
arq = open('resultado.txt', 'w')
workbook = xlrd.open_workbook(r'C:\Users\ENGISA\Desktop\robos\excel.xls') # abre o arquivo
sheet = workbook.sheet_by_name('Plan1') # pega a primeira planilha
rows = sheet.nrows # pega o numero de linhas
colums = sheet.ncols # pega o numero de colunas

options = webdriver.ChromeOptions() # abre o navegador
options.add_argument('--disable-logging') # desabilita o log
options.add_argument('--log-level=3') # desabilita o log    


driver = webdriver.Chrome('C:/Users/ENGISA\Desktop/robos/chromedriver', options=options) # abre o navegador
driver.get("https://registro.br/") # Abrindo o site


for curr_row in range(0, rows): # percorre as linhas
    x = sheet.cell_value(curr_row, 0) # pega o valor da celula
    pesquisa = driver.find_element_by_id("is-avail-field") #pesquisa o campo de pesquisa
    time.sleep(1) # Espera 1 segundo
    pesquisa.clear() # Limpa o campo
    time.sleep(1) # Espera 1 segundo
    pesquisa.send_keys(x)    # pesquisa o nome dentro do site digita o nome do site 
    time.sleep(1) # Espera 1 segundo   
    pesquisa.send_keys(Keys.RETURN) # pesquisa e retorna
    time.sleep(1)   # Espera 1 segundos
    driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)   # Espera 1segundos
    texto ="Dominio %s %s\n" % (x, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    arq.write(texto)

arq.close()
driver.close() # Fecha o navegador