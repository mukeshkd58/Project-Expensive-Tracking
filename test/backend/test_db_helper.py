
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend import db_helper
def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"

def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-12-31")
    assert len(summary) == 0

# Yeh ek Python import path adjustment line hai — iska matlab hai ke hum manually ek folder (directory) ko Python ke import search path mein add kar rahe hain taake hum us folder se modules import kar saken.
# Ab isko part by part samajhte hain 

# 🔹 1. sys.path

# sys ek Python ka built-in module hai jo interpreter ke sath interact karne ke liye use hota hai.

# sys.path ek list hai jisme Python wo sab folders rakhta hai jahan wo modules ko search karta hai jab aap import something likhte ho.

# 👉 Agar aap koi file import karte ho aur Python ke paas uska path sys.path mein nahi hai, to ModuleNotFoundError aata hai.

# Example:

# import sys
# print(sys.path)


# Ye list dikhata hai ke Python kin folders mein modules dhund raha hai.

# 🔹 2. sys.path.append(...)

# append() ka matlab hota hai list mein ek naya element add karna.

# Yahan hum ek naya folder path add kar rahe hain jahan hamare project ke extra modules hain.

# Purpose:
# Taki Python us folder ke andar ke modules ko bhi recognize kar sake aur unhe import kar sake.

# 🔹 3. os.path.abspath(...)

# os.path ek module hai jo file paths ke sath kaam karta hai.

# abspath() ka matlab hai absolute path banana (full path jahan tak file hoti hai, like C:/Users/.../project/...).

# 👉 Ye relative path (jaise ../..) ko complete full system path mein badal deta hai.

# 🔹 4. os.path.join(os.path.dirname(__file__), '../../')

# Ye thoda complex lagta hai, lekin simple hai: ye path ko build kar raha hai.

# __file__ = current Python file ka path (jis file mein yeh code likha hai).

# os.path.dirname(__file__) = current file ka folder (directory) name deta hai.

# '../../' = iska matlab hai "do folders upar jao".

# Example samjho:

# Project/
# │
# ├── backend/
# │   └── db_helper.py
# │
# └── Tests/
#     └── backend/
#         └── test_db_helper.py  ← yahan yeh line likhi hai


# Agar aapka test file Tests/backend/test_db_helper.py mein hai,
# to os.path.dirname(__file__) = Tests/backend
# aur '../../' jane ka matlab hai → 2 folders upar jao → Project/

# 🔹 5. Overall Meaning

# Sab kuch mila kar:

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


# ka matlab hai:

# “Current file ke directory se do level upar jao (../../), uska absolute path banao, aur us path ko Python ke module search path (sys.path) mein add kar do.”

# 🔹 6. Example (Visual)

# Agar current file ka path hai:

# C:\Code\Project\Tests\backend\test_db_helper.py


# To ye line karegi:

# os.path.dirname(__file__) → C:\Code\Project\Tests\backend
# os.path.join(..., '../../') → C:\Code\Project\
# os.path.abspath(...) → C:\Code\Project\
# sys.path.append(...) → add this path to Python's module search list


# Ab aap db_helper ko directly import kar sakte ho:

# from backend import db_helper


# without ModuleNotFoundError.

# 🔹 Summary Table
# Part	Meaning
# sys.path	Python ke import search directories
# append()	ek naya directory add karta hai
# os.path.dirname(__file__)	current file ka folder
# '../../'	2 folders upar jaana
# os.path.abspath()	full path banata hai
# Overall	project root folder ko import path mein add karta hai