import streamlit as st
import pandas as pd
import json
from PyPDF2 import PdfReader
from metrics import detect_authenticity, consistency_of_emotion, positive_emotions, negative_emotions, authenticity_keywords
from metrics import consistency_of_opinion, positive_opinion, negative_opinion, alertness_in_conversation, engagement_keywords, clarifying_keywords
from metrics1 import detect_sarcasm, sarcasm_indicators, exaggeration_phrases, contradictory_phrases, high_risk_words, detect_high_risk_words
from metrics1 import openness_keywords, detect_openness
from logic import metric_logic

st.title("Analyze Your Chat")
uploaded_file = st.file_uploader("Upload Chat Data", type=["txt", "csv", "json", "pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if uploaded_file.type == "text/plain":
        chat_data = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/json":
        chat_data = json.load(uploaded_file)
    elif uploaded_file.type == "text/csv":
        chat_data = pd.read_csv(uploaded_file)
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        chat_data = ""
        for page in pdf_reader.pages:
            chat_data += page.extract_text()
    else:
        st.error("Unsupported file format.")
        st.stop()

    st.subheader("Uploaded data preview")
    #add on
    st.session_state["chat_data"] = chat_data
    #
    st.write("Data Preview:", chat_data)

    st.subheader("Choose a Metric")
    metrics = [
        "Authenticity",
        "Consistency of Emotion",
        "Consistency of Opinion",
        "Alertness in Conversation",
        "Use of Sarcasm",
        "High-Risk Words Usage",
        "Openness to Improve",
    ]

    metrics = list(metric_logic.keys())
    selected_metric = st.selectbox("Select a Metric to Analyze", [None] + metrics)

    if selected_metric and selected_metric != "None": 
        st.subheader(f"Logic of {selected_metric}")
        st.code(metric_logic[selected_metric], language="python")

    if st.button("Analyze"):
        if selected_metric == "Authenticity":
            result = detect_authenticity(chat_data, authenticity_keywords)
            st.write("---Analysis Of Authenticity---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == "Consistency of Emotion":
            result = consistency_of_emotion(chat_data, positive_emotions, negative_emotions)
            st.write("---Analysis Of Consistency of Emotion---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == "Consistency of Opinion":
            result = consistency_of_opinion(chat_data, positive_opinion, negative_opinion)
            st.session_state['opinion_result'] = result
            st.write("---Analysis Of Consistency Of Openion---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == 'Alertness in Conversation':
            result = alertness_in_conversation(chat_data, engagement_keywords, clarifying_keywords)
            st.session_state['alertness_result'] = result
            st.write("---Analysis Of Alertness In Conversation---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == 'Use of Sarcasm':
            result = detect_sarcasm(chat_data, sarcasm_indicators, exaggeration_phrases, contradictory_phrases)
            st.session_state['sarcasm_result'] = result
            st.write("---Analysis Of Sarcasm---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == 'High-Risk Words Usage':
            result = detect_high_risk_words(chat_data, high_risk_words)
            st.session_state['risk_word_result'] = result
            st.write("---Analysis Of Risk Words---")
            for key, value in result.items():
                st.write(f"{key}: {value}")

        elif selected_metric == 'Openness to Improve':
            result = detect_openness(chat_data, openness_keywords)
            st.session_state['openness_result'] = result
            st.write("---Analysis Of Openness---")
            for key, value in result.items():
                st.write(f"{key}: {value}")
        else:
            st.warning("This metric is not yet implemented.")

selected_text = st.text_area("Paste or write the info that you want to underline", "", height=100)
comment = st.text_area("Comment on the selected text", "")

if st.button("Submit Selected Text"):
    if selected_text: 
        st.session_state.selected_text = selected_text
        st.session_state.comment = comment
        
        st.write("You selected:", st.session_state.selected_text)
        st.write("Your comment:", st.session_state.comment)
    else:
        st.warning("Please enter a portion of text to comment on.")
