import pandas as pd
import webbrowser
import time
import urllib.parse
import os
import pyautogui
import random

def iniciar_prospeccao_industrial():
    arquivo = "leads_prospeccao.csv"
    if not os.path.exists(arquivo):
        print("❌ ERRO: Rode o buscador primeiro para gerar a lista!")
        return

    df = pd.read_csv(arquivo)
    print(f"🚀 MOTOR LIGADO: {len(df)} leads encontrados.")

    contagem_envios = 0
    LIMITE_DIARIO = 30 # Segurança para não ser bloqueado

    for index, row in df.iterrows():
        if contagem_envios >= LIMITE_DIARIO:
            print(f"\n🛑 LIMITE DE SEGURANÇA ATINGIDO ({LIMITE_DIARIO}). Parando por hoje.")
            break

        empresa = row['Nome']
        fone_raw = str(row['WhatsApp'])
        fone_limpo = "".join(filter(str.isdigit, fone_raw))
        
        # Filtro regional DDD 24
        if "24" not in fone_limpo[:4]: 
            continue

        if not fone_limpo.startswith("55"):
            fone_limpo = "55" + fone_limpo

        mensagem = (
            f"Olá! Tudo bem? Me chamo *Wagner Fonseca*, sou Engenheiro Mecânico aqui em Barra Mansa.\n\n"
            f"Estou entrando em contato com algumas empresas da região para suporte técnico em *PMOC* "
            f"ou laudos estruturais.\n\n"
            f"Como sou da cidade, gostaria de me colocar à disposição caso precisem de vistoria, "
            f"renovação de laudo ou tirar dúvidas sobre a legislação da *ANVISA*.\n\n"
            f"----------------------------------------\n"
            f"📋 *MINHAS ESPECIALIDADES:*\n"
            f"----------------------------------------\n"
            f"• *PMOC & Exaustão de Coifas*\n"
            f"• *Laudos Técnicos & ART*\n"
            f"• *Simulação Estrutural (FEA)*\n"
            f"• *Linhas de Vida - NR 35*\n\n"
            f"----------------------------------------\n"
            f"Um abraço,\n*Eng. Wagner Fonseca*\n📞 (21) 97993-2621"
        )

        msg_url = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={fone_limpo}&text={msg_url}"

        print(f"\n▶️ [{index+1}] PROCESSANDO: {empresa}")
        webbrowser.open(link)

        # Espera o WhatsApp carregar (Aumentado para segurança)
        espera = random.randint(40, 60) 
        print(f"⏳ Aguardando {espera}s (Simulação Humana)...")
        time.sleep(espera)

        # Foco e Envio
        largura, altura = pyautogui.size()
        pyautogui.click(largura/2, altura/2) 
        time.sleep(1)
        pyautogui.press('enter')
        
        contagem_envios += 1
        print(f"✅ Enviada! Total de hoje: {contagem_envios}")

        # Fecha a aba para não sobrecarregar o PC (Ctrl + W)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')

    print(f"\n🏁 MISSÃO CUMPRIDA! {contagem_envios} contatos realizados.")

if __name__ == "__main__":
    iniciar_prospeccao_industrial()