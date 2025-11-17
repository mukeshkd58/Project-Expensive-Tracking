import streamlit as st
# Is line se hum Streamlit library use kar sakte hain.
# Jaise Streamlit ke functions — st.button, st.table, st.bar_chart, etc.
# Streamlit se hum web page pe buttons, charts aur tables bana sakte hain.

from datetime import datetime
# Yeh line Python ke datetime module se datetime class import karti hai.
# Iska kaam hota hai date aur time handle karna, jaise 2024-08-01 ko date format mein likhna.

import requests
# Yeh line requests library import karti hai.
# Iska use hota hai server se data mangwane (API request) ke liye.
# Jaise hum kisi website ya backend se data lete hain.

import pandas as pd
# Yeh line pandas library import karti hai, jise short form mein pd likha gaya hai.
# Pandas ek library hai jo tables aur data analysis ke liye use hoti hai.
# Yeh Excel sheet jaisa data handle karti hai.

API_URL = "http://127.0.0.1:8000"
# Yeh ek variable hai jisme humne API ka address likha hai.
# 127.0.0.1 ka matlab hai local computer (tumhara apna PC).
# Port 8000 wo jagah hai jahan tumhara FastAPI backend chal raha hai.

def analytics_tab():
# Yeh ek function define kar raha hai jiska naam hai analytics_tab.
# Jab yeh function chalega, tab yeh Streamlit page pe analytics section dikhayega.

    col1, col2 = st.columns(2)
# Streamlit mein st.columns(2) ka matlab hai 2 columns banana (side by side).
# col1 left side ka column hai, aur col2 right side ka.
    
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
# Yeh left column mein ek date picker box banata hai jisme user Start Date choose karega.
# Default value di gayi hai 1 August 2024.

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))
# Yeh right column mein ek date picker box banata hai jisme user End Date choose karega.
# Default value hai 5 August 2024.    

    if st.button("Get Analytics"):
# Yeh ek button banata hai jiska naam hai “Get Analytics”.
# Jab user is button ko click karega, tab neeche ka code chalega.
        
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
# Yahaan humne ek dictionary banayi hai jisme humne start aur end date likhi hai.
# strftime("%Y-%m-%d") date ko proper format mein convert karta hai jaise 2024-08-01.
# Yeh format server ko samajhne ke liye zaroori hota hai.

        response = requests.post(f"{API_URL}/analytics/", json=payload)
# Yeh line ek POST request bhejti hai backend server ko (FastAPI).
# Address hoga http://127.0.0.1:8000/analytics/.
# Aur saath mein hum dates ka data (payload) bhej rahe hain.
        
        response = response.json()
# Jab server se reply aata hai, wo usually JSON format mein hota hai (like a dictionary).
# Is line se hum us reply ko Python dictionary mein convert kar lete hain.

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }
# Yeh line ek naya data dictionary banati hai jise hum Pandas ke DataFrame mein use karenge.
# response.keys() se hum categories ke naam le rahe hain (jaise “Food”, “Travel”).
# Har category ke andar se hum total aur percentage value nikaal rahe hain.
# Matlab example:
# response = {
#     "Food": {"total": 200, "percentage": 40},
#     "Travel": {"total": 300, "percentage": 60}
# }
# Toh output data hoga:
# Category   Total   Percentage
# Food       200     40
# Travel     300     60

        df = pd.DataFrame(data)
# Yeh line data dictionary ko ek table (DataFrame) mein convert karti hai.
# Jaise Excel sheet ke rows aur columns.
        
        df_sorted = df.sort_values(by="Percentage", ascending=False)
# Yeh table ko Percentage ke according sort karta hai (zyada se kam tak).
# Taaki top spending categories sabse pehle dikhein.      
       
        st.subheader("Expense Breakdown By Category")
# Yeh Streamlit page pe ek heading dikhata hai — "Expense Breakdown By Category".
        
        st.bar_chart(df_sorted.set_index("Category")["Percentage"])
# Yeh ek bar chart banata hai jisme x-axis pe category aur y-axis pe percentage dikhaya jata hai.
# .set_index("Category") ka matlab hai category ko chart ke labels bana do.
        
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
# Yeh dono lines numbers ko 2 decimal places tak format karti hain.
# Jaise 123.4567 ko 123.46 bana diya jaye.

        st.table(df_sorted)
# Yeh Streamlit pe ek table show karta hai jisme sorted data hota hai.
# Table mein columns honge: Category, Total, Percentage.

# Summary:

# Yeh pura code:

# User se date range leta hai.

# Us range ka data backend (API) se mangta hai.

# Data ko table aur bar chart mein dikhata hai.