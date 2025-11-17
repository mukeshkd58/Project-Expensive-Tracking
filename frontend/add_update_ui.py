import streamlit as st
from datetime import datetime
import requests
API_URL = "http://127.0.0.1:8000"

def add_update_tab():
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )
    date_str = selected_date.isoformat()
    def get_expenses(selected_date):
        try:
            response = requests.get(f"{API_URL}/expenses/{selected_date}")
            if response.status_code == 200:
                return response.json()
            else:
                st.error("Failed to retrieve expenses from server.")
                return []

        except Exception as e:
            st.error(f"Error connecting to API: {e}")
            return []
    existing_expenses = get_expenses(selected_date)
    st.write("Fetched expenses for", selected_date, ":", existing_expenses)
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    with st.form(key=f"expense_form_{date_str}"):
        st.write("### Add / Update Expenses")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                st.number_input(
                    "Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{date_str}_{i}",
                    label_visibility="collapsed"
                )
           
            with col2:
                st.selectbox(
                    "Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{date_str}_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                st.text_input(
                    "Notes",
                    value=notes,
                    key=f"notes_{date_str}_{i}",
                    label_visibility="collapsed"
                )
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            expenses_to_submit = []
            for i in range(5):
                amount_val = st.session_state[f"amount_{date_str}_{i}"]
                category_val = st.session_state[f"category_{date_str}_{i}"]
                notes_val = st.session_state[f"notes_{date_str}_{i}"]
                if amount_val > 0 or notes_val.strip():
                    expenses_to_submit.append({
                        "amount": amount_val,
                        "category": category_val,
                        "notes": notes_val
                    })
            try:
                res = requests.post(
                    f"{API_URL}/expenses/{selected_date}",
                    json=expenses_to_submit
                )

                if res.status_code == 200:
                    st.success("Expenses updated successfully!")
                else:
                    st.error(f"Failed to update expenses: {res.text}")
            except Exception as e:
                st.error(f"Error connecting to API: {e}")

