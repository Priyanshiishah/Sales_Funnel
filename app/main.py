import streamlit as st
import pandas as pd
from db import init_db, save_lead, get_all_leads, get_one_lead
from emailer import send_email

st.title("📩 Sales & Marketing CRM")

init_db()

st.header("📝 Add a New Lead")
with st.form("lead_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit Lead")
    if submitted:
        save_lead(name, email, message)
        # After saving lead:
        send_email(email, "Thanks for reaching out!", "Hi there! We'll contact you shortly.")
        st.success("Lead submitted and email sent!")

st.header("📊 CRM Dashboard")

# --- Search Section ---
st.subheader("🔍 Search for a Lead by Email")

with st.form("search_form"):
    search_email = st.text_input("Enter email to search")
    search_submitted = st.form_submit_button("Search")

    if search_submitted:
        if search_email:
            lead = get_one_lead(search_email)
            if lead:
                st.success("Lead found!")
                df = pd.DataFrame(lead, columns=["Name", "Email", "Message", "Status", "Last Contacted"])
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("No lead found with that email.")
        else:
            st.error("Please enter an email to search.")

# --- All Leads Section ---
leads = get_all_leads()

if leads:
    # Convert leads list to a pandas DataFrame
    df = pd.DataFrame(leads, columns=["Name", "Email", "Message", "Status", "Last Contacted"])

    # Display as a table
    st.dataframe(df, use_container_width=True)
else:
    st.info("No leads yet!")
