import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') #lendo os dados do arquivo.
st.header('Análise Comparativa do Mercado de Carros Usados') #titulo do dashboard.

build_histogram = st.checkbox('Click para criar uma histograma que compare as Condição do Veículo Vs Preço.')
if build_histogram: #se essa caixa for selecionada.
    st.write('Criando histograma comparando as Condições do Veículo anúnciados VS o preço.') #o que acontece se clincar no botão.
    fig = px.histogram(
        car_data,
        x = "condition",
        y = "price",
        title='Condição do Veículo VS Preço',
        color = 'condition',
        color_discrete_sequence=px.colors.qualitative.Set1
    ) #criando histograma com as condições que os veículos estão VS o preço.
    fig.update_layout(
        xaxis_title="Condição do Veículo",
        yaxis_title="Preço"
    )#Eixos, etc.
    st.plotly_chart(fig , use_container_width=True)#exibindo o grafico em streamlit

build_scatter = st.checkbox('Criando um gráfico de dispersão entre Modelo de Carro VS Odômetro')

if build_scatter: # se a caixa for selecionada
    st.write('Criando um gráfico de dispersão para ver seo modelo tem relação com o odômetro.')
    fig = px.scatter(
        car_data,
        x= "model",
        y="odometer",
        color='model',
        color_discrete_sequence=px.colors.qualitative.Set1
    )#Criando um gráfico de dispersão para ver se a qualidade do modelo tem relação com o odômetro.
    fig.update_layout(
        xaxis_tickangle=45,
        title= "Relação entre Modelo e Odômetro",
        xaxis_title="Modelo de Veículo",
        yaxis_title="Odômetro"
    )#Titulos,Eixos, etc.
    fig.update_layout(
    autosize=True,  # Permite redimensionamento automático
    margin=dict(l=50, r=50, t=50, b=50),
    width=1200,height=600
    ) #Redimencionando o tamanho do grafico.
    st.plotly_chart(fig, use_container_width=True) #exibindo
 
