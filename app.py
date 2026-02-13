import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') #lendo os dados do arquivo.
st.header('Anúncios de vendas de carro')

build_histogram = st.checkbox('Criar um histograma')

if build_histogram: #se a caixa for selecionada.
    st.write('Criando histograma para dados de anúncios de vendas de carro') #o que vai acontecer se clincar no botão.
    fig= px.histogram(car_data, x="model_year") #montando o histograma
    st.plotly_chart(fig , use_container_width=True)#exibindo o grafico em streamlit

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter: # se a caixa for selecionada
  st.write('Criando um gráfico de dispersão para todos os anúncios de vendas de carro')
  fig = px.scatter(car_data, x= "odometer", y="price") #criando gráfico de dispersão com valor do odômetro vs preço.
  st.plotly_chart(fig, use_container_width=True) #exibindo
 
