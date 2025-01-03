import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as mplt
import seaborn as sb
import plotly.graph_objects as go
import re
from metrics1 import detect_openness, openness_keywords

st.title("Openness Breakdown Report")

if 'chat_data' in st.session_state:
    chat_data = st.session_state["chat_data"]

    openness_result = detect_openness(chat_data, openness_keywords)

    st.write("### Openness to Improve Metrics")
    st.table(openness_result.items())

    openness_data = pd.DataFrame.from_dict(
        {"Metric": list(openness_result.keys()), "Value": list(openness_result.values())}
    )

    st.write("### Openness Metrics Visualization")
    st.bar_chart(openness_data.set_index("Metric"))

    if openness_result["Total Words"] == 0:
        st.write("### No Openness Keywords Detected")
        st.write(openness_result["Message"])
    else:
        st.write("### Openness Pie Chart")
        openness_chart_data = pd.DataFrame({
            "Metric": ["Openness Keywords", "Total Words"],
            "Count": [openness_result["Openness Keywords"], openness_result["Total Words"] - openness_result["Openness Keywords"]]
        })

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=openness_chart_data["Metric"],
                    values=openness_chart_data["Count"],
                    textinfo="label+percent",
                    insidetextorientation="radial",
                    marker=dict(colors=["blue", "orange"]),
                )
            ]
        )

        fig.update_layout(
            title="Openness Word Distribution",
            annotations=[
                dict(
                    text=f"Openness Keywords: {openness_result['Openness Keywords']}",
                    x=0.8,
                    y=-0.2,
                    showarrow=False,
                    font=dict(size=12, color="black"),
                    align="right",
                    xanchor="center",
                    yanchor="top",
                ),
                dict(
                    text=f"Total Words: {openness_result['Total Words']}",
                    x=0.8,
                    y=-0.3,
                    showarrow=False,
                    font=dict(size=12, color="black"),
                    align="right",
                    xanchor="center",
                    yanchor="top",
                )
            ],
        )
        st.plotly_chart(fig)
        st.write(f"##### Openness Level is: {openness_result['Openness Level']}")

    openness_data = pd.DataFrame({"Metric": list(openness_result.keys())[:-1], "Value": list(openness_result.values())[:-1]})
    openness_data["Metric"] = openness_data["Metric"].astype(str)
    openness_data["Value"] = pd.to_numeric(openness_data["Value"], errors="coerce")

    st.subheader("Bar Plot")
    fig, ax = mplt.subplots()
    ax.bar(openness_data["Metric"], openness_data["Value"], color="lightblue")
    ax.set_ylabel("Values")
    ax.set_title("Bar Plot of Openness Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Scatter Plot")
    fig, ax = mplt.subplots()
    ax.scatter(openness_data["Metric"], openness_data["Value"], color="green", s=100)
    ax.set_ylabel("Values")
    ax.set_title("Scatter Plot of Openness Metrics")
    st.pyplot(fig)

    st.subheader("Histogram")
    fig, ax = mplt.subplots()
    ax.hist(openness_data["Value"], bins=10, color="purple", edgecolor="brown")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Openness Metric Values")
    st.pyplot(fig)

    st.subheader("Box Plot")
    fig, ax = mplt.subplots()
    sb.boxplot(data=openness_data, x="Metric", y="Value", ax=ax, palette="Set1")
    ax.set_title("Box Plot of Openness Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Line Plot")
    fig, ax = mplt.subplots()
    ax.plot(openness_data["Metric"], openness_data["Value"], marker="o", color="red", linestyle="--")
    ax.set_ylabel("Values")
    ax.set_title("Line Plot of Openness Metrics")
    st.pyplot(fig)

    st.subheader("Interactive Bar Chart")
    fig = px.bar(openness_data, x="Metric", y="Value", color="Metric", title="Openness Bar Chart (Interactive)")
    fig.update_layout(
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig)
else:
    st.write("###### Oops, Visuals Are Unavailable. Please Upload Your Data on the Home Page.")