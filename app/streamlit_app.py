
import streamlit as st
from src.bayesian_ab_test import compare
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bayesian A/B Testing")
st.title("🧮 Bayesian A/B Testing")

col1, col2 = st.columns(2)
with col1:
    a_s = st.number_input("A successes", min_value=0, value=120)
    a_n = st.number_input("A trials", min_value=1, value=200)
with col2:
    b_s = st.number_input("B successes", min_value=0, value=150)
    b_n = st.number_input("B trials", min_value=1, value=200)

res = compare(a_s, a_n, b_s, b_n)
st.write(res)

fig = plt.figure()
plt.bar([0,1], [res["a_mean"], res["b_mean"]])
plt.xticks([0,1], ["A", "B"])
plt.title("Posterior Mean Conversion Rates")
st.pyplot(fig)
