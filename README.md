
# 🍲 AI Recipe Generator

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?logo=flask)](https://flask.palletsprojects.com/)
[![Deployment](https://img.shields.io/website?url=https%3A%2F%2Frecipe-generator.onrender.com)](https://recipe-generator.onrender.com)

This is an **AI-powered recipe generator** built using Flask and OpenAI. You simply provide the ingredients you have, and it returns two recipe suggestions — each with a fun name and a quirky fun fact!

🟢 **Live Demo:** [https://recipe-generator.onrender.com](https://recipe-generator.onrender.com)

---

## 🛠️ Tools & Technologies Used

- **Python 3.10+**
- **Flask** – Web framework for Python
- **HTML/CSS** – Frontend templating using Jinja
- **OpenAI API / boltiotai** – AI recipe suggestions using GPT
- **Render** – Cloud platform used to deploy the application

---

## ⚙️ How It Works

1. User enters a list of ingredients in a form.
2. Flask backend captures the input and sends it to OpenAI's GPT-3.5 API (via `boltiotai` or `openai`).
3. The API generates two creative recipe names (with funny aliases), steps to cook, and a fun fact.
4. The result is displayed back to the user on the webpage.

---

## 📚 What I Learned

- Building a web application using **Flask**
- Templating with **Jinja2** and **HTML forms**
- Making API requests to **OpenAI GPT models**
- Managing environment variables securely
- Deploying a full-stack app to **Render**
- Writing clean and maintainable backend code

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-recipe-generator.git
cd ai-recipe-generator
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure Python 3.10+ is installed.

### 3. Add Environment Variable

Create a `.env` file and add your OpenAI key (or set it in your system):

```env
OPENAI_API_KEY=your-openai-api-key
```

Alternatively, set it directly in `app.py` if you’re testing:

```python
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### 4. Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📦 Deployment

The project is deployed on **Render**.

### Render Deployment Settings:

* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `python app.py`
* **Environment Variable**: `OPENAI_API_KEY`

---
