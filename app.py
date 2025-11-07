import requests
import streamlit as st


# Criando 3 colunas
col1, col2, col3 = st.columns([1, 4, 1])  # A coluna central tem mais peso (4x mais larga)

# Colocando a imagem na coluna do meio
with col2:
    st.image("https://images.pexels.com/photos/8378723/pexels-photo-8378723.jpeg", width=500)


def bring_quote():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    data = response.json()
    return data['slip']['advice']
with col2:
    if st.button("I want the quote", key='quote_button'):
        with st.spinner("Searching for the phrase..."):
            phrase = bring_quote()
            # st.success(frase)
            with st.container():
                st.markdown("### 💡 Quote of the day")
                st.info(phrase)
    else:
        st.info("Click the button and receive the quote of the day!")



with st.sidebar:
    st.title("Quote of the day")
    st.write("Receive an inspiring quote every time you click the button.")




