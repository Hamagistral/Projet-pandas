import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projet Pandas", page_icon='📊')

st.title('📊 Mini Projet Pandas')

# Uploading the file
uploaded_file = st.file_uploader("Importer un fichier excel :", type='xlsx')
st.markdown('___')

# Preprocessing the excel
if uploaded_file is not None:

    # Reading Excel File
    df = pd.read_excel(uploaded_file)

    # Preprocessing the Excel File (see steps in jupyter notebook)
    df[['Id','Nom', 'Prenom', 'Université', 'Grade', 'Spécialité','Structure de recherche Porteuse']] = df[['Id','Nom', 'Prenom', 'Université', 'Grade', 'Spécialité','Structure de recherche Porteuse']].fillna(method='ffill')
    df = df.iloc[1:, :]
    df = df.rename({'Unnamed: 8': 'Grade_partenaire', 'Unnamed: 9': 'Spécialité_partenaire', 'Unnamed: 10': 'Intitulé de la structure', 'Unnamed: 12': 'Nombre'}, axis='columns')    
    df = df.fillna(0)
    df[['Id', 'Nombre']] = df[['Id', 'Nombre']].astype('int')
    df.set_index('Id', inplace=True, drop=True)

    # Number input for ID
    id = st.number_input("Donner l'ID de la personne :", min_value=1, value=1, step=1)
    st.markdown('___')

    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Élargir le tableau", value=False, key="use_container_width")

    if id in df.index:
        st.write("Informations sur le professeur :")
        st.dataframe(df.loc[df.index == id, ['Nom', 'Prenom','Université','Grade','Spécialité','Structure de recherche Porteuse']].head(1), use_container_width=st.session_state.use_container_width)
        st.markdown('___')
        st.write("Membre des structures de recherche partenaires :")
        st.dataframe(df.loc[df.index == id, ['Membre des structures de recherche partenaires','Grade','Spécialité_partenaire','Intitulé de la structure']], use_container_width=st.session_state.use_container_width)
        st.markdown('___')
        st.write("Publications Scientifiques :")
        st.dataframe(df.loc[df.index == id, ['Publications Scientifiques','Nombre']], use_container_width=st.session_state.use_container_width)  
    else:
        st.write("L'ID que vous recherchez n'existe pas dans le fichier !")


# Hide Left Menu
st.markdown("""<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)