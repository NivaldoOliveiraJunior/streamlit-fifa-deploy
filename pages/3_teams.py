import streamlit as st

#formatação da pagina
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

#pegando os dados que estão na session
df_data = st.session_state["data"]

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

#Filtrando o df que vai ser utilizado para exibição.
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

#vamos coletar a primeira imagem de jogador utilizando o iloc
st.image(df_filtered.iloc[0] ["Club Logo"])
st.markdown(f"## {club}")

#criando uma variavel que contenha apernas as colunas que eu quero dentro do data frame que vou apresentar na tela
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

#Utilizando aas colunas dentro do data frame para exibição.
# Vamos configurar tambem cada coluna do dataframe utilizando o colum_config.
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })


