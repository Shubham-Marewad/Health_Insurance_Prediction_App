##🏥 Health Insurance Premium Prediction

A Streamlit web application that predicts health insurance premiums based on user inputs such as age, gender, BMI, children, and smoking status. This project demonstrates machine learning deployment with a professional-grade, clean, and minimal UI design.

📌 Features

✅ Predicts health insurance premium using a trained ML model
✅ Clean & professional business-style UI
✅ Dropdowns for gender and smoking status (instead of text input)
✅ Displays prediction in a popup modal for better UX
✅ Sidebar with BMI categories and reference info
✅ Risk assessment insights based on BMI and smoking habits
✅ Responsive layout (desktop & mobile friendly)

🛠️ Tech Stack

Python 3.x

Streamlit – UI framework

scikit-learn / ML Model – Training the premium prediction model

pickle – Saving/loading trained model

📂 Project Structure
health_insurance_premium_prediction/
│── model.pkl                 # Trained ML model
│── app.py                    # Streamlit app (main script)
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
│── data/                     # (Optional) Dataset used for training
│── notebooks/                # (Optional) Model training notebooks

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/health-insurance-premium-prediction.git
cd health-insurance-premium-prediction

2️⃣ Create Virtual Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

🧠 Model Details

Algorithm Used: Linear Regression / Random Forest (based on training choice)

Input Features:

Age

Gender (Male/Female)

BMI

Number of Children

Smoker (Yes/No)

Output: Predicted Health Insurance Premium (in USD)

📊 Example Prediction

Input:

Age: 35

Gender: Male

BMI: 28.5

Children: 2

Smoker: No

Output:

Predicted Premium: $12,350.75

📜 Disclaimer

This tool is for educational purposes only.
Predictions are based on a simplified ML model and should not be used for real financial or medical decisions.

🤝 Contribution

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit pull requests.

📧 Contact

Developed by [Your Name]

GitHub: Shubham-Marewad

Email: shubhamreddy170311@gmail.com
