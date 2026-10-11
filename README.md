# 🧠 Sentiment Analyzer

A simple yet powerful sentiment analysis web app built with Python and Streamlit. Enter any text — a review, tweet, feedback, or sentence — and instantly get a sentiment breakdown.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?style=flat-square&logo=streamlit)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-green?style=flat-square)

---

🌐 **Live Demo:** [Try it here](https://sentiment-analyzer-b9xuxmxbt6aqhraty4t5g3.streamlit.app/)

## 🚀 Features

- **Real-time sentiment detection** — Positive, Negative, or Neutral
- **Polarity score** — Ranges from -1 (very negative) to +1 (very positive)
- **Subjectivity score** — Ranges from 0 (factual) to 1 (opinionated)
- **Interactive gauge chart** — Visual representation of polarity using Plotly
- **Clean dark UI** — Built with custom Streamlit CSS

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| TextBlob | NLP & sentiment scoring |
| Streamlit | Web app framework |
| Plotly | Interactive gauge chart |

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Navld14/sentiment-analyzer.git
cd sentiment-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download TextBlob corpora
python -m textblob.download_corpora

# 4. Run the app
streamlit run app.py
```

---

## 🧪 Example Inputs

| Text | Sentiment |
|------|-----------|
| "This product is absolutely amazing!" | Positive 😊 |
| "Worst experience I've ever had." | Negative 😞 |
| "The package arrived on Tuesday." | Neutral 😐 |

---

## 📁 Project Structure

```
sentiment-analyzer/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## 🙋 Author

**Naveen Ladha**
[GitHub](https://github.com/Navld14)

---

