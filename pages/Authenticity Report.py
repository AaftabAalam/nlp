import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as mplt
import seaborn as sb
import plotly.graph_objects as go
from metrics import detect_authenticity, authenticity_keywords


st.title("Authenticity Breakdown Report")

if 'chat_data' in st.session_state:
    chat_data = st.session_state["chat_data"]

    result = detect_authenticity(chat_data, authenticity_keywords)

    st.write("### Authenticity Metrics")
    st.table(result.items())

    data = pd.DataFrame.from_dict(
        {"Metric": list(result.keys()), "Value": list(result.values())}
    )

    st.write("### Metrics Visualization")
    st.bar_chart(data.set_index("Metric"))

    # This is pie chart code
    if result["Total Words"] == 0:
        st.write("### No Authenticity Words Are Detected")
        st.write(result["Message"])
    else:
        st.write("### Pie Chart")
        chart_data = pd.DataFrame({
            "Metric": ["Authenticity Keywords", "Totoal Words"],
            "Count": [result["Authenticity Keywords"], result["Total Words"] - result["Authenticity Keywords"]]
        })

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=chart_data["Metric"],
                    values=chart_data["Count"],
                    textinfo="label+percent",
                    insidetextorientation="radial",
                    marker=dict(colors=["green", "orange"]),
                )
            ]
        )

        fig.update_layout(
            title="Authenticity Word Distribution",
            annotations=[
                dict(
                    text=f"Authenticity Keywords: {result['Authenticity Keywords']}",
                    x=0.8,
                    y=-0.2,
                    showarrow=False,
                    font=dict(size=12, color="black"),
                    align="right",
                    xanchor="center",
                    yanchor="top",
                ),
                dict(
                    text=f"Total Words: {result['Total Words']}",
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
        st.write(f"##### Authenticity Level is: {result['Authenticity Level']}")

    # This is Bar plot code
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

    # This is scatter plot code
    st.subheader("Scatter Plot")
    fig, ax = mplt.subplots()
    ax.scatter(data["Metric"], data["Value"], color="orange", s=100)
    ax.set_ylabel("Values")
    ax.set_title("Scatter Plot of Metrics")
    st.pyplot(fig)

    # This is histogram pot code
    st.subheader("Histogram")
    fig, ax = mplt.subplots()
    ax.hist(data["Value"], bins=10, color="green", edgecolor="brown")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Metric Values")
    st.pyplot(fig)

    # This is box plot code
    st.subheader("Box Plot")
    fig, ax = mplt.subplots()
    sb.boxplot(data=data, x="Metric", y="Value", ax=ax, palette="Set2")
    ax.set_title("Box Plot of Metrics")
    mplt.xticks(rotation=45)
    st.pyplot(fig)

    # This is line plot code
    st.subheader("Line Plot")
    fig, ax = mplt.subplots()
    ax.plot(data["Metric"], data["Value"], marker="o", color="purple", linestyle="--")
    ax.set_ylabel("Values")
    ax.set_title("Line Plot of Metrics")
    st.pyplot(fig)

    # This is interactive Bar Plot code
    st.subheader("Interactive Bar Chart")
    fig = px.bar(data, x="Metric", y="Value", color="Metric", title="Bar Chart (Interactive)")
    fig.update_layout(
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig)
else:
    st.write("###### Oops, Visuals Are Unavailable, Please Upload Your Data At Home Page.")