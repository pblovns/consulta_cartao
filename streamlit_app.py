<<<<<<< HEAD
import streamlit as st
import time

st.set_page_config(page_title='Consulta de Cartão', layout="centered")
st.html('<html lang="pt-BR"></html>')
st.logo(image=r'images\tropa-do-7.jpg', size="large", icon_image=r'images\tropa-do-7.jpg')

st.title('Informe os dados do seu cartão 🎭')
st.write('Consulte seu seu cartão foi clonado!')

def resultado():
    left, middle = st.columns(2)
    with st.container():
            with st.spinner('Verificando...'):
                time.sleep(7)
            st.balloons()
            st.success(body='Tranquilo paizão, seu cartão tá seguro! 👍🏼')
            left.image(r'images\bob-esponja-mandrake.jpg', width=220)
            middle.image(r'images\urubu-do-pix.jpg', width=250)

with st.container():
    numero_cartao = st.text_input(label='Número do Cartão:', max_chars=16)
    nome_cartao = st.text_input(label='Nome Impresso no Cartão:')

left, middle = st.columns(2)
with st.container():
    data_vencimento = left.date_input(label='Data de Vencimento do Cartão:', format="DD/MM/YYYY")
    cvv = middle.text_input(label='CVV', max_chars=3)

left, middle = st.columns(2)
with st.container():
    consulta = left.button(label='Consultar', use_container_width=True, on_click=resultado)
=======
import streamlit as st
import time

st.set_page_config(page_title='Consulta de Cartão', layout="centered")
st.html('<html lang="pt-BR"></html>')
st.logo(image=r'images\tropa-do-7.jpg', size="large", icon_image=r'images\tropa-do-7.jpg')

st.title('Informe os dados do seu cartão 🎭')
st.write('Consulte seu seu cartão foi clonado!')

def resultado():
    left, middle = st.columns(2)
    with st.container():
            with st.spinner('Verificando...'):
                time.sleep(7)
            st.balloons()
            st.success(body='Tranquilo paizão, seu cartão tá seguro! 👍🏼')
            left.image(r'images\bob-esponja-mandrake.jpg', width=220)
            middle.image(r'images\urubu-do-pix.jpg', width=250)

with st.container():
    numero_cartao = st.text_input(label='Número do Cartão:', max_chars=16)
    nome_cartao = st.text_input(label='Nome Impresso no Cartão:')

left, middle = st.columns(2)
with st.container():
    data_vencimento = left.date_input(label='Data de Vencimento do Cartão:', format="DD/MM/YYYY")
    cvv = middle.text_input(label='CVV', max_chars=3)

left, middle = st.columns(2)
with st.container():
    consulta = left.button(label='Consultar', use_container_width=True, on_click=resultado)
    middle.button(label='Nova Consulta', use_container_width=True)
