# Workforce Performance & Sentiment Analysis

This project simulates and analyzes a synthetic workforce to provide insights into employee performance, productivity, and engagement. By generating realistic employee, performance, and feedback data, it serves as a comprehensive example of how HR and management teams can track workforce efficiency and morale using data-driven approaches in Power BI.

---

## Project Overview

The main goal of this project is to create a realistic, synthetic dataset that mimics real-world workforce dynamics and provide tools to analyze performance and sentiment trends. The project integrates Python-based data generation, sentiment analysis, and Power BI-ready datasets to enable interactive dashboards for workforce analytics.

---

## Project Contents

**Code**  
- `data_preparation.py` – Generates synthetic employee, performance, and feedback data  
- `sentiment_analysis.py` – Calculates sentiment scores from feedback and prepares datasets for analysis  

**Datasets**  
- `Employee_Master.csv` – Employee demographics and role information  
- `Performance_Data.csv` – Daily performance metrics for each employee  
- `Feedback_Data_Scored.csv` – Monthly feedback with sentiment scores and labels  

**Power BI File**  
- `Workforce_Sentiment_Analysis.pbix` – Interactive dashboards for workforce performance and sentiment analysis  

**Findings Document**  
- `Workforce_Performance_Analysis.docx` – Summary of key insights and analysis results  

---

## Dataset Components

1. **Employee Master Data**  
Contains information on 200 synthetic employees, including Employee ID and name, Department and role, Office location, and Tenure in years. This dataset provides the foundation for linking performance and feedback data.

2. **Performance Data**  
Daily weekday performance data from January to September 2025, including Tasks completed, Hours worked, and Efficiency scores (reflecting department-level variation and monthly trends).  

3. **Feedback Data**  
Monthly employee feedback with positive, neutral, or negative sentiments, including Feedback text sampled from realistic statements, Sentiment scoring using TextBlob, Normalized sentiment scores (0–1), and Sentiment labels (Positive, Neutral, Negative).  

4. **Sentiment Summary**  
Aggregated counts of positive, neutral, and negative feedback, ready for dashboard KPIs and visualizations.

---

## Data Loading and Power BI Model

The three datasets (`Employee_Master.csv`, `Performance_Data.csv`, `Feedback_Data_Scored.csv`) are loaded into Power BI with relationships managed as follows:  
- `Employee_Master[EmployeeID]` → `Performance_Data[EmployeeID]`  
- `Employee_Master[EmployeeID]` → `Feedback_Data_Scored[EmployeeID]`  

**DAX Measures**  

**Performance Metrics (Performance_Data)**  
- Total Tasks Completed = SUM(Performance_Data[TasksCompleted])  
- Total Hours Worked = SUM(Performance_Data[HoursWorked])  
- Average Efficiency = AVERAGE(Performance_Data[EfficiencyScore])  
- Tasks per Hour = DIVIDE([Total Tasks], [Total Hours], 0)  

**Feedback & Sentiment (Feedback_Data_Scored)**  
- Avg Sentiment = AVERAGE(Feedback_Data_Scored[Sentiment_Score_Normalized])  
- Count Positive Feedback = CALCULATE(COUNTROWS(Feedback_Data_Scored), Feedback_Data_Scored[Sentiment_Label] = "Positive")  
- Count Negative Feedback = CALCULATE(COUNTROWS(Feedback_Data_Scored), Feedback_Data_Scored[Sentiment_Label] = "Negative")  
- Positive % = DIVIDE([Count Positive Feedback], COUNTROWS(Feedback_Data_Scored), 0)  
- Net Sentiment = [Positive %] - DIVIDE([Count Negative Feedback], COUNTROWS(Feedback_Data_Scored), 0)  

These measures allow dynamic dashboards that respond to slicers and filters, enabling analysis by department, role, or employee.

---

## Analysis Capabilities

- Workforce-Level KPIs: Total tasks, hours, efficiency, average sentiment, and net sentiment  
- Department & Role Insights: Comparative analysis across departments and roles  
- Time Trends: Monthly tracking of performance and morale  
- Employee-Level Insights: High-performing employees and correlation between efficiency and sentiment  
- Visual Analytics: KPI cards, trend charts, scatter plots, heatmaps, role-specific comparisons  

---

## Key Insights Derived

- IT and Operations are top-performing departments in efficiency and productivity  
- Average efficiency is moderate (0.55), HR and Marketing are lower  
- Overall sentiment is positive (avg. 0.62), net sentiment 0.41  
- Sentiment remains stable; efficiency shows minor seasonal variation  
- Scatter plots of efficiency vs sentiment help identify areas for engagement improvement  

---

## Practical Applications

- HR analytics and workforce planning simulations  
- Department and role-level performance monitoring  
- Employee sentiment analysis to inform engagement strategies  
- Interactive dashboards for management decision-making  
- Training for Power BI, DAX, and data visualization  

---

## Why This Project is Useful

- Realistic yet safe: Synthetic data simulates real workforce patterns without sensitive info  
- End-to-end workflow: From data generation to dashboard visualization  
- Actionable insights: Highlights performance gaps and engagement opportunities  
- Power BI ready: Clean, relational CSVs for seamless integration  

---

This project demonstrates how organizations can combine synthetic data, performance metrics, and sentiment analysis to build a comprehensive workforce analytics system, providing actionable insights for managers, HR teams, and analysts.
