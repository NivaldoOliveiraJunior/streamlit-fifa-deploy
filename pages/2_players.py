import streamlit as st

# para ajustar como os valores de venda e salrios do jogador ficam formatados de acordo com a página
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]


#seletor de clubes, e depois pega o clube dentro so side bar e joga na variavel club.
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube",clubes)

#Selecionar o jogador do clube selecionado acima.
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player  = st.sidebar.selectbox("Jogador", players)

# Selecionando os dados do jogador escolhido acima, nocaso apenas a foto dele.
player_stats = df_data[df_data["Name"] == player].iloc[0]
#Foto do jogador
st.image(player_stats["Photo"])

# nome do jogador
st.title(player_stats["Name"])

# clube do jogador
st.markdown(f"**Clube:** {player_stats['Club']}")

#posição em que joga
st.markdown(f"**Posição:** {player_stats['Position']}")


# colunas para os dados pessoais
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] *0.453:.2f}")
st.divider()


st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))


#Quanto custa e quanto ganha
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado",delta=100.00, delta_color="normal" ,border=True ,value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal",delta=200.00, delta_color="normal",border=True , value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão",delta=190.00, delta_color="normal" ,border=True ,value=f"£ {player_stats['Release Clause(£)']:,}")
             


