import streamlit as st
import pandas as pd
import numpy as np

st.title('My first cloud app')

st.write("A simple dataframe: ")

df=pd.DataFrame(np.random.rand(10,2), columns=['a','b'])
st.dataframe(df)