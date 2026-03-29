import pandas as pd
import webbrowser
import time
import urllib.parse
import os

def disparar_whatsapp():
    # 1. Carrega os leads que o buscador encontrou
    if not os.path.exists("leads_prospeccao.csv"):
        print("❌ Arquivo de leads nao encontrado! Rode o buscador primeiro.")
        return

    leads = pd.read_csv("leads_prospeccao.csv")
    print(f"🚀 Iniciando disparos para {len(leads)} contatos...")

    for index, lead in leads.iterrows():
        nome = lead['Nome']
        telefone = str(lead['WhatsApp']).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        
        # Se nao tiver o codigo do pais, adiciona o 55 (Brasil)
        if not telefone.startswith("55"):
            telefone = "55" + telefone

        # MENSAGEM PERSONALIZADA (Altere aqui o seu texto)
        mensagem = f"Olá {nome}, tudo bem? Vi sua empresa no Google Maps e gostaria de oferecer nossos serviços de Engenharia e Manutenção em Barra Mansa. Podemos conversar?"
        
        # Codifica a mensagem para o link do WhatsApp
        texto_url = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto_url}"
        
        print(f"📲 Abrindo conversa com: {nome} ({telefone})")
        webbrowser.open(link)
        
        # TEMPO DE ESPERA: O WhatsApp Web demora para carregar
        # Voce precisa clicar no botao "Enviar" manualmente no primeiro teste
        print("⏳ Aguardando 20 segundos para voce enviar e o sistema carregar o proximo...")
        time.sleep(20) 

    print("\n✅ Rodada de prospecção finalizada!")

if __name__ == "__main__":
    disparar_whatsapp()