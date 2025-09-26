import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    
    
    .result-box {
        background: linear-gradient(90deg, #2E86AB, #A23B72);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #2E86AB, #A23B72);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f0f2f6, #ffffff);
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">Health Insurance Premium Predictor</h1>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<h2 class="sub-header">Personal Information</h2>', unsafe_allow_html=True)
    
    # Age input with validation
    age = st.number_input(
        "Age (years)",
        min_value=18,
        max_value=100,
        value=30,
        step=1,
        help="Enter your age in years (18-100)"
    )
    
    # Gender selection
    gender = st.selectbox(
        "Gender",
        options=["Male", "Female"],
        help="Select your gender"
    )
    
    # BMI input with validation
    bmi = st.number_input(
        "BMI (Body Mass Index)",
        min_value=10.0,
        max_value=50.0,
        value=25.0,
        step=0.1,
        format="%.1f",
        help="Enter your BMI (typically between 15-40)"
    )

with col2:
    st.markdown('<h2 class="sub-header">Family & Lifestyle</h2>', unsafe_allow_html=True)
    
    # Number of children
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0,
        step=1,
        help="Number of children covered by the insurance"
    )
    
    # Smoker status
    smoker = st.selectbox(
        "Smoking Status",
        options=["No", "Yes"],
        help="Do you smoke?"
    )
    
    # Empty space for alignment
    st.write("")
    st.write("")



# Center the predict button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_button = st.button('Predict Premium', use_container_width=True)

# Prediction logic
if predict_button:
    try:
        # Load the model
        model = pickle.load(open('model.pkl', 'rb'))
        
        # Convert categorical variables to numerical
        gender_encoded = 0 if gender.upper() == 'MALE' else 1
        smoker_encoded = 0 if smoker.upper() == 'NO' else 1
        
        # Prepare input for prediction
        X_test = [[age, gender_encoded, bmi, children, smoker_encoded]]
        
        # Make prediction
        prediction = model.predict(X_test)[0]
        
        # Display result
        st.markdown(f"""
        <div class="result-box">
             Your Estimated Health Insurance Premium: <br>
            <span style="font-size: 2rem;">₹{prediction:,.2f}</span> per year
        </div>
        """, unsafe_allow_html=True)
        
        # Additional insights
        st.markdown('<h3 class="sub-header">Premium Breakdown</h3>', unsafe_allow_html=True)
        
        insight_col1, insight_col2, insight_col3 = st.columns(3)
        
        with insight_col1:
            st.metric(
                label="Age Factor", 
                value=f"{age} years",
                help="Older age typically increases premium"
            )
        
        with insight_col2:
            st.metric(
                label="BMI Status", 
                value=f"{bmi:.1f}",
                delta="Healthy" if 18.5 <= bmi <= 24.9 else "Monitor",
                help="BMI outside normal range may affect premium"
            )
        
        with insight_col3:
            st.metric(
                label="Risk Factor", 
                value="High" if smoker == "Yes" else "Low",
                delta="Smoker" if smoker == "Yes" else "Non-smoker",
                help="Smoking significantly impacts insurance costs"
            )
        
        # Show input summary
        with st.expander(" Input Summary"):
            summary_data = {
                "Parameter": ["Age", "Gender", "BMI", "Children", "Smoking Status"],
                "Value": [f"{age} years", gender, f"{bmi:.1f}", children, smoker]
            }
            df_summary = pd.DataFrame(summary_data)
            st.table(df_summary)
            
    except FileNotFoundError:
        st.error("❌ Model file 'model.pkl' not found. Please ensure the model file is in the same directory.")
    except Exception as e:
        st.error(f"❌ An error occurred during prediction: {str(e)}")

# Sidebar with additional information
with st.sidebar:
    st.markdown("### 📚 About This Tool")
    st.markdown("""
    This tool uses machine learning to predict health insurance premiums based on:
    
    - **Age**: Older individuals typically pay higher premiums
    - **Gender**: May affect premium calculations
    - **BMI**: Higher BMI can indicate health risks
    - **Children**: More dependents increase coverage costs
    - **Smoking**: Significantly impacts premium due to health risks
    """)
    
    st.markdown("### BMI Reference")
    st.markdown("""
    - **Underweight**: BMI < 18.5
    - **Normal**: BMI 18.5 - 24.9
    - **Overweight**: BMI 25 - 29.9
    - **Obese**: BMI ≥ 30
    """)
    
    st.markdown("### ⚠️ Disclaimer")
    st.markdown("""
    This is a predictive tool for estimation purposes only. 
    Actual insurance premiums may vary based on additional 
    factors not considered in this model.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666666;'>Made with ❤️ using Streamlit | Health Insurance Premium Predictor</p>", 
    unsafe_allow_html=True
)