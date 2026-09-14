import streamlit as st

st.title("meu primeiro app funcionou")
st.success("parabéns yally, seu robô está no ar")



st.write("agora estamos na etapa 1: seu sistema já tem um link.")



preco = st.number_input("digite o preco por m2", value=15.50)
area = st.number_input("digite a área", value=250)

if st.button("Resultado"):
    st.write(f"total: R${preco * area:.2f}")
