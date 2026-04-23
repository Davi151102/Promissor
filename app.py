import streamlit as st
import requests

st.title("Diagnóstico do Bot Telegram")

token = st.text_input("Cole seu TOKEN aqui:", type="password")
chat_id = st.text_input("Cole seu CHAT ID aqui:")

if st.button("Rodar Diagnóstico"):
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/getMe"
        try:
            # Teste 1: O Token é válido?
            r1 = requests.get(url)
            if r1.status_code == 200:
                st.success(f"✅ Token Válido! Nome do Bot: {r1.json()['result']['first_name']}")
                
                # Teste 2: Tentar enviar mensagem
                url_send = f"https://api.telegram.org/bot{token}/sendMessage"
                dados = {"chat_id": chat_id, "text": "Teste de conexão do Barber App! ✂️"}
                r2 = requests.post(url_send, data=dados)
                
                if r2.status_code == 200:
                    st.success("✅ MENSAGEM ENVIADA! Cheque seu Telegram.")
                else:
                    st.error(f"❌ Erro ao enviar: {r2.json()['description']}")
                    if "chat not found" in r2.text:
                        st.info("💡 DICA: Você esqueceu de abrir o bot no Telegram e clicar em 'COMEÇAR'.")
            else:
                st.error("❌ Token Inválido! Verifique se copiou o código inteiro do BotFather.")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")
    else:
        st.warning("Preencha o Token e o ID para testar.")
