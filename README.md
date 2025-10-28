# Workforce Performance & Sentiment Analysis

This project simulates and analyzes a synthetic workforce to provide insights into employee performance, productivity, and engagement. It demonstrates an **end-to-end workflow** from synthetic data generation to sentiment analysis and interactive Power BI dashboards.

---

## **Project Overview**

The main goal of this project is to generate realistic synthetic employee, performance, and feedback data, perform sentiment scoring on textual feedback, and visualize workforce performance and engagement metrics using Power BI. The project demonstrates how HR teams and managers can track efficiency, productivity, and morale in a data-driven way.

---

## **Project Flow & Contents**

### **Code**

- `data_preparation.py`  
  - Generates synthetic datasets for employees, performance, and feedback.  
  - Includes realistic department-level efficiency, weekday-only performance, monthly performance drift, and sentiment variation.  
  - Outputs: `Employee_Master.csv`, `Performance_Data.csv`, `Feedback_Data.csv`.

- `sentiment_analysis.py`  
  - Analyzes the feedback text using TextBlob for sentiment scoring.  
  - Normalizes sentiment scores (0–1) and labels them as Positive, Neutral, or Negative.  
  - Outputs: `Feedback_Data_Scored.csv` and a sentiment summary file for Power BI.  

**Purpose:** Together, these scripts create realistic datasets ready for analysis and visualization in Power BI.

---

### **Datasets**

1. **Employee_Master.csv**  
   - Contains synthetic employee information: ID, Name, Department, Role, Location, Tenure.  
   - Serves as the main table to link performance and feedback data.

2. **Performance_Data.csv**  
   - Contains daily weekday performance from Jan–Sep 2025: Tasks Completed, Hours Worked, Efficiency Score.  
   - Allows analysis of productivity, efficiency trends, and department-level comparisons.

3. **Feedback_Data_Scored.csv**  
   - Contains monthly feedback with sentiment scores and labels.  
   - Enables sentiment analysis at employee, role, and department levels.  

**Purpose:** These three datasets form the **relational model** in Power BI for KPIs, dashboards, and trend analysis.

---

### **Power BI File**

- `Workforce_Sentiment_Analysis.pbix`  
  - Integrates all datasets with relationships:  
    - `Employee_Master[EmployeeID]` → `Performance_Data[EmployeeID]`  
    - `Employee_Master[EmployeeID]` → `Feedback_Data_Scored[EmployeeID]`  
  - Uses DAX measures for dynamic calculations:  
    - Total Tasks, Total Hours, Average Efficiency, Tasks per Hour  
    - Average Sentiment, Count Positive/Negative Feedback, Positive %, Net Sentiment  
  - Interactive dashboards include KPI cards, trend charts, scatter plots, and heatmaps.

---

### **Findings Document**

- `Workforce_Performance_Analysis.docx`  
  - Summarizes all insights derived from the Power BI dashboards.  
  - Highlights department and role-level efficiency, sentiment trends, and actionable recommendations.  

---

## **Key Insights & Analysis Capabilities**

- High productivity in IT and Operations; moderate efficiency in HR and Marketing  
- Overall positive employee sentiment (avg. 0.62) with net sentiment 0.41  
- Efficiency shows minor seasonal variation; sentiment remains stable  
- Employee-level scatter plots identify areas where engagement can boost performance  
- Dashboards allow filtering by department, role, location, and individual employee

**Practical Uses:**  
- HR analytics, workforce planning simulations, and performance monitoring  
- Employee sentiment and engagement analysis  
- Training for Power BI, DAX, and data visualization workflows

---

## **Why This Project is Useful**

- **Realistic yet safe:** Synthetic datasets avoid sensitive data issues  
- **End-to-end workflow:** From data generation to sentiment scoring to dashboards  
- **Actionable insights:** Identifies efficiency gaps and engagement opportunities  
- **Power BI ready:** Clean CSVs and defined relationships for quick dashboard creation

---

This project demonstrates how organizations can combine **synthetic data, sentiment analysis, and performance metrics** into a full workforce analytics system, providing actionable insights for managers, HR teams, and analysts.
