import pandas as pd
import webbrowser
import time
import urllib.parse
import os
import pyautogui
import random

ARQUIVO_LEADS = "leads_prospeccao.csv"
ARQUIVO_LOG = "log_envios.txt"
LIMITE_DIARIO = 30 

def carregar_log():
    if not os.path.exists(ARQUIVO_LOG): return []
    with open(ARQUIVO_LOG, "r") as f: return f.read().splitlines()

def salvar_no_log(numero):
    with open(ARQUIVO_LOG, "a") as f: f.write(f"{numero}\n")

def iniciar_prospeccao_inteligente():
    df = pd.read_csv(ARQUIVO_LEADS)
    enviados = carregar_log()
    contagem_hoje = 0

    for index, row in df.iterrows():
        if contagem_hoje >= LIMITE_DIARIO: break

        empresa = row['Nome']
        fone_raw = str(row['WhatsApp'])
        fone_limpo = "".join(filter(str.isdigit, fone_raw))
        
        if not fone_limpo.startswith("55"): fone_limpo = "55" + fone_limpo
        if fone_limpo in enviados: continue

        # --- LÓGICA DE WHATSAPP ---
        # No Brasil, celulares têm o 9 depois do DDD. 
        # Ex: 55 24 9... (total 13 dígitos)
        e_celular = len(fone_limpo) >= 13 and fone_limpo[4] == '9'
        
        status_msg = "📱 CELULAR" if e_celular else "☎️ POSSÍVEL FIXO"
        print(f"\n▶️ [{contagem_hoje+1}] {status_msg}: {empresa}")

        mensagem = (
            f"Olá! Tudo bem? Me chamo *Wagner Fonseca*, sou Engenheiro Mecânico aqui em Barra Mansa.\n\n"
            f"Estou entrando em contato com a *{empresa}* para me colocar à disposição "
            f"caso precisem de suporte técnico em *PMOC* ou laudos estruturais.\n\n"
            f"Como sou da cidade, gostaria de deixar meu contato para vistorias ou "
            f"tirar dúvidas sobre a legislação da *ANVISA*.\n\n"
            f"----------------------------------------\n"
            f"📋 *MINHAS ESPECIALIDADES:*\n"
            f"----------------------------------------\n"
            f"• *PMOC & Exaustão de Coifas*\n"
            f"• *Laudos Técnicos & ART*\n"
            f"• *Linhas de Vida - NR 35*\n\n"
            f"Um abraço, *Eng. Wagner Fonseca* - (21) 97993-2621"
        )

        webbrowser.open(f"https://web.whatsapp.com/send?phone={fone_limpo}&text={urllib.parse.quote(mensagem)}")

        # Tempo para carregar. Se for fixo SEM zap, a página avisa rápido.
        espera = random.randint(35, 50)
        print(f"⏳ Analisando número e aguardando {espera}s...")
        time.sleep(espera)

        # FOCO E ENVIO
        pyautogui.click(pyautogui.size().width/2, pyautogui.size().height/2)
        time.sleep(1)
        pyautogui.press('enter')
        
        salvar_no_log(fone_limpo)
        contagem_hoje += 1
        
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w') # Fecha a aba

    print(f"\n🏁 Ciclo finalizado!")

if __name__ == "__main__":
    iniciar_prospeccao_inteligente()