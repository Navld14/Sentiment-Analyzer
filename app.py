import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stTextArea textarea {
            background-color: #1a1a1a;
            color: #f0f0f0;
            border: 1px solid #333;
            border-radius: 10px;
            font-size: 16px;
        }

        .result-card {
            background: #1a1a1a;
            border-radius: 14px;
            padding: 24px;
            margin-top: 20px;
            border: 1px solid #2a2a2a;
        }

        .sentiment-label {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 6px;
        }

        .subtext {
            color: #888;
            font-size: 14px;
        }

        .metric-box {
            background: #222;
            border-radius: 10px;
            padding: 16px;
            text-align: center;
        }

        .metric-value {
            font-size: 28px;
            font-weight: 700;
            color: #fff;
        }

        .metric-label {
            font-size: 12px;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
    </style>
""", unsafe_allow_html=True)


def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive 😊"
        color = "#22c55e"
    elif polarity < -0.1:
        label = "Negative 😞"
        color = "#ef4444"
    else:
        label = "Neutral 😐"
        color = "#f59e0b"

    return {
        "label": label,
        "color": color,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
    }


def polarity_gauge(polarity, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=polarity,
        number={"font": {"color": color, "size": 28}},
        gauge={
            "axis": {"range": [-1, 1], "tickcolor": "#555", "tickfont": {"color": "#888"}},
            "bar": {"color": color},
            "bgcolor": "#1a1a1a",
            "bordercolor": "#333",
            "steps": [
                {"range": [-1, -0.1], "color": "#2a1010"},
                {"range": [-0.1, 0.1], "color": "#1a1a10"},
                {"range": [0.1, 1], "color": "#0a1a0a"},
            ],
        },
        title={"text": "Polarity Score", "font": {"color": "#888", "size": 14}},
        domain={"x": [0, 1], "y": [0, 1]},
    ))

    fig.update_layout(
        paper_bgcolor="#1a1a1a",
        font={"color": "#fff"},
        height=220,
        margin=dict(t=40, b=10, l=20, r=20),
    )
    return fig


# ── UI ──────────────────────────────────────────────────────────────────────
st.markdown("## 🧠 Sentiment Analyzer")
st.markdown("<p class='subtext'>Type or paste any text below — reviews, tweets, feedback, anything.</p>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_area(
    label="",
    placeholder="e.g. The product was absolutely amazing, I loved every bit of it!",
    height=160,
    label_visibility="collapsed"
)

analyze_btn = st.button("Analyze Sentiment →", use_container_width=True, type="primary")

if analyze_btn:
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        result = get_sentiment(user_input)

        st.markdown("---")
        st.markdown(f"""
            <div class='result-card'>
                <div class='sentiment-label' style='color:{result["color"]}'>{result["label"]}</div>
                <div class='subtext'>Based on polarity and subjectivity scores</div>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class='metric-box' style='margin-top:16px'>
                    <div class='metric-value' style='color:{result["color"]}'>{result["polarity"]}</div>
                    <div class='metric-label'>Polarity (-1 to 1)</div>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='metric-box' style='margin-top:16px'>
                    <div class='metric-value'>{result["subjectivity"]}</div>
                    <div class='metric-label'>Subjectivity (0 to 1)</div>
                </div>
            """, unsafe_allow_html=True)

        st.plotly_chart(polarity_gauge(result["polarity"], result["color"]), use_container_width=True)

        with st.expander("📖 What do these scores mean?"):
            st.markdown("""
            **Polarity** measures how positive or negative the text is:
            - `1.0` → very positive
            - `0.0` → neutral
            - `-1.0` → very negative

            **Subjectivity** measures how opinion-based the text is:
            - `0.0` → completely factual
            - `1.0` → completely subjective / opinion-based
            """)

st.markdown("---")
st.markdown("<p class='subtext' style='text-align:center'>Built with Python · TextBlob · Streamlit · Plotly</p>", unsafe_allow_html=True)
