import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Load and Preprocess Data
@st.cache_data
def load_data():
    return pd.read_csv("GenZ_Health_Insights_BRFFS2023.csv")

df = load_data()

# Categorize BMI
def categorize_bmi(bmi):
    if pd.isnull(bmi): return None
    elif bmi < 18.5: return 'Underweight'
    elif bmi < 25: return 'Normal'
    elif bmi < 30: return 'Overweight'
    else: return 'Obese'

df['BMI_CATEGORY'] = df['BMI'].apply(categorize_bmi)

# 2. Sidebar Filters
st.sidebar.header("Filter Gen Z Respondents")
st.sidebar.markdown("ℹ️ Use filters to explore health trends.")
gender = st.sidebar.selectbox("Gender", ['All'] + sorted(df['GENDER'].dropna().unique().tolist()))
smoker = st.sidebar.selectbox("Smoker", ['All'] + sorted(df['SMOKER'].dropna().unique().tolist()))
drinker = st.sidebar.selectbox("Drinker", ['All'] + sorted(df['DRINKER'].dropna().unique().tolist()))
exercise = st.sidebar.selectbox("Exercise", ['All'] + sorted(df['EXERCISE'].dropna().unique().tolist()))

# Apply filters
filtered_df = df.copy()
if gender != 'All':
    filtered_df = filtered_df[filtered_df['GENDER'] == gender]
if smoker != 'All':
    filtered_df = filtered_df[filtered_df['SMOKER'] == smoker]
if drinker != 'All':
    filtered_df = filtered_df[filtered_df['DRINKER'] == drinker]
if exercise != 'All':
    filtered_df = filtered_df[filtered_df['EXERCISE'] == exercise]

filtered_df = filtered_df.dropna(subset=["MENTHLTH"])

# Title
st.title("🧠 Gen Z Health Habits Dashboard")
st.markdown("Explore mental health patterns by gender, lifestyle, and BMI (BRFSS 2023)")
st.metric("Sample Size", len(filtered_df))

# 3 & 4. Visualizations and Data Table with Tabs
tab1, tab2 = st.tabs(["📊 Visualizations", "📄 Data Table"])

# --- Tab 1: Visualizations ---
with tab1:
    # Visualization 1: Bar chart by gender
    gender_avg = filtered_df.groupby("GENDER")["MENTHLTH"].mean().reset_index()
    fig1 = px.bar(
        gender_avg, x="GENDER", y="MENTHLTH", color="GENDER", text_auto=".2f",
        title="Avg Poor Mental Health Days by Gender",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig1.update_layout(xaxis_title="", yaxis_title="Days", title_x=0.5)
    st.plotly_chart(fig1, use_container_width=True)

    # Visualization 2: Bar chart by BMI category
    bmi_avg = (
        filtered_df.dropna(subset=["BMI_CATEGORY", "MENTHLTH"])
        .groupby("BMI_CATEGORY")["MENTHLTH"]
        .mean()
        .reindex(['Underweight', 'Normal', 'Overweight', 'Obese'])
        .reset_index()
    )
    fig2 = px.bar(
        bmi_avg, x="BMI_CATEGORY", y="MENTHLTH", color="BMI_CATEGORY", text_auto=".2f",
        title="Avg Mental Health by BMI Category",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig2.update_layout(xaxis_title="BMI Category", yaxis_title="Days", title_x=0.5)
    st.plotly_chart(fig2, use_container_width=True)

    # Visualization 3: Histogram
    fig3 = px.histogram(
        filtered_df,
        x="MENTHLTH",
        nbins=30,
        color="GENDER",
        hover_data=["BMI", "EXERCISE", "DRINKER"],
        title="Distribution of Poor Mental Health Days by Gender",
        marginal="rug"
    )
    fig3.update_layout(xaxis_title="Poor Mental Health Days", yaxis_title="Count", title_x=0.5)
    st.plotly_chart(fig3, use_container_width=True)

# --- Tab 2: Data Table ---
with tab2:
    st.dataframe(filtered_df)
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Filtered Data as CSV", data=csv, file_name="genz_filtered.csv")
st.caption("📊 Data source: CDC BRFSS 2023 (Behavioral Risk Factor Surveillance System)")
