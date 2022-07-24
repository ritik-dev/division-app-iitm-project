import streamlit as st

st.set_page_config(page_title="Division", page_icon=":heavy_division_sign:",layout="wide")
#-----HEADER------

st.subheader("Division :heavy_division_sign: App")
st.title("Divide 2 Numbers here : ")
st.write("A web Division App Made using Python :")
st.write("[Links](https://www.google.com)")

st.write('*Expression : a/b*')
a = st.number_input('Enter a :')
b = st.number_input('Enter b :')
d = (a/b)
st.write(a,"÷",b," = ",d) 