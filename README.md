# SmartSpend – Personal Finance Tracker with Prescriptive Analytics

Overview
SmartSpend is a prescriptive analytics application designed to help users move beyond simply tracking expenses and toward making better financial decisions. Instead of only showing historical spending, the app provides actionable recommendations based on a user’s income and spending behavior.

I chose this problem because many students and early-career professionals track expenses but struggle to understand what actions they should take to improve their financial health.

---

## Problem & Value Proposition
Many personal finance tools focus on visualization and reporting, but they stop short of telling users *what to do next*. As a result, users are left with insights but no guidance.

**SmartSpend solves this by:**
- Identifying overspending patterns
- Comparing spending to income-based thresholds
- Prescribing specific actions users can take to improve outcomes

This makes the tool especially useful for students and young professionals managing a limited budget.

---

## Analytics & Prescriptive Approach
The app uses a rule-based prescriptive analytics approach:

1. Expense data is aggregated by category.
2. Spending is evaluated relative to monthly income.
3. Predefined financial thresholds are applied:
   - Rent > 40% of income
   - Food > 30% of income
   - Entertainment > 15% of income
4. When thresholds are exceeded, the app generates actionable recommendations such as reducing spending by a certain percentage.

This approach demonstrates how analytics can directly support decision-making rather than just reporting past behavior.

---

## Working Prototype
The application is deployed as a live Streamlit app and functions as a working prototype:
- Users upload their own expense CSV file
- Users input their monthly income
- The app dynamically generates insights and recommendations

**Live App:**  
👉 [https://https://smartspend-financialtracker.streamlit.app/](https://smartspend-financialtracker.streamlit.app/)

---

## Demo Video below
Here is a short video which  demonstrates the app’s functionality and prescriptive logic.
👉 https://www.loom.com/share/e524ddaecbf14d7eb5521d25190696eb

---

## Technology Stack
- Python
- Streamlit
- Pandas
- GitHub
- Streamlit Community Cloud

---

## Screenshots
<img width="985" height="575" alt="Screenshot 2025-12-12 at 10 23 11 PM" src="https://github.com/user-attachments/assets/d61a0d94-2d88-434b-9917-19dd8653ca40" />
<img width="1032" height="880" alt="Screenshot 2025-12-12 at 10 21 02 PM" src="https://github.com/user-attachments/assets/314291f4-bbb2-4109-9d25-b82967b93d9d" />
<img width="1205" height="869" alt="Screenshot 2025-12-12 at 10 21 59 PM" src="https://github.com/user-attachments/assets/e494e392-4da8-4b86-91ff-d81c0401a308" />
<img width="705" height="684" alt="Screenshot 2025-12-12 at 9 32 22 PM" src="https://github.com/user-attachments/assets/1cb1e5df-28da-45c5-bf0f-8dc8608a9d7b" />


---

## Future Improvements
If expanded further, this project could include:
- Personalized savings goals
- Predictive expense forecasting
- Optimization-based budget allocation
- Category-level budget customization

---

## Conclusion
SmartSpend demonstrates how prescriptive analytics can transform raw financial data into actionable decisions. While the prototype is intentionally simple, it highlights the core logic behind decision-support systems and provides a strong foundation for future development.


