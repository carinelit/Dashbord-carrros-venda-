import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') #lendo os dados do arquivo.
st.header('Anúncios de vendas de carro')

build_histogram = st.checkbox('Criar uma histograma que comparar Condição do Veículo Vs Preço.')

if build_histogram: #se a caixa for selecionada.
    st.write('Criando histograma para dados de anúncios de vendas de carro') #o que acontece se clincar no botão.
    car_data_tips = px.data.tips()
    fig = px.histogram(car_data , x = "condition", y = "price", color = 'condition', color_discrete_sequence=px.colors.qualitative.Set1) #criando histograma com as condições que os veículos estão VS o preço.
    st.plotly_chart(fig , use_container_width=True)#exibindo o grafico em streamlit

build_scatter = st.checkbox('Criar um gráfico de dispersão entre Modelo de Carro VS Odômetro')

if build_scatter: # se a caixa for selecionada
  st.write('Criando um gráfico de dispersão para ver se a qua')
  fig = px.scatter(car_data, x= "model", y="odometer", color='model',color_discrete_sequence=px.colors.qualitative.Set1)
  fig.update_layout(xaxis_tickangle=45,title= "Relação entre Modelo e Odômetro", xaxis_title="Modelo de Veículo", yaxis_title="Odômetro")#Criando umma aparencia melhor para analisar entre 
  st.plotly_chart(fig, use_container_width=True) #exibindo
 
