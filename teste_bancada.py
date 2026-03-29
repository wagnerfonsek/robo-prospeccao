import webbrowser
import time
import urllib.parse
import pyautogui

def teste_bancada_completo():
    # CONFIGURAÇÃO DO SEU NÚMERO DE TESTE
    numero_teste = "5524999459746" 
    
    # MENSAGEM UNIFICADA (Abordagem + Especialidades + NR-35)
    mensagem = (
        "Olá, tudo bem? Me chamo *Wagner Fonseca*, sou Engenheiro Mecânico aqui em Barra Mansa.\n\n"
        "Estou entrando em contato com algumas empresas da região para me colocar à disposição "
        "caso precisem de suporte técnico em *PMOC* (Plano de Manutenção de Ar-condicionado) ou laudos estruturais.\n\n"
        "Não sei se vocês já possuem um responsável técnico ou se já têm o plano de manutenção em dia, "
        "mas como sou da cidade, gostaria de deixar meu contato caso precisem de uma vistoria, "
        "renovação de laudo ou tirar dúvidas técnicas sobre a legislação da *ANVISA*.\n\n"
        "----------------------------------------\n"
        "📋 *MINHAS ESPECIALIDADES:*\n"
        "----------------------------------------\n"
        "• *PMOC & Exaustão de Coifas*\n"
        "• *Laudos Técnicos & ART*\n"
        "• *Simulação Estrutural (FEA)*\n"
        "• *Linhas de Vida - NR 35*\n\n"
        "----------------------------------------\n"
        "Um abraço,\n"
        "*Eng. Wagner Fonseca*\n"
        "📞 (21) 97993-2621"
    )

    # Codificação para o link do Zap
    texto_url = urllib.parse.quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero_teste}&text={texto_url}"

    print(f"🚀 Iniciando teste de disparo automático para: {numero_teste}")
    webbrowser.open(link)
    
    # TEMPO DE ESPERA: Aguarda carregar o WhatsApp Web
    print("⏳ Aguardando 22 segundos para carregar o WhatsApp...")
    time.sleep(22) 
    
    # AJUSTE DE FOCO: Clica no centro da tela para o Windows entender que queremos usar essa aba
    largura, altura = pyautogui.size()
    pyautogui.click(largura/2, altura/2)
    
    time.sleep(1) # Pausa técnica após o clique de foco
    
    # O GATILHO: Aperta ENTER sozinho
    pyautogui.press('enter')
    
    print("\n✅ SUCESSO! Mensagem enviada automaticamente.")

if __name__ == "__main__":
    teste_bancada_completo()