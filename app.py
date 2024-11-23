# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:49:26 2024

@author: shere
"""

import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

# Streamlit app layout
st.title("Caesar Cipher Web App")
st.write("Encrypt your text using the Caesar cipher.")

# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (-25-25):", min_value=-25, max_value=25, value=3)

# Button to encrypt
if st.button("Encrypt"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")