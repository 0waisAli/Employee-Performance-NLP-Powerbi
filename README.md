# Workforce Performance & Sentiment Analysis

This project simulates and analyzes a synthetic workforce to provide insights into employee performance, productivity, and engagement. By generating realistic employee, performance, and feedback data, it serves as a comprehensive example of how HR and management teams can track workforce efficiency and morale using data-driven approaches in Power BI.

---

## **Project Overview**

The main goal of this project is to create a realistic, synthetic dataset that mimics real-world workforce dynamics and provide tools to analyze performance and sentiment trends. The project integrates Python-based data generation, sentiment analysis, and Power BI-ready datasets to enable interactive dashboards for workforce analytics.

---

## **Dataset Components**

1. **Employee Master Data**  
   Contains information on 200 synthetic employees, including:
   - Employee ID and name  
   - Department and role  
   - Office location  
   - Tenure in years  
   This dataset provides the foundation for linking performance and feedback data.

2. **Performance Data**  
   Daily weekday performance data from January to September 2025, including:
   - Tasks completed  
   - Hours worked  
   - Efficiency scores (reflecting department-level variation and monthly trends)  
   This dataset enables productivity analysis, efficiency benchmarking, and trend tracking over time.

3. **Feedback Data**  
   Monthly employee feedback with positive, neutral, or negative sentiments:
   - Feedback text sampled from realistic statements  
   - Sentiment scoring using TextBlob  
   - Normalized sentiment scores (0–1) for easier analysis  
   - Sentiment labels (Positive, Neutral, Negative)  
   This dataset allows the study of workforce morale and engagement patterns.

4. **Sentiment Summary**  
   Aggregated counts of positive, neutral, and negative feedback, ready for dashboard KPIs and quick visualizations.

---

## **Data Loading and Power BI Model**

The three datasets (`Employee_Master.csv`, `Performance_Data.csv`, `Feedback_Data_Scored.csv`) are loaded into Power BI, and relationships are managed as follows:

- **Relationships**:  
  - `Employee_Master[EmployeeID]` → `Performance_Data[EmployeeID]`  
  - `Employee_Master[EmployeeID]` → `Feedback_Data_Scored[EmployeeID]`  
  This ensures all measures respect slicers for department, role, location, or employee-level filtering.

- **DAX Measures**:  
  ### Performance Metrics (Performance_Data)
  - **Total Tasks Completed**: `Total Tasks = SUM(Performance_Data[TasksCompleted])`  
  - **Total Hours Worked**: `Total Hours = SUM(Performance_Data[HoursWorked])`  
  - **Average Efficiency**: `Avg Efficiency = AVERAGE(Performance_Data[EfficiencyScore])`  
  - **Tasks per Hour**: `Tasks per Hour = DIVIDE([Total Tasks], [Total Hours], 0)`  

  ### Feedback & Sentiment (Feedback_Data_Scored)
  - **Avg Sentiment**: `Avg Sentiment = AVERAGE(Feedback_Data_Scored[Sentiment_Score_Normalized])`  
  - **Count Positive Feedback**: `Positive Feedback Count = CALCULATE(COUNTROWS(Feedback_Data_Scored), Feedback_Data_Scored[Sentiment_Label] = "Positive")`  
  - **Count Negative Feedback**: `Negative Feedback Count = CALCULATE(COUNTROWS(Feedback_Data_Scored), Feedback_Data_Scored[Sentiment_Label] = "Negative")`  
  - **Positive %**: `Positive % = DIVIDE([Count Positive Feedback], COUNTROWS(Feedback_Data_Scored), 0)`  
  - **Net Sentiment Score**: `Net Sentiment = [Positive %] - DIVIDE([Count Negative Feedback], COUNTROWS(Feedback_Data_Scored), 0)`  

These measures allow dynamic dashboards that **respond to slicers and filters**, making it easy to analyze performance and sentiment by department, role, or individual employee.

---

## **Analysis Capabilities**

Using the synthetic datasets and Power BI model, the project enables:

- **Workforce-Level KPIs:** Total tasks, hours, efficiency, average sentiment, and net sentiment.  
- **Department & Role Insights:** Comparative analysis of efficiency, productivity, and sentiment trends.  
- **Time Trends:** Monthly tracking of performance and morale, highlighting seasonal workload or engagement patterns.  
- **Employee-Level Insights:** Identification of high-performing employees and correlations between efficiency and sentiment.  
- **Visual Analytics:** KPI cards, trend charts, scatter plots, heatmaps, and role-specific comparisons.  

---

## **Key Insights Derived**

- IT and Operations are top-performing departments in both efficiency and productivity.  
- Average efficiency is moderate (0.55), with HR and Marketing showing lower scores.  
- Overall sentiment is positive (average 0.62) with net sentiment 0.41.  
- Sentiment remains stable over time, while efficiency shows minor seasonal variation, peaking mid-year.  
- Scatter plots of efficiency vs sentiment help identify employees and departments where engagement initiatives can boost performance.

---

## **Practical Applications**

- HR analytics and workforce planning simulations  
- Department and role-level performance monitoring  
- Employee sentiment analysis to inform engagement strategies  
- Creating interactive dashboards for management and decision-making  
- Training purposes for Power BI, DAX, and data visualization

---

## **Why This Project is Useful**

- **Realistic yet safe:** Synthetic data mimics real workforce patterns without using sensitive information.  
- **End-to-end workflow:** Includes data generation, cleaning, sentiment scoring, KPI calculation, and Power BI dashboarding.  
- **Actionable insights:** Highlights performance gaps and engagement opportunities for HR strategy.  
- **Power BI ready:** Clean, relational CSVs with consistent formatting and keys for easy integration.

---

This project demonstrates how organizations can combine **synthetic data, performance metrics, and sentiment analysis** to build a comprehensive workforce analytics system, providing actionable insights for managers, HR teams, and analysts.
