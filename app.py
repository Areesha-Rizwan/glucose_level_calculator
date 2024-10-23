import streamlit as st

# Set a page title and favicon
st.set_page_config(page_title="Glucose Level & HbA1c Estimation", page_icon="💉", layout="centered")

# Use some custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #4A90E2;
            text-align: center;
        }
        .sub-title {
            font-size: 1.5em;
            color: #555;
            text-align: center;
        }
        .advice-box {
            background-color: #f0f8ff;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #4A90E2;
            font-size: 1.2em;
        }
        .footer {
            text-align: center;
            color: gray;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# Display the main title with large font and color
st.markdown('<div class="main-title">🩸 Blood Glucose & HbA1c Estimator</div>', unsafe_allow_html=True)

# Add a brief description
st.markdown('<div class="sub-title">Easily calculate your estimated HbA1c and get personalized health advice based on your blood glucose levels.</div>', unsafe_allow_html=True)

# Use columns to organize the layout
col1, col2 = st.columns([2, 1])

with col1:
    # User input section
    st.subheader("Enter your average blood glucose level (mg/dL):")
    glucose = st.number_input("Average Blood Glucose", min_value=0, step=1)

with col2:
    st.image("https://image.shutterstock.com/image-vector/glucose-meter-icon-vector-illustration-260nw-1403768747.jpg", width=150)

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

if glucose > 0:
    # Calculate and display estimated HbA1c
    hba1c = calculate_hba1c(glucose)
    st.write(f"### Your Estimated HbA1c: `{hba1c}%`")
    
    # Provide health advice based on glucose levels with styled advice box
    advice = health_advice(glucose)
    st.markdown(f'<div class="advice-box">**Health Advice:** {advice}</div>', unsafe_allow_html=True)
else:
    st.write("Please enter your average blood glucose level to get results.")

# Footer section
st.markdown('<div class="footer">Note: This app is for educational purposes only and should not replace professional medical advice.</div>', unsafe_allow_html=True)
