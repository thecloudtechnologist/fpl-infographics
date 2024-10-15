import streamlit as st
import pandas as pd
import plotly.express as px
#

CURR_GW = st.session_state.CURR_GW
#
# sidebar
with st.sidebar:
    st.markdown(""":soccer: :green[FPL] *Infographics*""")
    st.caption(
        """Latest gameweek data: :blue["""
        + str(CURR_GW)
        + """]  
                [thecloudtechnologist](https://github.com/thecloudtechnologist)"""
    )

############
st.markdown(
    "##### Set piece takers"
)
PLAYERS_DF = pd.read_csv("players_data.csv")
FK_DF = PLAYERS_DF[PLAYERS_DF['direct_freekicks_order'] == 1]
PEN_DF = PLAYERS_DF[PLAYERS_DF['penalties_order'] == 1]
CORN_DF = PLAYERS_DF[PLAYERS_DF['corners_and_indirect_freekicks_order'] == 1]

#
FK_DF = FK_DF[['web_name','team']]
FK_DF.rename(columns={'web_name': 'Name'}, inplace=True)
#
PEN_DF = PEN_DF[['web_name','team']]
PEN_DF.rename(columns={'web_name': 'Name'}, inplace=True)
#
CORN_DF = CORN_DF[['web_name','team']]
CORN_DF.rename(columns={'web_name': 'Name'}, inplace=True)
#
tab1, tab2, tab3 = st.tabs(["Penalties Oder","Direct free kicks","Corners and Indirect free kicks"])
with tab1:
    st.dataframe(data=PEN_DF,hide_index=True,use_container_width=False,width=800, height=1500)
with tab2:
    st.dataframe(data=FK_DF,hide_index=True,use_container_width=False,width=800, height=1500)
with tab3:
    st.dataframe(data=CORN_DF,hide_index=True,use_container_width=False,width=800, height=1500)