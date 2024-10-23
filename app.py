import streamlit as st

# Function to calculate estimated HbA1c from average blood glucose
def calculate_hba1c(avg_glucose):
    hba1c = (avg_glucose + 46.7) / 28.7
    return round(hba1c, 2)

# Function to provide health advice based on blood glucose levels
def health_advice(glucose):
    if glucose < 70:
        return "Low blood sugar (Hypoglycemia). Please eat something with sugar and consult your doctor."
    elif 70 <= glucose <= 140:
        return "Normal blood sugar levels. Maintain a balanced diet and healthy lifestyle."
    elif 140 < glucose <= 199:
        return "Prediabetic range. Consider lifestyle changes, exercise, and consult a healthcare professional."
    else:
        return "High blood sugar (Hyperglycemia). This could indicate diabetes. Consult a healthcare provider."

# Streamlit app layout
st.title("Blood Glucose Level Assessment and HbA1c Estimation")

st.subheader("Enter your average blood glucose level (mg/dL):")
glucose = st.number_input("Average Blood Glucose", min_value=0, step=1)

if glucose > 0:
    # Calculate and display estimated HbA1c
    hba1c = calculate_hba1c(glucose)
    st.write(f"**Estimated HbA1c:** {hba1c}%")
    
    # Provide health advice based on glucose levels
    advice = health_advice(glucose)
    st.write(f"**Health Advice:** {advice}")
else:
    st.write("Please enter your average blood glucose level to get results.")

# Footer
st.write("Note: This app is for educational purposes only and should not replace professional medical advice.")
