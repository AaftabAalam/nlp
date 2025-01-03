import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as mplt
import seaborn as sb
import plotly.graph_objects as go
from metrics1 import detect_high_risk_words, high_risk_words

st.title("High-Risk Words Usage Breakdown Report")

if "chat_data" in st.session_state:
    chat_data = st.session_state["chat_data"]

    result = detect_high_risk_words(chat_data, high_risk_words)

    # Table
    st.write("### High-Risk Words Metrics")
    st.table(result.items())

    # Metric Visualization
    data = pd.DataFrame.from_dict(
        {"Metric": list(result.keys()), "Value": list(result.values())}
    )

    st.write("### Metrics Visualization")
    st.bar_chart(data.set_index("Metric"))

    # Pie Chart
    if result["High-Risk Words"] == 0:
        st.write("### No High-Risk Words Detected")
        st.write(result["Message"])
    else:
        st.write("### Distribution of High-Risk Words")
        
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["High-Risk Words", "Other Words"],
                    values=[result["High-Risk Words"], result["Total Words"] - result["High-Risk Words"]],
                    textinfo="label+percent",
                    insidetextorientation="radial",
                    marker=dict(colors=["red", "green"]),
                )
            ]
        )
        fig.update_layout(
            title="High-Risk Word Distribution",
            annotations=[
                dict(
                    text=f"Risk Level: {result['Risk Level']}",
                    x=0.8,
                    y=-0.2,
                    showarrow=False,
                    font=dict(size=12, color="black"),
                    align="right",
                    xanchor="center",
                    yanchor="top",
                )
            ],
        )
        st.plotly_chart(fig)
        st.write(f"##### Risk Level: {result['Risk Level']}")

    # Bar plot Code
    data = pd.DataFrame({"Metric": list(result.keys())[:-1], "Value": list(result.values())[:-1]})
    data["Metric"] = data["Metric"].astype(str)
    data["Value"] = pd.to_numeric(data["Value"], errors="coerce")

    st.subheader("Bar Plot")
    fig, ax = mplt.subplots()
    ax.bar(data["Metric"], data["Value"], color="skyblue")
    ax.set_ylabel("Values")
    ax.set_title("Bar Plot of Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    # Scatter Plot Code
    st.subheader("Scatter Plot")
    fig, ax = mplt.subplots()
    ax.scatter(data["Metric"], data["Value"], color="orange", s=100)
    ax.set_ylabel("Values")
    ax.set_title("Scatter Plot of Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    # Histogram Plot Code
    st.subheader("Histogram")
    fig, ax = mplt.subplots()
    ax.hist(data["Value"], bins=10, color="green", edgecolor="black")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Metric Values")
    st.pyplot(fig)

    # Box Plot Code
    st.subheader("Box Plot")
    fig, ax = mplt.subplots()
    sb.boxplot(data=data, x="Metric", y="Value", ax=ax, palette="Set2")
    ax.set_title("Box Plot of Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    # Line Plot Code
    st.subheader("Line Plot")
    fig, ax = mplt.subplots()
    ax.plot(data["Metric"], data["Value"], marker="o", color="purple", linestyle="--")
    ax.set_ylabel("Values")
    ax.set_title("Line Plot of Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    # Interactive Bar Chart
    st.subheader("Interactive Bar Chart")
    fig = px.bar(data, x="Metric", y="Value", color="Metric", title="Bar Chart (Interactive)")
    st.plotly_chart(fig)
else:
    st.write("###### Oops, Visuals Are Unavailable, Please Upload Your Data At Home Page.")