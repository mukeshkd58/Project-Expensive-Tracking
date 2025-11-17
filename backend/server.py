from fastapi import FastAPI, HTTPException
# FastAPI ka use app banane ke liye hota hai.
# HTTPException ka use error messages bhejne ke liye hota hai jab kuch galat ho jaye (jaise database kaam na kare).

from datetime import date
# date ka use hum dates handle karne ke liye karte hain (jaise 2025-11-09).

import db_helper
# Ye ek custom Python file hai (tumhare project ke andar hogi) jo database ke saath kaam karti hai.
# Isme aise functions honge jaise fetch_expenses_for_date(), insert_expense(), etc.

from typing import List
# List ka matlab hota hai “list of items”.
# Example: [1, 2, 3] ek list hai. 
# Hum isko type ke taur par use karte hain jab hum multiple cheezen bhejna chahein (jaise expenses ki list).

from pydantic import BaseModel
# BaseModel FastAPI mein data validation ke liye use hota hai.
# Ye check karta hai ke user ne sahi format mein data bheja hai ya nahi (jaise amount number hai ya string?).

app = FastAPI()
# Ye line ek FastAPI app object banati hai.
# Isse hum server chala sakte hain aur routes define kar sakte hain (jaise /expenses, /analytics, etc).

class Expense(BaseModel):
    amount: float
    category: str
    notes: str
# Ye ek data model (schema) hai jiska naam Expense hai.
# Ye define karta hai ke ek expense (kharcha) kaisa dikhega:
# amount: float → kharche ki amount (decimal ya number)
# category: str → kis type ka expense hai (jaise "Food", "Travel", "Rent")
# notes: str → extra information (jaise “Lunch with friends”)
# FastAPI is model ka use data validate karne ke liye karega.
#Example:
# {
#   "amount": 100.5,
#   "category": "Food",
#   "notes": "Lunch"
# }

class DateRange(BaseModel):
    start_date: date
    end_date: date
# Ye ek aur model hai, jisme user ek date range dega — start aur end date ke beech mein analytics karne ke liye.
#Example:
# {
#   "start_date": "2025-11-01",
#   "end_date": "2025-11-09"
# }

@app.get("/expenses/{expense_date}", response_model= List[Expense])
def get_expenses(expense_date: date):
# Ye ek API route define karta hai:
# Jab koi GET request /expenses/2025-11-09 pe bhejega,
# to ye function chalega.
# expense_date URL ke andar likhi hui date hoti hai.
# response_model=List[Expense] ka matlab hai hum ek list of Expense objects return karenge.
    
    expenses = db_helper.fetch_expenses_for_date(expense_date)
# Ye line database se data laati hai (function fetch_expenses_for_date ke zariye).
# Ye us date ke saare expenses laata hai.
    if expenses is None:
        raise HTTPException(status_code=500, details="Failed to retrieve expense summary from the database.")
    return expenses
# Agar sab kuch sahi hai, to expenses ka data return kar diya jaata hai.
# Ye FastAPI automatically JSON format mein bhej deta hai.
#Example response:
# [
#   {"amount": 50, "category": "Food", "notes": "Lunch"},
#   {"amount": 20, "category": "Transport", "notes": "Bus fare"}
# ]

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date, expenses:List[Expense]):
# Ye ek POST route hai (data bhejne ke liye).
# Isme user ek specific date ke liye poore expenses update/add kar sakta hai.
# Parameters:
# expense_date → URL se milti hai
# expenses → JSON body ke andar se (List of Expense objects)

    db_helper.delete_expenses_for_date(expense_date)
# Pehle purane expenses delete kiye jaate hain us date ke liye.
# Matlab — “nayi list se replace karo purane data ko.”
    
    for expense in expenses:
        db_helper.insert_expense(
            expense_date,  # yahan expense.date nahi tha — use expense_date from URL
            expense.amount,
            expense.category,
            expense.notes
        )
# Fir loop chalakar har expense ko database mein insert kiya jaata hai.
# Har item ke andar se:
# amount
# category
# notes
# nikal kar insert_expense() function ko bheje jaate hain.
    return {"message": "Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
# Ye ek aur POST route hai /analytics/ ke liye.
# User start aur end date dega (jaise 1 November se 9 November tak).
# Server un dates ke expenses ka summary (analysis) banayega.

    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
# Ye database se summary data laata hai — jaise har category ka total expense.
#Example data:
# [
#   {"category": "Food", "total": 300},
#   {"category": "Travel", "total": 200}
# ]
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")
    total = sum([row['total'] for row in data])
# Ye line total expenses ka sum nikalti hai sab categories ka mila kar.
# Example:
# 300 + 200 = 500
    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
# Ye loop har category ke liye ek percentage nikalta hai.
# Example:
# Food → 300/500 × 100 = 60%
# Travel → 200/500 × 100 = 40%
# Aur sab ko ek dictionary mein store karta hai.

#Final breakdown:
# {
#   "Food": {"total": 300, "percentage": 60.0},
#   "Travel": {"total": 200, "percentage": 40.0}
# }
    return breakdown

# Line-by-Line Explanation
# @app.post("/analytics/")
# Ye FastAPI decorator hai.
# Ye batata hai ke jab koi user POST request bheje URL /analytics/ par,
# to niche likha hua function get_analytics() chale.
# POST request ka matlab hai: user kuch data bhej raha hai (yahan date range).

#def get_analytics(date_range: DateRange):
#Ye function define karta hai get_analytics.
# Iska ek input parameter hai date_range, jo DateRange model par based hai.

# DateRange model humne pehle define kiya tha:

# class DateRange(BaseModel):
#     start_date: date
#     end_date: date


# 🔸 Matlab: user request body mein JSON format mein start aur end date bhejta hai.

# 🧩 Example Request:

# {
#   "start_date": "2025-11-01",
#   "end_date": "2025-11-09"
# }


# To FastAPI automatically is JSON ko DateRange object mein badal deta hai,
# jisse hum date_range.start_date aur date_range.end_date use kar sakte hain.

# 3️⃣
# data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)


# 👉 Ye line database helper (db_helper) file ke function ko call karti hai.

# Iska kaam hota hai:

# Database mein jaakar,

# start_date aur end_date ke beech ke expenses grouped by category nikalna.

# 🧩 Example: Agar tumhare expenses table mein ye data hai 👇

# Date	Category	Amount
# 2025-11-02	Food	50
# 2025-11-02	Travel	30
# 2025-11-03	Food	100
# 2025-11-03	Rent	200

# To ye function return karega kuch aisa data:

# [
#   {"category": "Food", "total": 150},
#   {"category": "Travel", "total": 30},
#   {"category": "Rent", "total": 200}
# ]


# Matlab har category ka total nikal diya gaya hai.

# 4️⃣
# if data is None:
#     raise HTTPException(status_code=500, details="Failed to retrieve expense summary from the database.")


# 👉 Ye ek error handling step hai.

# Agar data ka value None aata hai (matlab database ne kuch nahi bheja ya query fail hui),
# to program yahan ruk jaata hai aur ek HTTP 500 (Server Error) return karta hai.

# 🔹 500 error = “Server side problem”.

# 🧩 Example Response:

# {
#   "detail": "Failed to retrieve expense summary from the database."
# }


# (Note: yahan details likha hai, lekin sahi parameter detail hota hai FastAPI mein.)

# 5️⃣
# total = sum([row['total'] for row in data])


# 👉 Ye line sabhi categories ke total expenses ka grand total nikalti hai.

# 🔹 Kaise?
# Ye data list ke andar har row ke 'total' value ko collect karta hai aur sabka sum karta hai.

# 🧩 Example:

# data = [
#   {"category": "Food", "total": 150},
#   {"category": "Travel", "total": 30},
#   {"category": "Rent", "total": 200}
# ]


# → [row['total'] for row in data] ban jaata hai [150, 30, 200]

# → sum([150, 30, 200]) = 380

# So total = 380

# 🔸 Purpose: ye humko overall kharche ka sum deta hai — taake hum percentage nikal sakein.

# 6️⃣
# breakdown = {}


# 👉 Ye ek empty dictionary banata hai jisme hum category-wise analysis rakhenge.
# Jaise ek chhoti summary report.

# Example:

# {
#   "Food": {"total": 150, "percentage": 39.47},
#   "Travel": {"total": 30, "percentage": 7.89},
#   "Rent": {"total": 200, "percentage": 52.63}
# }


# Abhi khaali hai, niche wale loop mein fill hoga.

# 7️⃣
# for row in data:


# 👉 Ye loop har category ke data par chalega.
# Matlab agar data mein 3 categories hain (Food, Travel, Rent),
# to ye loop 3 baar chalega — har category ke liye ek baar.

# 8️⃣
#     percentage = (row['total']/total)*100 if total != 0 else 0


# 👉 Ye line har category ka percentage share nikalti hai.

# Formula:

# percentage
# =
# category ka total
# overall total
# ×
# 100
# percentage=
# overall total
# category ka total
# 	​

# ×100

# Example:

# Food → (150 / 380) × 100 = 39.47%

# Travel → (30 / 380) × 100 = 7.89%

# Rent → (200 / 380) × 100 = 52.63%

# 🔸 if total != 0 else 0 ka matlab hai:
# Agar total 0 hua (matlab koi expense nahi mila),
# to division na kare (kyunki zero se divide karna error deta hai),
# us case mein percentage = 0.

# 9️⃣
#     breakdown[row['category']] = {
#         "total": row['total'],
#         "percentage": percentage
#     }


# 👉 Ye line har category ka result breakdown dictionary mein store kar deti hai.

# Example:

# Pehle iteration:
# breakdown['Food'] = {"total": 150, "percentage": 39.47}

# Doosre iteration:
# breakdown['Travel'] = {"total": 30, "percentage": 7.89}

# Teesre iteration:
# breakdown['Rent'] = {"total": 200, "percentage": 52.63}

# To final output ho jaata hai:

# {
#   "Food": {"total": 150, "percentage": 39.47},
#   "Travel": {"total": 30, "percentage": 7.89},
#   "Rent": {"total": 200, "percentage": 52.63}
# }

# 🔟
# return breakdown


# 👉 Finally, ye dictionary response ke taur par bhej di jaati hai.
# FastAPI automatically isse JSON format mein convert karke user ko bhejta hai.

# 🧩 Final Output Example (JSON response):

# {
#   "Food": {"total": 150, "percentage": 39.47},
#   "Travel": {"total": 30, "percentage": 7.89},
#   "Rent": {"total": 200, "percentage": 52.63}
# }

# 🧾 Summary in Plain Words
# Step	What It Does	Why It’s Needed
# 1	@app.post("/analytics/")	Defines the route (URL endpoint)
# 2	date_range: DateRange	Gets start and end dates from user
# 3	db_helper.fetch_expense_summary()	Fetches category totals from DB
# 4	if data is None	Error handling if DB fails
# 5	total = sum(...)	Finds total expense of all categories
# 6	breakdown = {}	Creates empty dictionary for results
# 7	for row in data:	Loops through each category
# 8	percentage = ...	Calculates percentage share of each category
# 9	breakdown[...] = {...}	Stores total + percentage for each category
# 10	return breakdown	Sends final result back as JSON
# 💡 In Short

# Yeh function ek expense analyzer hai.
# Wo start aur end date ke beech:

# Database se expenses laata hai

# Har category ka total nikalta hai

# Grand total calculate karta hai

# Har category ka percentage share nikalta hai

# Aur final breakdown report bana ke return karta hai ✅