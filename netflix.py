import pandas as pd
import streamlit as st

movies_data = 'https://raw.githubusercontent.com/Manuel1928/Netflix/main/movies.csv'

datas=pd.read_csv(movies_data,encoding="ISO-8859-1")

@st.cache 
def load_data(nrows):
    data = pd.read_csv(movies_data, encoding="ISO-8859-1", nrows=nrows)
    return data

@st.cache
def load_data_byname(name):
  data = pd.read_csv(movies_data, encoding="ISO-8859-1")
  filtered_data_byname = data[data['name'].str.contains(name)]
  return filtered_data_byname

@st.cache
def load_data_bydirector(director):
  data = pd.read_csv(movies_data, encoding="ISO-8859-1")
  filtered_data_byname = data[data['director'].str.contains(director)]
  return filtered_data_byname

# Create the title for the web app
st.title("Netflix APP")
sidebar = st.sidebar
agree=sidebar.checkbox("Mostrar todos los filmes?")
nombre=sidebar.text_area("Titulo del filme:")
myname=sidebar.button("Buscar Filmes")
di=sidebar.selectbox("Buscar por director:",datas['director'].unique())
dire=sidebar.button("Filtrar director")
if (myname):
  filterbyname = load_data_byname(nombre)
  count_row = filterbyname.shape[0]
  st.write(f"Total names : {count_row}")
  st.dataframe(filterbyname)

# Display the content of the dataset if checkbox is true

if agree:
  data= load_data(500)
  st.dataframe(data)
if(dire):
  filterbydir = load_data_bydirector(di)
  count_row = filterbydir.shape[0]
  st.write(f"Total filmes: {count_row}")
  st.dataframe(filterbydir)
