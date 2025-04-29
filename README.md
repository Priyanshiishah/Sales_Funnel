# 📩 Sales & Marketing CRM Tool

An easy-to-use, lightweight CRM built with **Python**, **Streamlit**, **SQLite**, and **Mailgun**.  
This tool allows you to **capture leads**, **automatically send follow-up emails**, and **manage your sales funnel** through a clean dashboard.

---

## 🚀 Features

- Submit and track new leads
- Automatic email follow-ups using Mailgun API
- Search leads by email
- View all leads in a clean CRM dashboard
- Update lead statuses (New → Contacted → Interested → Closed)
- Lightweight and low-code, perfect for startups or small teams

---

## 🛠️ Tech Stack

| Purpose                 | Technology |
|--------------------------|------------|
| Frontend / UI            | Streamlit  |
| Backend / Server         | Python     |
| Database                 | SQLite     |
| Email Automation         | Mailgun API |
| Environment Management   | python-dotenv |

---

## 📦 Project Structure

```
sales_tool/
│
├── app/
│   ├── db.py          # Database connection and queries
│   ├── emailer.py     # Mailgun integration for sending emails
│   └── config.py      # Environment variables loader
│
├── data/
│   └── leads.sqlite   # SQLite database
│
├── templates/
│   └── (optional) email templates
│
├── main.py            # Streamlit app entry point
├── requirements.txt   # Python dependencies
├── .env               # API keys and secrets (not uploaded to GitHub)
└── README.md          # Project documentation
```

---

## 🧹 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sales_tool.git
cd sales_tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up `.env` File

Create a `.env` file in the project root with your Mailgun details:

```
MAILGUN_API_KEY=your-mailgun-api-key
MAILGUN_DOMAIN=sandboxxxxxxx.mailgun.org
MAILGUN_POSTMASTER=postmaster@sandboxxxxxxx.mailgun.org
```

> ⚡️ **Note:** If you're using a Mailgun Sandbox domain, make sure to verify your recipient email address.

### 4. Initialize the Database

You can manually initialize the SQLite database by running the app once, or insert sample leads using the provided SQL script.

```bash
sqlite3 data/leads.sqlite < sample_leads.sql
```

*(If you created a sample_leads.sql)*

### 5. Run the Application

```bash
streamlit run main.py
```

Your CRM dashboard should now be running at:  
📍 `http://localhost:8501`

---

## 🎯 Future Enhancements

- Inline editing of lead status in the dashboard
- Email open/click tracking
- Lead scoring and prioritization
- Multi-user login system
- Integration with Calendly for demo scheduling

---

## 📚 Acknowledgments

- [Streamlit](https://streamlit.io/) – Rapid UI development
- [Mailgun](https://www.mailgun.com/) – Email sending made easy
- [SQLite](https://sqlite.org/) – Lightweight database for local apps

---

## ✨ Personal Note

This project was a wonderful learning experience combining frontend simplicity, backend logic, API integrations, and database management.  
I'm excited to continue improving it and exploring even more automation features in the future! 🚀
