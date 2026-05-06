import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Cancer Risk Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI-Based Cancer Risk Prediction and Prevention Support System")

st.markdown("""
### Educational Prototype
This application provides AI-assisted cancer risk awareness and prevention support based on user lifestyle and health-related inputs.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Patient Information")

    age = st.slider("Age", 10, 100, 30)

    weight = st.number_input("Weight (kg)", 20, 200, 60)

    height = st.number_input("Height (cm)", 100, 250, 170)

    smoking = st.selectbox(
        "Smoking Habit",
        ["Non-Smoker", "Occasional Smoker", "Regular Smoker"]
    )

with col2:
    st.subheader("Lifestyle & Medical History")

    family_history = st.selectbox(
        "Family History of Cancer",
        ["No", "Yes"]
    )

    exercise = st.selectbox(
        "Physical Activity Level",
        ["Low", "Moderate", "High"]
    )

    alcohol = st.selectbox(
        "Alcohol Consumption",
        ["No", "Occasionally", "Frequently"]
    )

# BMI Calculation
height_m = height / 100
bmi = weight / (height_m ** 2)

st.subheader("BMI Analysis")

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

st.info(f"Calculated BMI: {bmi:.2f} ({bmi_status})")

# Risk Score Logic
risk_score = 0

if age > 50:
    risk_score += 2

if smoking == "Regular Smoker":
    risk_score += 3

if family_history == "Yes":
    risk_score += 3

if exercise == "Low":
    risk_score += 2

if alcohol == "Frequently":
    risk_score += 2

if bmi >= 30:
    risk_score += 2

st.divider()

st.subheader("📊 Cancer Risk Prediction Result")

if risk_score >= 9:
    risk_level = "High Risk"
    st.error("High Cancer Risk")
    recommendation = """
    • Consult healthcare professionals immediately  
    • Schedule regular cancer screening  
    • Improve lifestyle habits  
    • Reduce smoking and alcohol intake  
    """
elif risk_score >= 5:
    risk_level = "Moderate Risk"
    st.warning("Moderate Cancer Risk")
    recommendation = """
    • Maintain regular health checkups  
    • Improve diet and exercise habits  
    • Monitor lifestyle risk factors  
    """
else:
    risk_level = "Low Risk"
    st.success("Low Cancer Risk")
    recommendation = """
    • Maintain healthy lifestyle  
    • Continue preventive healthcare practices  
    """

st.markdown("### Prevention Recommendations")
st.markdown(recommendation)

# Chart
chart_data = pd.DataFrame({
    "Category": ["Age", "Smoking", "Family History", "Exercise", "Alcohol", "BMI"],
    "Risk Contribution": [
        2 if age > 50 else 0,
        3 if smoking == "Regular Smoker" else 1,
        3 if family_history == "Yes" else 0,
        2 if exercise == "Low" else 0,
        2 if alcohol == "Frequently" else 0,
        2 if bmi >= 30 else 0
    ]
})

fig = px.bar(
    chart_data,
    x="Category",
    y="Risk Contribution",
    title="Risk Factor Contribution Analysis"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.caption("Disclaimer: This application is developed for educational and awareness purposes only and does not provide medical diagnosis.")
st.divider()

st.subheader("📄 Download Patient Risk Report")

report = f"""
AI-Based Cancer Risk Prediction and Prevention Support Report

Age: {age}
Smoking Habit: {smoking}
Family History: {family_history}
Exercise Level: {exercise}
Alcohol Consumption: {alcohol}

BMI: {bmi:.2f}
Risk Level: {risk_level}

Prevention Recommendations:
{recommendation}

Disclaimer:
This application is developed for educational and awareness purposes only and does not provide medical diagnosis.
"""

st.download_button(
    label="Download Report",
    data=report,
    file_name="Cancer_Risk_Report.txt",
    mime="text/plain"
)