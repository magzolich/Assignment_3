import pandas as pd 
import streamlit as st
df = pd.read_csv("C:\\Users\\magda\\Downloads\\mieszkania_windows.csv")
print(df.head())
df_year = df.groupby(df["Rok"])['Wartosc'].mean()
print(df_year)
st.dataframe(df_year)