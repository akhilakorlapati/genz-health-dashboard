# 🧠 Gen Z Health Habits Dashboard

This Streamlit dashboard explores the mental health and lifestyle patterns of Gen Z respondents using data from the 2023 Behavioral Risk Factor Surveillance System (BRFSS). It provides interactive filters, insightful visualizations, and downloadable data to understand how gender, smoking, drinking, exercise, and BMI relate to mental health outcomes.

---

## Features

- **Interactive Sidebar Filters**: Filter data by gender, smoking, drinking, and exercise status
- **Visual Insights**:
  - Average poor mental health days by gender
  - Average poor mental health days by BMI category
  - Distribution histogram of mental health days
- **BMI Categorization**: Groups into Underweight, Normal, Overweight, Obese
- **Data Preview**: Filtered table view with CSV export button
- **Organized Layout**: Visuals and table separated into clean `st.tabs()`

---

## Dataset

- **Source**: [CDC BRFSS 2023](https://www.cdc.gov/brfss/)
- **Subset**: Gen Z respondents (approx. age 18–26)
- **Final Data File**: `GenZ_Health_Insights_BRFFS2023.csv`

---

## How to Run the App

1. **Clone this repository**:
   ```bash
   git clone https://github.com/akhilakorlapati/genz-health-dashboard.git
   cd genz-health-dashboard
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

### Project Structure
```
├── app.py                                # Streamlit dashboard
├── GenZ_Health_Insights_BRFFS2023.csv    # Cleaned dataset used by the app
├── genz_preprocessing_and_modeling.ipynb # Notebook with data cleaning and model training
├── requirements.txt                      # Python packages needed to run the app
└── README.md                             # Project overview and documentation
```

## Preprocessing & Modeling Notebook
The file genz_preprocessing_and_modeling.ipynb includes:
Selecting relevant health columns from BRFSS 2023
Mapping responses (e.g., smoker, drinker, exerciser)
Analyzing and cleaning data
Training models like Logistic Regression and XGBoost
Exporting the cleaned dataset to CSV for use in the dashboard
This notebook is not required to run the dashboard, but it shows how the data was prepared.

## Last Updated
July 03, 2025.

## Credits
Built by **Akhila Korlapati**  
Made using **Streamlit**, **Plotly**, and **CDC BRFSS 2023** public data.
> This project is for educational and analytical purposes only. All data is publicly sourced from the CDC BRFSS.
