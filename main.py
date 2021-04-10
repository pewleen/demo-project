import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'x':[10,20,30,40],
                   'y':[100,200,300,400],
                   'name':['alpha','beta','gamma','delta']
                   })

x_max = st.slider('Max value of x', float(df['x'].max()))
st.title("My streamlit app")
st.markdown("""
Let's look at this fine dataframe
""")

df[df['x'] <= x_max]

st.markdown(
    """## Now let's draw something"""
)
a = st.slider('Amplitude', 0., 10.)
b = st.slider('Frequency', 0., 10.)
x = np.linspace(0, 10, 500)
fig = plt.figure()
plt.plot(x, a * np.sin(x * b))
plt.ylim(-5, 5)
st.pyplot(fig)


uploaded_file = st.file_uploader("Upload some file")
if uploaded_file is not None:
   # st.text(uploaded_file.getvalue().decode('utf-8'))
    for i, line in enumerate(
            uploaded_file.getvalue().decode('utf-8').splitlines()):
        st.text(f"{i}. {line}".rstrip())
