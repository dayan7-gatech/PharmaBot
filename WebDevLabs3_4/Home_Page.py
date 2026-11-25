import streamlit as st

st.set_page_config(
    page_title="PharmaBot",
    page_icon="💊"
)

# Title of App
st.title("Prescription Drug Shortages💊")

st.image("images/pharmacy.jpg", use_container_width=True)



st.header("CS 1301")
st.subheader("Team 88, Web Development - Section A")
st.subheader("Dora and Megan")




# Introduction
st.header("Welcome to Our Project!")

st.write("""Our project explores prescription drug shortages and the importance
         of pharmaceutical supply chains. We aim to help users understand
         medication shortages and how they affect pharmacies, patients,
         and the healthcare system.
         
         This project combines pharmacy and industrial engineering by
         exploring the challenges of medication and availability, distribution
         and supply chain management.""")

st.header("Explore Our App!")

st.write("""
1. **Data Page 📊:** Explore FDA drug shortage data through
interactive charts and data summaries.
2. **PharmaBot 🤖:** Chat with our AI-powered assistant to
learn more about prescription drug shortages, pharmacy,
and pharmaceutical supply chains."""
)

st.info(""" Use the sidebar to navigate between the pages!""")

st.subheader("💡 Example Questions")

st.write(""" - Why do prescription drug shortages happen?
- How do drug shortages affect patients?
- What role does the FDA play in drug shortages?
- How do pharmacies manage medication shortages?
- How can industrial engineering improve pharmaceutical supply chains?
- How can manufacturers prevent drug shortages?
""")

st.warning(""" This application is for educational purposes only and
does not provide medical advice.""")

