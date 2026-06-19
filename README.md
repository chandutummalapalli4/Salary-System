# 💼 Salary Calculator System (Python Project)

## 📌 Objective

This project is a beginner-friendly Python program that calculates an employee’s net salary by including allowances and deducting tax based on salary conditions.

---

## 🧠 Features

* Takes basic salary as input
* Validates input (salary should not be negative)
* Calculates:

  * HRA (20% of basic salary)
  * DA (10% of basic salary)
* Computes:

  * Gross Salary = Basic + HRA + DA
* Applies tax:

  * 10% tax if gross salary > 50,000
  * 5% tax otherwise
* Displays:

  * Basic salary
  * HRA
  * DA
  * Gross salary
  * Tax amount (with percentage)
  * Net salary

---

## 🛠️ Technologies Used

* Python (Basic)
* Conditional Statements (`if`, `elif`, `else`)
* Input/Output handling

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the file as `salary_calculator.py`
3. Run the program:

```id="6y0g3g"
python salary_calculator.py
```

---

## 💻 Sample Output

```id="ht2y0h"
Enter Salary Amount: 60000

Basic Salary: 60000
HRA: 12000
DA: 6000
Gross Salary: 78000
Tax (10%): 7800
Net Salary: 70200
```

---

## ⚠️ Validation

* If salary is less than 0:

  * Output: `Invalid salary`

---

## 🚀 Future Improvements

* Add bonuses and deductions
* Support multiple employees
* Export salary report
* Convert into GUI or web application

---

## 👨‍💻 Author

* Chandu Tummlapalli
