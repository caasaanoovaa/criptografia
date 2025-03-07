import streamlit as st
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Función para cifrar un mensaje
def cifrar_mensaje(texto):
    clave = os.urandom(16)
    iv = os.urandom(16)
    mensaje = texto.encode()
    mensaje += b' ' * (16 - len(mensaje) % 16)

    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cifrado = encryptor.update(mensaje) + encryptor.finalize()

    return cifrado, clave, iv

# Función para descifrar un mensaje
def descifrar_mensaje(cifrado, clave, iv):
    cipher_dec = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher_dec.decryptor()
    mensaje_descifrado = decryptor.update(cifrado) + decryptor.finalize()
    mensaje_descifrado = mensaje_descifrado.rstrip().decode()

    return mensaje_descifrado

st.title("Cifrado y Descifrado con AES")
texto = st.text_input("Introduce un texto para cifrar:")

if st.button("Cifrar y Descifrar"):
    if texto:
        cifrado, clave, iv = cifrar_mensaje(texto)
        mensaje_descifrado = descifrar_mensaje(cifrado, clave, iv)

        st.write("### Texto Cifrado:")
        st.code(cifrado)

        st.write("### Texto Descifrado:")
        st.code(mensaje_descifrado)
    else:
        st.error("Por favor, introduce un texto antes de cifrar.")
