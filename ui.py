import streamlit as st
import requests
import os
import base58

URL = os.getenv("URL")


def is_valid_solana_address(address):
    try:
        decoded = base58.b58decode(address)
        return len(decoded) == 32
    except Exception:
        return False


st.title("Net Worth of your Solana Wallet")
user_input = st.text_input("Wallet Address", placeholder="Enter Wallet Address")

if st.button("Submit"):
    if is_valid_solana_address(user_input):
        if user_input:
            try:
                payload = {"wallet_address": user_input}
                response = requests.get(URL, json=payload)
                net_worth = str(response.json())
                if response:
                    st.subheader(f"NetWorth = :green[{net_worth} $]")
            except Exception as e:
                st.error(e)
        else:
            st.warning("Wallet Address is empty! Enter valid Wallet Address")
    else:
        st.error("Invalid Solana wallet address. Enter Valid Address.")
