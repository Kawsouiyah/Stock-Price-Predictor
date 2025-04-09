import streamlit as st
import joblib
import yfinance as yf
import pandas as pd
import emoji  

st.set_page_config(page_title="Prédiction du Prix des Actions", page_icon="📊")

st.title(f"{emoji.emojize(':money_with_wings:')} Prédiction du prix d'une action {emoji.emojize(':chart_with_upwards_trend:')}")


ticker = st.text_input(f"Entrez le symbole de l'action (ex: AAPL, TSLA, BTC-USD) {emoji.emojize(':rocket:')}", "AAPL")

model = joblib.load("model/stock_model.pkl")

if st.button(f" {emoji.emojize(':crystal_ball:')} Prédire le prix de demain"):
    # Télécharger les données récentes
    data = yf.download(ticker, period="5d")
    df = data[["Open", "High", "Low", "Close", "Volume"]].dropna()

    if df.empty:
        st.error(f" Aucune donnée récupérée. {emoji.emojize(':sweat:' )}")
    else:
        latest = df.iloc[-1]
        prediction = model.predict([latest])[0]
        st.success(f" Prix prédit pour demain : {round(prediction, 2)} USD {emoji.emojize(':money_bag:')}")

        st.subheader(f" Données les plus récentes {emoji.emojize(':memo:')}")
        st.write(latest)
