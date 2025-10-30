# 🤖 Streamlit Chatbot using Machine Learning (Naive Bayes)

A simple **AI-powered chatbot** built with **Python**, **Scikit-learn**, and **Streamlit**.  
This project uses a **Naive Bayes text classification model** to understand user input and respond intelligently based on predefined intents.

---

## 🧠 Project Overview

This chatbot reads data from an `intents.json` file, which contains:
- **Tags** (intent categories)
- **Patterns** (possible user inputs)
- **Responses** (bot replies)

Using **CountVectorizer**, it converts text into numerical features and trains a **Multinomial Naive Bayes model** to classify new messages into the correct intent.

The **Streamlit interface** provides a simple chat-style UI where users can interact with the bot in real-time.

---

## 🧩 Features

- 💬 Interactive chat interface with Streamlit  
- 🧠 Machine learning model trained on `intents.json`  
- ⚙️ Text preprocessing using **CountVectorizer**  
- 🤓 Classification powered by **Multinomial Naive Bayes**  
- 🎯 Real-time user–bot interaction  
- 🔁 Context memory (chat history stored using `st.session_state`)

---

## 🧾 Tech Stack

| Component | Library / Tool |
|------------|----------------|
| Frontend UI | Streamlit |
| ML Model | Scikit-learn (MultinomialNB) |
| Text Processing | CountVectorizer |
| Data Source | intents.json |
| Programming Language | Python |

---

## 🚀 How to Run the Chatbot

1. **Install dependencies**
   ```bash
   pip install streamlit scikit-learn
