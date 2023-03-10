# ELIMINANDO SPAMS DO EMAIL:
#!usr/bin/env python
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
    arguments = ['--lang=pl', '--window-size=1000, 1300','--incognito']
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
        return data

def go_down_screen(value):
    driver.execute_script(f'window.scrollTo(0,{str(value)})')

user_data = 'assets\\user_data.txt'
if getsize(user_data) == 0:
    get_user_information()

new_user = input('Would you like to sign in with another account? Yes [y] - No [n]').lower().strip()
if new_user in ('yes', 'y'):
    get_user_information()
    
user_name, password = read_data()
email = user_name.split("\n")[0]
# 1: ABRIR O NAVEGADOR
driver = start_driver()
wait_a_little()
try:
    # 2: ACESSAR O SITE 'https://poczta.wp.pl/login/login.html'
    driver.get('https://poczta.wp.pl/login/login.html')
    wait_a_little()
    # PASSANDO NOTIFICAÇÕES
    try:
        notifications = driver.find_element(By.XPATH, '//button[text()="AKCEPTUJĘ I PRZECHODZĘ DO SERWISU"]')
        wait_a_little()
        # ACEITAR NOTIFICAÇÃO
        notifications.click()
        wait_a_little()
    except:
        print('Notification button not identified.')
    finally:
        # 3: LOCALIZAR CAMPO DE EMAIL
        email_bar = driver.find_element(By.ID,'login')
        wait_a_little()
        # 4: CLICAR NO CAMPO EMAIL
        email_bar.click()
        wait_a_little()
        # 5: DIGITAR EMAIL NO CAMPO DE EMAIL
        type_naturally(email, email_bar)
        wait_a_little()
        # 6: LOCALIZAR O CAMPO DE SENHA
        password_bar = driver.find_element(By.ID,'password')
        wait_a_little()
        # 7: CLICAR NO CAMPO SENHA
        password_bar.click()
        wait_a_little()
        # 8: DIGITAR SENHA
        type_naturally(password, password_bar)
        wait_a_little()
        # 9: LOCALIZAR CAMPO 'CONECTE-SE'
        button_logIn = driver.find_element(By.XPATH,"//button[@type='submit']")
        wait_a_little()
        # 10: CLICAR NO BOTÃO 'CONECTE-SE'
        button_logIn.click()
        wait_a_lot()
        # DESCER TELA 
        go_down_screen(150)
        # LOCALIZAR BOTÃO DE SPAM
        spam = driver.find_elements(By.XPATH, '//div[@class="sidebar__label"]')[3]
        wait_a_little()
        # CLICAR NO BOTÃO SPAM
        spam.click()
        wait_a_little()
        # DESCER TELA 
        go_down_screen(500)
        wait_a_little()
        try:
            # 13: ACHAR BARRA DE SELEÇAO DE TODOS OS SPAMS
            selector = driver.find_elements(By.XPATH, '//div[@class="Checkbox"]')[0]
            wait_a_little()
            # 14: CLICAR NA BARRA DE SELEÇÃO
            selector.click()
            wait_a_little()
            # 15: ENCONTRAR O BOTÃO EXCLUIR
            exclude_button = driver.find_elements(By.XPATH, '//button[@class="Button Button--secondary"]')[0]
            wait_a_little()
            # 16: SE O BOTÃO ESTIVER CLICÁVEL, EXCLUIR EMAILS. CASO CONTRÁRIO, EXIBIR MENSAGEM 'THERE'S NO SPAMS NOW.'
            exclude_button.click()
            wait_a_little()
            # 11: LOCALIZAR O BOTÃO 'SPAM'
            bin = driver.find_elements(By.XPATH, '//div[@class="sidebar__label"]')[0]
            # //span[@ng-if="LabelsController.resource.elementsById[5].count"]
            wait_a_little()
            # 12: CLICAR NO BOTÃO 'SPAM'
            bin.click()
            wait_a_little()
            # DESCER A BARRA DO NAVEGADOR
            go_down_screen(500)
            # 13: ACHAR BARRA DE SELEÇAO DE TODOS OS SPAMS
            selector = driver.find_elements(By.XPATH, '//div[@class="Checkbox"]')[0]
            wait_a_little()
            # 14: CLICAR NA BARRA DE SELEÇÃO
            selector.click()
            wait_a_little()
            # 15: ENCONTRAR O BOTÃO EXCLUIR
            exclude_button = driver.find_elements(By.XPATH, '//button[@class="Button Button--secondary"]')[0]
            wait_a_little()
            # 16: SE O BOTÃO ESTIVER CLICÁVEL, EXCLUIR EMAILS. CASO CONTRÁRIO, EXIBIR MENSAGEM 'THERE'S NO SPAMS NOW.'
            exclude_button.click()
            wait_a_little()
            confirmation = driver.find_element(By.XPATH, '//button[@class="Button Button--cta"]')
            wait_a_little()
            confirmation.click()
            print("\nSpams has been deleted successfully.\n")
        except:
            print("\nThere are no spams now. Please, try it again later.\n")
except:
        print('We could not delete the spams on your account. The website is likely', end=" ")
        print(' to have been updated. Please, reach out to the developer for new updates too.\n')
        driver.close()
    
