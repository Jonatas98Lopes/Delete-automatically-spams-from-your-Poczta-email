# ELIMINANDO SPAMS DO EMAIL:
from genericpath import getsize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random import randint
from time import sleep
import os

def start_driver():
    chrome_settings = Options()
    arguments = ['--lang=pl', '--window-size=1000, 1300','--incognito','headless']
    for argument in arguments:
        chrome_settings.add_argument(argument)
    chrome_settings.add_experimental_option('prefs',{
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options= chrome_settings)
    return driver

def type_naturally(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5) / 30)

def wait_a_little():
    sleep(randint(2, 10))

def wait_a_lot():
    sleep(randint(20, 30))

def get_data(type):
    while True:
        information = input(f'What is your {type}? ').strip()
        print(f'\nCheck {type}: {information}\n')
        check = input(f'Your {type} is correct? Yes - [y] | No [n]: ').lower().strip()
        if check in ('yes','y'):
            return information

def get_user_information():
    email_user = get_data('email address')
    password_user = get_data('password')
    save_data(email_user, password_user)

def save_data(data1, data2):
    with open(user_data, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write(f'{data1}{os.linesep}')
        arquivo.write(f'{data2}')

def read_data():
    data = []
    with open(user_data, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            data.append(linha)
        data[0] = data[0].split("\n")[0]
        return data

def go_down_screen(value):
    driver.execute_script(f'window.scrollTo(0,{str(value)})')

user_data = 'assets\\user_data.txt'
# 1 VERIFICAR SE O ARQUIVO "user_data.txt" ESTÁ VAZIO. SE SIM, OBTER CREDENCIAIS DE ACESSO DO USUÁRIO 
if getsize(user_data) == 0:
    #  SE SIM, OBTER CREDENCIAIS DE ACESSO DO USUÁRIO E SALVÁ-LAS NO "user_data.txt"
    get_user_information()

# 2 PERGUNTE SE O USUÁRIO QUER TROCAR DE CONTA.
new_user = input('Would you like to sign in with another account? Yes [y] - No [n] ').lower().strip()
if new_user in ('yes', 'y'):
    # SE SIM, OBTER AS NOVAS CREDENCIAIS DE ACESSO E SALVÁ-LAS NO "user_data.txt"
    get_user_information()

# 3 LER OS DADOS DE ACESSO DO USUÁRIO
email, password = read_data()
# 4: ABRIR O NAVEGADOR
driver = start_driver()
wait_a_little()
try:
    # 5: ACESSAR O SITE 'https://poczta.wp.pl/login/login.html'
    driver.get('https://poczta.wp.pl/login/login.html')
    wait_a_little()
    # 6: CASO O BOTÃO DE NOTIFICAÇÕES APAREÇA, CLICAR NELE. DO CONTRÁRIO, IGNORE-O.
    try:
        notifications = driver.find_element(By.XPATH, '//button[text()="AKCEPTUJĘ I PRZECHODZĘ DO SERWISU"]')
        wait_a_little()
        # ACEITAR NOTIFICAÇÃO
        notifications.click()
        wait_a_little()
    except:
        pass
    finally:
        # 7: LOCALIZAR CAMPO DE EMAIL
        email_bar = driver.find_element(By.ID,'login')
        wait_a_little()
        # 8: CLICAR NO CAMPO EMAIL
        email_bar.click()
        wait_a_little()
        # 9: DIGITAR EMAIL NO CAMPO DE EMAIL
        type_naturally(email, email_bar)
        wait_a_little()
        # 10: LOCALIZAR O CAMPO DE SENHA
        password_bar = driver.find_element(By.ID,'password')
        wait_a_little()
        # 11: CLICAR NO CAMPO SENHA
        password_bar.click()
        wait_a_little()
        # 12: DIGITAR SENHA
        type_naturally(password, password_bar)
        wait_a_little()
        # 13: LOCALIZAR CAMPO DE LOGIN
        button_logIn = driver.find_element(By.XPATH,"//button[@type='submit']")
        wait_a_little()
        # 14: CLICAR NO BOTÃO DE LOGIN
        button_logIn.click()
        wait_a_lot()
        # 15: DESCER A TELA 150px
        go_down_screen(150)
        # 16: LOCALIZAR BOTÃO DE SPAM
        spam = driver.find_elements(By.XPATH, '//div[@class="sidebar__label"]')[3]
        wait_a_little()
        # 17: CLICAR NO BOTÃO DE SPAM
        spam.click()
        wait_a_little()
        # 18: DESCER A TELA 500px
        go_down_screen(500)
        wait_a_little()
        try:
            # 19: ACHAR ÍCONE DE SELEÇÃO DE TODOS OS SPAMS
            selector = driver.find_elements(By.XPATH, '//div[@class="Checkbox"]')[0]
            wait_a_little()
            # 20: CLICAR NO ÍCONE DE SELEÇÃO DE TODOS OS SPAMS
            selector.click()
            wait_a_little()
            # 21: ENCONTRAR O BOTÃO EXCLUIR
            exclude_button = driver.find_elements(By.XPATH, '//button[@class="Button Button--secondary"]')[0]
            wait_a_little()
            # 22: CLICAR NO BOTÃO EXCLUIR
            exclude_button.click()
            wait_a_little()
            # 23: LOCALIZAR BOTÃO DE CONFIRMAÇÃO DE EXCLUSÃO
            confirmation = driver.find_element(By.XPATH, '//button[@class="Button Button--cta"]')
            wait_a_little()
            # 24: CLICAR NA CONFIRMAÇÃO DE EXCLUSÃO
            confirmation.click()
            wait_a_little()
            # 25: FECHAR JANELA DO NAVEGADOR
            driver.close()
            # 26: IMPRIMIR MENSAGEM: "Os spams foram deletados com sucesso."
            print("\nSpams has been deleted successfully.\n")
        # ?: CASO HAJA UM ERRO NESSE PROCESSO, SIGNIFICA QUE NAO HÁ SPAMS"
        except:
            # ??: NESTE CASO, IMPRIMIR MENSAGEM: "Não há spams agora. Por favor, tente mais tarde."
            print("\nThere are no spams now. Please, try it again later.\n")
# !: SE POR ACASO, OS BUTÕES NÃO FOREM LOCALIZADOS, O SITE DEVE TER SIDO ATUALIZADO.
except:
        # !: NESTE CASO, INFORMAR O USUÁRIO PARA QUE ELE NOTIFIQUE O DESENVOLVEDOR.
        print('We could not delete the spams on your account. The website is likely', end=" ")
        print(' to have been updated. Please, reach out to the developer for new updates too.\n')
        # 31: FECHAR JANELA DO NAVEGADOR
        driver.close()
