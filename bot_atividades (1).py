#bibliotecaskkk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os, sys

os.system("cls")

try:
    os.system("pip install webdriver_manager")
    os.system("pip install selenium")
except:
    print("nescessario instalar python")
os.system("cls")

if sys.version_info[0] < 3:
    print(f'{C}[{R}ERROR{C}] Necessário utilizar python3!')
    print(f'{C}[{Y}i{C}] Instale-o com base em sua distribuição.')
    print(f'{C}[{Y}i{C}] caso precise de ajuda veja algum tutorial')
    sys.exit()

print(r"""    

                _________  ________  ________  ________  _______   ________  _____ ______   ________     
               |\___   ___\\   __  \|\   __  \|\   __  \|\  ___ \ |\   ____\|\   _ \  _   \|\   __  \    
               \|___ \  \_\ \  \|\  \ \  \|\  \ \  \|\  \ \   __/|\ \  \___|\ \  \\\__\ \  \ \  \|\  \   
                    \ \  \ \ \  \\\  \ \   _  _\ \   _  _\ \  \_|/_\ \_____  \ \  \\|__| \  \ \  \\\  \  
                     \ \  \ \ \  \\\  \ \  \\  \\ \  \\  \\ \  \_|\ \|____|\  \ \  \    \ \  \ \  \\\  \ 
                      \ \__\ \ \_______\ \__\\ _\\ \__\\ _\\ \_______\____\_\  \ \__\    \ \__\ \_______\
                       \|__|  \|_______|\|__|\|__|\|__|\|__|\|_______|\_________\|__|     \|__|\|_______|     
                                                                     \|_________|                         



                                                                                                                       """)

#primeiro login(beta)
print("********Este progama eh gratis e OpenSource********")
print("********A todos que nao sabem o que é OpenSource, recomendo estudo********")
print("********Agora fique com o progama********")
print("********DEVELOPED BY: TORRESMO********")

time.sleep(4)

os.system("cls")

print("Reiniciando em alguns segundos")

time.sleep(5)

os.system("cls")
print("'''")


senha = str(input("Digite a senha: ".strip()))
while senha not in 'omserrot':
    print("senha errada :( tente novamente mais tarde :3")
    print("reabra o programa e tente novamente :p")
    exit()
print("Login Realizado")


os.system("cls")

print(r"""

                         ████████╗░█████╗░██████╗░██████╗░███████╗░██████╗███╗░░░███╗░█████╗░
                         ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║██╔══██╗    
                         ░░░██║░░░██║░░██║██████╔╝██████╔╝█████╗░░╚█████╗░██╔████╔██║██║░░██║
                         ░░░██║░░░██║░░██║██╔══██╗██╔══██╗██╔══╝░░░╚═══██╗██║╚██╔╝██║██║░░██║
                         ░░░██║░░░╚█████╔╝██║░░██║██║░░██║███████╗██████╔╝██║░╚═╝░██║╚█████╔╝
                         ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
                         
                                                                       """)



print("*******NOTA: login é seu login no site do sigaa, seu cpf, e a senha obviamente é a senha*******")
print("*******nenhum dado colocado nesse progama esta sendo visto por mim, ou por terceiros*******")
print("*******SEUS DADOS ESTAO SEGUROS*******")


########################################################################################################################################################

#fiquei sabendo de uma certa pessoa que disse que os alunos de ele1 nunca teriam futuro, cá estou eu para provar o contrario
#pessoa que nao irei revelar o nome, voce nao é bem vindo aqui!!!!!
#deixando bem claro para quem ler esse script, que isso eh uma coisa feita para fins de estudo, nao tem como intenção prejudicar a escola, ou o site

#########################################################################################################################################################

#login no site

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

time.sleep(3)




#historia
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[13]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[29]/div[1]/div[2]/span/div/span[2]/a").click()

#portugues

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[19]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[21]/div[1]/div[2]/span/div/span[2]/a").click()

#fisica

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[9]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[55]/div[1]/div[2]/span[2]/div/span[2]/a").click()

#REDAÇÃO


driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[27]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[18]/div[1]/div[2]/span[3]/div/span[2]/a").click()


#filosofia

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[7]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[21]/div[1]/div[2]/span[3]/div/span[2]/a").click()

#biologiakk

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[3]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[31]/div[1]/div[2]/span[2]/div/span[2]/a").click()

#artes agr aqui

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[1]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[10]/div[1]/div[2]/span/div/span[2]/a").click()

#ingles kapa kapa

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[17]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[4]/div[1]/div[2]/span/div/span[2]/a").click()

#educação fisica

driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[5]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[6]/div[1]/div[2]/span[5]/div/span[2]/a").click()


#matematica
driver.get("https://sig.cefetmg.br/sigaa/verTelaLogin.do")
driver.find_element_by_name("user.login").send_keys(login)
driver.find_element_by_name("user.senha").send_keys(senha)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[21]/td[1]/form/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/form/span/span[28]/div[1]/div[2]/span/div/span[2]/a").click()


input()


#NOTA: FEITO POR TORRESMO
#OBRIGADO PELA AJUDA: KEDER, GCOELHO171, CAUAN...
#NOTA2.0, nenhum dado colocado nesse progama esta sendo visto por mim, ou por terceiros

print("obrigado por usar")

# :3