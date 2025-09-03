import streamlit as st
import openai
import os

# Recupera la chiave API da Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Carica la base di conoscenza
with open("reconsulting_base.txt", "r", encoding="utf-8") as f:
    knowledge_base = f.read()

# Interfaccia grafica
st.set_page_config(page_title="Reconsulting Chatbot", layout="centered")
st.title("💬 Chatbot Reconsulting")
st.write("Fai una domanda sui servizi Reconsulting. Il chatbot risponde basandosi su conoscenze pre-caricate.")

# Input utente
user_input = st.text_input("Scrivi la tua domanda:", "")

# Logica di risposta
if user_input:
    with st.spinner("Sto pensando..."):
        prompt = f"""Sei un assistente AI professionale. Rispondi solo in base al seguente testo. 
Se non trovi una risposta adeguata, invita l'utente a compilare il form: https://reconsulting.it/contatti

TESTO DI RIFERIMENTO:
{knowledge_base}

DOMANDA:
{user_input}

RISPOSTA:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=600
            )
            reply = response.choices[0].message.content.strip()
            st.success(reply)
        except Exception as e:
            st.error(f"Errore nell'API: {str(e)}")
