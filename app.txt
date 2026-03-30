from flask import Flask, render_template, request, jsonify

import time

import webbrowser

import urllib.parse

import pyautogui

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



app = Flask(__name__)



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/buscar', methods=['POST'])

def buscar():

    dados = request.json

    nicho = dados['nicho']

    localidade = dados['localidade']

    limite = int(dados['limite'])



    options = Options()

    options.add_argument("--start-maximized")

    

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    leads_encontrados = []

    

    try:

        driver.get(f"https://www.google.com.br/maps/search/{nicho}+{localidade}")

        time.sleep(6)



        while len(leads_encontrados) < limite:

            cards = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/maps/place/"]')

            

            if not cards: break



            for card in cards:

                if len(leads_encontrados) >= limite: break

                try:

                    nome_empresa = card.get_attribute("aria-label")

                    if not nome_empresa or any(l['Nome'] == nome_empresa for l in leads_encontrados):

                        continue

                    

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)

                    time.sleep(1)

                    card.click()

                    time.sleep(3)



                    try:

                        fone_elem = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "phone:tel:")]')

                        fone = fone_elem.get_attribute("data-item-id").replace("phone:tel:", "").strip()

                    except:

                        fone = "Não encontrado"

                    

                    leads_encontrados.append({"Nome": nome_empresa, "WhatsApp": fone})

                except: continue



            try:

                feed = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')

                driver.execute_script("arguments[0].scrollBy(0, 1000);", feed)

                time.sleep(2)

            except: break

    finally:

        driver.quit()

    

    return jsonify(leads_encontrados)



@app.route('/disparar', methods=['POST'])

def disparar():

    dados = request.json

    leads = dados['leads']

    mensagem_base = dados['mensagem']

    delay = int(dados['delay'])



    # Tempo para você alternar para o navegador do WhatsApp se necessário

    time.sleep(5) 



    for lead in leads:

        nome = lead['Nome']

        telefone = lead['WhatsApp']

        

        if telefone == "Não encontrado":

            continue



        texto = mensagem_base.replace("{empresa}", nome)

        texto_final = urllib.parse.quote(texto)

        

        link_api = f"https://web.whatsapp.com/send?phone={telefone}&text={texto_final}"

        webbrowser.open(link_api)

        

        # Espera o carregamento da conversa

        time.sleep(16) 

        

        # Simula o pressionamento do Enter

        pyautogui.press('enter')

        

        # Delay de segurança entre um cliente e outro

        time.sleep(delay)



    return jsonify({"status": "Protocolo de disparos finalizado"})



if __name__ == '__main__':

    app.run(debug=True, port=5000)