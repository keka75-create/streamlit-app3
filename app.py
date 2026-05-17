import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# ===== CHARGER LES UTILISATEURS =====
df_users = pd.read_csv('users.csv')

# ===== PAGE DE CONNEXION =====
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''

if not st.session_state['logged_in']:
    st.title("🔐 Connexion")
    username = st.text_input("Username")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        user = df_users[(df_users['name'] == username) & (df_users['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.rerun()
        else:
            st.error("Username ou mot de passe incorrect !")

else:
    with st.sidebar:
        st.write(f"Bienvenue **{st.session_state['username']}** 👋")
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Album photo"],
            icons=["house", "camera"],
        )
        if st.button("Déconnexion"):
            st.session_state['logged_in'] = False
            st.rerun()

    if selection == "Accueil":
        st.title("🏠 Bienvenue sur l'application !")
        st.write("Utilisez le menu à gauche pour naviguer.")

    elif selection == "Album photo":
        st.title("📸 Album photo")
        photos = [
            "img/chat1.jpg",
            "img/chat2.jpg",
            "img/chat3.jpg",
        ]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(photos[0])
        with col2:
            st.image(photos[1])
        with col3:
            st.image(photos[2])