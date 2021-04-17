import streamlit as st
import sklearn
import joblib
model = joblib.load('Review_Class')
st.title('Review Classifier')
ip = st.text_input('Enter your review')
op = model.predict([ip])
if st.button('Predict'):
  if op[0]==0:
    st.title('Negative Review')
  elif op[0]==1:
    st.title('Neutral Review')
  else:
    st.title('Positive Review')
