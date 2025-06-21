
import streamlit as st
from utils import calculate_player_score, get_market_value, get_team_suggestions
import json

# טוען את רשימת הקבוצות
with open("data/clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)["clubs"]

st.set_page_config(page_title="GiladScore", layout="centered")
st.title("⚽ GiladScore - ניתוח שחקני כדורגל")

player_name = st.text_input("הזן שם שחקן:")
selected_team = st.selectbox("בחר קבוצה להערכת התאמה:", clubs)

if st.button("חשב מדדים"):
    with st.spinner("טוען נתונים..."):
        score = calculate_player_score(player_name)
        value = get_market_value(player_name)
        fit = get_team_suggestions(player_name, selected_team)

    st.subheader("📊 תוצאות")
    st.write(f"**מדד ביצועים:** {score}")
    st.write(f"**שווי שוק (מוערך):** {value}")
    st.write(f"**התאמה לקבוצה {selected_team}:** {fit}")
