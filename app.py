import streamlit as st
import pandas as pd

st.set_page_config(page_title="SmartSpend", layout="centered")

st.title("💰 SmartSpend: Personal Finance Tracker")
st.write("Upload your expense data and receive personalized recommendations.")

uploaded_file = st.file_uploader("Upload your expense CSV file", type=["csv"])

income = st.number_input("Enter your monthly income ($)", min_value=0)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Expense Data")
    st.dataframe(df)

    total_spend = df["amount"].sum()
    st.metric("Total Monthly Spending", f"${total_spend:.2f}")

    category_summary = df.groupby("category")["amount"].sum().reset_index()

    st.subheader("📈 Spending by Category")
    st.bar_chart(category_summary.set_index("category"))

    st.subheader("🧠 Prescriptive Recommendations")

    if income > 0:
        rent = category_summary.loc[category_summary["category"] == "Rent", "amount"].sum()
        food = category_summary.loc[category_summary["category"] == "Food", "amount"].sum()
        entertainment = category_summary.loc[category_summary["category"] == "Entertainment", "amount"].sum()

        if rent > 0.4 * income:
            st.warning("🏠 Rent exceeds 40% of your income. Consider downsizing or finding a roommate.")

        if food > 0.3 * income:
            st.warning("🍔 Food spending is high. Reducing food expenses by 15% could save money.")

        if entertainment > 0.15 * income:
            st.warning("🎮 Entertainment spending is high. Cutting back by 20% could improve savings.")

        if rent <= 0.4 * income and food <= 0.3 * income and entertainment <= 0.15 * income:
            st.success("✅ Your spending looks balanced. Keep it up!")

    else:
        st.info("Enter income to receive recommendations.")
