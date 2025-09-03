import streamlit as st
import google.generativeai as genai

# Configura l'API key da Streamlit Cloud
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Carica la base di conoscenza
with open("reconsulting_base.txt", "r", encoding="utf-8") as f:
    knowledge_base = f.read()

# UI Streamlit
st.set_page_config(page_title="Reconsulting Chatbot - Gemini", layout="centered")
st.title("💬 Chatbot Reconsulting (Google Gemini)")
st.write("Fai una domanda sui servizi Reconsulting. Il chatbot risponde basandosi su conoscenze pre-caricate.")

# Input dell'utente
user_input = st.text_input("Scrivi la tua domanda:", "")

# Logica del chatbot
if user_input:
    with st.spinner("Sto pensando con Gemini..."):
        prompt = f"""\
Sei un assistente AI professionale che risponde alle domande sulla società Reconsulting.
Usa solo le informazioni qui sotto per rispondere. Se non trovi una risposta adeguata, suggerisci all'utente di contattare Reconsulting tramite il form: https://reconsulting.it/contatti

---
{knowledge_base}
---

Domanda: {user_input}
Risposta:
"""

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Errore nell'API Gemini: {str(e)}")

