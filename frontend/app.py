# import streamlit as st
# Ye line Streamlit library ko import karti hai.
# Streamlit ek tool hai jisse hum Python code likh kar web app bana sakte hain (jaise dashboard ya form).
# st short form hai Streamlit ke liye.
# Matlab: hum st.header() likhenge instead of streamlit.header().

# import pandas as pd #to create dateframe
# Ye line Pandas library import karti hai aur uska short name pd rakhti hai.
# Pandas data ke saath kaam karne ke liye hoti hai — jaise table banana (DataFrame), sort karna, analyze karna, etc.

# Text elements
# st.header("Streamlit Core Features")
# st.subheader("Text Elements")
# st.text("This is a simple text elemment.")
# st.header() → bada heading banata hai
# Example: “Streamlit Core Features” title jaisa bold likha dikhega.
# st.subheader() → chhoti heading banata hai
# “Text Elements” likha thoda chhota heading dikhega.
# st.text() → normal plain text likhta hai
# “This is a simple text element.” ek normal sentence jaisa dikhai dega.
# On screen:
# Streamlit Core Features      ← big heading
# Text Elements                ← smaller heading
# This is a simple text elemment.  ← normal text


# Data display
# st.subheader("Data Display")
# st.write("Here is a simple table:")
# df = pd.DataFrame({
#     "Data": ["2024-08-01", "2024-08-02", "2024-08-03"],
#     "Amount": [250, 134, 340]
# })

# st.table(df)
# Ye Pandas ka DataFrame (table) bana raha hai — ek chhoti si table jisme 2 columns hain:

# Data	Amount
# 2024-08-01	250
# 2024-08-02	134
# 2024-08-03	340
# st.table(df)
# Ye Streamlit function st.table() is DataFrame ko table format mein web page par dikhata hai.

#Charts
# st.subheader("Charts")
# st.line_chart([1, 2, 3, 4])

#User Input
# st.subheader("User Input")
# value = st.slider("Select a value", 0, 100)
# st.write(f"Selected value: {value}")
# 🔸 Summary Table
# Part	Function	Kya karta hai
# st.header()	Text Heading	Bada title show karta hai
# st.text()	Normal Text	Simple line likhta hai
# st.table()	Data Table	Pandas DataFrame ko table mein dikhata hai
# st.line_chart()	Chart	Data ka line chart banata hai
# st.slider()	User Input	User se number input leta hai
# st.write()	Output	Screen par result likhta hai

#added another codes

# st.title("Interactive Widgets Example")

# #checkbox
# if st.checkbox("show/Hide"):
#     st.write("Checkbox is checked!")

# #selectbox
# option = st.selectbox("category", ["Rent", "Food"], label_visibility="collapsed") #agar hum is category wale word ko waha se hatna chahte tu yeh likhe gaye label_visabillity = collapsed
# st.write(f"You selected: {option}")

# #multiselect
# options = st.multiselect("Select multiple numbers", [1, 2, 3, 4])
# st.write(f"You selected: {options}")

#add another code now for the topic(Expense Management: Frontend (Streamlit)
# import streamlit as st
# # Explanation: import matlab hum ek library (toolbox) la rahe hain.
# # streamlit ek library hai jo simple web apps banane ke kaam aati hai.
# # as st matlab ab hum streamlit ko chhota naam st se use karenge (taaki baar-baar lamba naam na likhna pade).

# from datetime import datetime
# # Explanation: from ek built-in module datetime se datetime naam ki cheez le raha hai.
# # datetime date aur time ke sath kaam karne ke liye hota hai (jaise aaj ki date banana).

# import requests
# # Explanation: requests ek library hai jo internet pe server se data lene ya bhejne (GET/POST) ke liye hoti hai.
# # Is se hum apne backend API se expenses la sakte ya bhej sakte hain.


# # Backend API URL
# API_URL = "http://127.0.0.1:8000"
# # ke baad wali line comment hai — sirf insaan padhne ke liye.
# # API_URL ek variable (box) hai jisme server ka address rakha gaya.
# # "http://127.0.0.1:8000" matlab server aapke computer (local) par port 8000 pe chal raha hai. (127.0.0.1 = local host)

# st.title("Expense Tracking System")
# # Streamlit ka title function page pe bada title dikhata hai.
# # "Expense Tracking System" woh text hai jo screen pe heading ban ke aayega.


# # Tabs for navigation
# tab1, tab2 = st.tabs(["Add/Update", "Analytics"])
# # st.tabs do tabs (jaldi change karne wala parts) banata hai.
# # ["Add/Update", "Analytics"] do tab ke labels hain.
# # tab1, tab2 variables hain jo ab in tab blocks ko refer karenge.


# # -----------------------------
# # TAB 1: Add / Update Expenses
# # -----------------------------
# with tab1:
# # with tab1: matlab jo code is block ke neeche hai, woh Add/Update tab ke andar dikhai dega.
# # with ek Python ka way hai kisi context (yahaan tab) ke andar kaam karne ka.

#     # Date selection
#     selected_date = st.date_input(
#         "Enter Date",
#         datetime(2024, 8, 1),
#         label_visibility="collapsed"
#     )
# # selected_date = : hum ek variable bana rahe hain jisme user ne jo date chuni woh store hogi.
# # st.date_input(...) : Streamlit ka function jo user ko date chunne ka calendar dikhata hai.
# # "Enter Date" : yeh label jo calendar ke pass dikh sakta tha (user ko batane ke liye).
# # datetime(2024, 8, 1) : default date set kar raha hai (1 Aug 2024). Agar user kuch na kare toh yeh dikhai dega.
# # label_visibility="collapsed" : label chhupa kar rakhta hai — UI saaf dikhega (label na dikhaye).

#     # Convert date to string for unique keys
#     date_str = selected_date.isoformat()
# # selected_date.isoformat() date ko ek string format "YYYY-MM-DD" mein convert karta hai.
# # date_str variable ab is string ko rakhta hai. Ye unique keys banane mein madad karega (har date ke liye inputs alag ho).

#     # Function to get expenses from backend
#     def get_expenses(selected_date):
# # def se hum function bana rahe hain — ek chhota kaam jo baar-baar use ho sakta.
# # get_expenses(selected_date) naam hai function ka, jo ek date lega aur us date ke expenses backend se la dega.
#         try:
# # try block ka matlab hai "koshish karo" — agar error aaya to except se handle karenge. Ye safe way hai server calls ke liye.
#             response = requests.get(f"{API_URL}/expenses/{selected_date}")
# # requests.get(...) server se GET request bhej raha hai.
# # f"{API_URL}/expenses/{selected_date}" isko f-string kehte hain — variable values ko string ke andar directly daal deta hai.
# # Agar API_URL = "http://127.0.0.1:8000" aur date 2024-08-01 ho, to URL banega http://127.0.0.1:8000/expenses/2024-08-01.
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 st.error("Failed to retrieve expenses from server.")
#                 return []
# # response.status_code == 200 check karta hai ki server ne "OK" bataya ya nahi. 200 matlab success.
# # response.json() server se aaye hue JSON data ko Python object (list/dict) bana deta hai.
# # Agar success hai to woh data return (wapas) kar dete hain.
# # else: matlab agar status 200 nahi, to st.error(...) screen pe error message show karega aur function empty list [] return karega.

#         except Exception as e:
#             st.error(f"Error connecting to API: {e}")
#             return []
# # except Exception as e: agar request bhejne mein koi bhi error aa jaye (internet down, server off), to code yahan aayega.
# # st.error(...) mein error message dikhega (jo e mein aya).
# # Phir empty list [] return kar diya jayega taake baad ka code crash na kare.

#     # Fetch existing expenses for the selected date
#     existing_expenses = get_expenses(selected_date)
# # yahan hum function call kar rahe — get_expenses(selected_date) — aur jo data milega usko existing_expenses variable mein rakh rahe hain.
# # Iska matlab agar pehle se us date pe expenses store hain toh woh aayenge.

#     # Debug info (optional)
#     st.write("Fetched expenses for", selected_date, ":", existing_expenses)
# #st.write screen pe kuch bhi likhne ke liye hota hai.
# #Yeh line basic debugging ke liye hai — developer ko dikhata hai kya data mila. User bhi dekh sakta hai.

#     # Expense categories
#     categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
# # categories ek list (array) hai jisme expense types rakhe gaye — ye selectbox mein options dikhenge.

#     # Expense Form
#     with st.form(key=f"expense_form_{date_str}"):
# # st.form ek form banata hai — form ke andar inputs rakhe jaate hain aur ek submit button hota hai.
# # key=f"expense_form_{date_str}" har date ke liye unique form key banata hai — taake Streamlit ko pata rahe ke kaunse inputs kis date ke liye hain.
#         st.write("### Add / Update Expenses")
# # form ke andar ek chhota heading likhi ja rahi hai — ### Markdown style se thoda chhota heading dikhata hai.

#         # Table headers
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.text("Amount")
#         with col2:
#             st.text("Category")
#         with col3:
#             st.text("Notes")
# # st.columns(3) screen ko 3 vertical columns mein divide karta hai.
# # with col1: ka matlab hai column 1 mein jo items likhenge woh us column mein dikhai denge.
# # st.text("Amount") aur baaki do lines headers dikhate hain: Amount, Category, Notes — ye table ke column titles hain.

#         # Generate form rows
#         for i in range(5):
# # for i in range(5): loop 5 rows banayega (0 se 4 tak). Matlab form mein 5 expense rows hain — user 5 alag entries bhar sakta hai.
#             if i < len(existing_expenses):
#                 amount = existing_expenses[i]["amount"]
#                 category = existing_expenses[i]["category"]
#                 notes = existing_expenses[i]["notes"]
#             else:
#                 amount = 0.0
#                 category = "Shopping"
#                 notes = ""
# # Ye check karta hai: agar existing_expenses mein already koi entry us index i pe hai, to uska data form mein pre-fill (pehle se bhara) rakhe.
# # existing_expenses[i]["amount"] ka matlab us saved item se amount value lena.
# # Agar koi existing data nahi hai to default values set kar de: amount 0.0, category default "Shopping", notes khali string "".

#             col1, col2, col3 = st.columns(3)
# # Har row mein phir se 3 columns banaye jate hain jahan input fields aayenge (Amount, Category, Notes).
#             with col1:
#                 st.number_input(
#                     "Amount",
#                     min_value=0.0,
#                     step=1.0,
#                     value=amount,
#                     key=f"amount_{date_str}_{i}",
#                     label_visibility="collapsed"
#                 )
# # with col1: = pehle column mein input rakhenge.
# # st.number_input(...) numeric input field dikhata hai (user numbers daale).
# # "Amount" label text (hidden because label_visibility="collapsed").
# # min_value=0.0 minimum allowed value 0 (negative allowed nahi).
# # step=1.0 increment step (upar niche karne pe 1 se badhega).
# # value=amount default/initial value (agar existing expense hai to woh dikhayi dega).
# # key=f"amount_{date_str}_{i}" unique key for this specific input; Streamlit ko state track karne mein madad karta hai.
           
#             with col2:
#                 st.selectbox(
#                     "Category",
#                     options=categories,
#                     index=categories.index(category),
#                     key=f"category_{date_str}_{i}",
#                     label_visibility="collapsed"
#                 )
# # st.selectbox(...) dropdown banata hai jisme se user category choose kare.
# # options=categories woh list jo pehle banayi thi.
# # index=categories.index(category) default selected option ka index set karta hai (agar category pre-filled ho to woh select ho).
# # key=... unique id for this selectbox.

#             with col3:
#                 st.text_input(
#                     "Notes",
#                     value=notes,
#                     key=f"notes_{date_str}_{i}",
#                     label_visibility="collapsed"
#                 )
# # st.text_input(...) ek choti text box deta hai jahan user extra notes likh sakta hai.
# # value=notes agar pehle se koi note hai to woh pre-fill ho jayega.
# # key=... unique id for this notes input.

#         # Submit button
#         submit_button = st.form_submit_button("Submit")
# # st.form_submit_button("Submit") form ka submit button banata hai.
# # Jab user ispe click karega tab form ke andar ki sari values ek saath submit hongi.
# # submit_button boolean (True/False) ho jata hai — True jab user ne submit kiya.

#         if submit_button:
# # Agar user ne submit button dabaya to ye block chalayega (form data process karega).
#             # Collect data from form inputs
#             expenses_to_submit = []
#             for i in range(5):
#                 amount_val = st.session_state[f"amount_{date_str}_{i}"]
#                 category_val = st.session_state[f"category_{date_str}_{i}"]
#                 notes_val = st.session_state[f"notes_{date_str}_{i}"]
# # expenses_to_submit = [] ek empty list banayi jisme hum final data append karenge.
# # for i in range(5): phir se har row ke inputs lena.
# # st.session_state[...] Streamlit ke andar raw values fetch karne ka tareeqa — jo keys humne pehle set ki thi unse values milengi.
# # amount_val, category_val, notes_val variables mein woh user-entered values store ho rahi hain.

#                 # Only add non-empty or non-zero records
#                 if amount_val > 0 or notes_val.strip():
#                     expenses_to_submit.append({
#                         "amount": amount_val,
#                         "category": category_val,
#                         "notes": notes_val
#                     })
# # if amount_val > 0 or notes_val.strip(): matlab agar amount zero se zyada ho ya notes mein koi non-space character ho toh record add karo. (faatish: notes_val.strip() spaces hata ke check karta hai agar kuch bach raha hai)
# # expenses_to_submit.append({...}) list mein ek dictionary add karta hai jisme amount, category, notes rakhe jate hain.

#             # Send data to backend
#             try:
#                 res = requests.post(
#                     f"{API_URL}/expenses/{selected_date}",
#                     json=expenses_to_submit
#                 )
# # Ab hum server ko POST request bhejte hain taki data save ho jaye.
# # requests.post(...) server ko data bhejne ka tareeqa.
# # f"{API_URL}/expenses/{selected_date}" woh URL jahan data bhej rahe hain.
# # json=expenses_to_submit body mein JSON format mein data jaa raha hai (server JSON expect karega).

#                 if res.status_code == 200:
#                     st.success("Expenses updated successfully!")
#                 else:
#                     st.error(f"Failed to update expenses: {res.text}")
# # if res.status_code == 200: agar server ne success bataya to st.success(...) green message dikhayega.
# # else: agar koi problem to st.error(...) message dikhayega aur server ka response text (res.text) show karega.

#             except Exception as e:
#                 st.error(f"Error connecting to API: {e}")
# # agar POST request bhejte waqt koi exception (error) aaya — jaise server down, network problem — to ye block chalega aur error message dikhayega.

# # -----------------------------
# # TAB 2: Analytics (placeholder)
# # -----------------------------
# with tab2:
#     st.write("Analytics features coming soon...")

import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()

