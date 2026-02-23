import streamlit as st
import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

st.title("Email Spam Classifier")

message = st.text_input("Enter your email message")

if st.button("Predict"):
    if message.strip() != "":
        
        message_transformed = vectorizer.transform([message])
        
        prediction = model.predict(message_transformed)
        
        if prediction[0] == 0:
            st.error("Spam Email 🚨")
        else:
            st.success("Not Spam Email ✅")
    else:
        st.warning("Please enter a message.")