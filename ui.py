import streamlit as st
import requests
import os

URL = os.getenv("URL")

st.title("Net Worth of your Solana Wallet")
user_input = st.text_input("Wallet Address", placeholder="Enter Wallet Address")

if st.button("Submit"):
    if user_input:
        try:
            payload = {"wallet_address": user_input}
            response = requests.post(URL, json=payload)
            net_worth = str(response.json())
            if response:
                st.write("Net Worth =", net_worth, "$")
        except Exception as e:
            st.error(e)
    else:
        st.warning("Wallet Address is empty! Enter valid Wallet Address")
