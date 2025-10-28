# ============================================
# Synthetic Workforce Performance & Feedback Data Generator
# ============================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
np.random.seed(42)
random.seed(42)

# ---------- CONFIG ----------
num_employees = 200
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 9, 30)

departments = ["HR", "Finance", "IT", "Marketing", "Sales", "Operations"]
roles = {
    "HR": ["HR Manager", "Recruiter", "HR Analyst"],
    "Finance": ["Accountant", "Financial Analyst", "Auditor"],
    "IT": ["Developer", "Data Analyst", "System Engineer"],
    "Marketing": ["Marketing Analyst", "SEO Specialist", "Brand Manager"],
    "Sales": ["Sales Executive", "Account Manager", "Sales Analyst"],
    "Operations": ["Operations Manager", "Logistics Coordinator", "Planner"],
}
locations = ["New York", "London", "Toronto", "Berlin", "Sydney"]

# Base efficiency ranges by department (adds variation)
dept_eff = {
    "HR": (0.25, 0.55),
    "Finance": (0.35, 0.65),
    "IT": (0.45, 0.80),
    "Marketing": (0.30, 0.60),
    "Sales": (0.40, 0.70),
    "Operations": (0.40, 0.75),
}

# Feedback text options
feedback_positive = [
    "I feel motivated by the team and our goals.",
    "The workload is manageable and leadership is supportive.",
    "Great collaboration across departments.",
    "I enjoy coming to work every day.",
    "The manager gives constructive feedback regularly.",
]
feedback_negative = [
    "Deadlines are unrealistic and stressful.",
    "There is a lack of communication from management.",
    "Workload feels overwhelming lately.",
    "Limited opportunities for career growth.",
    "The expectations are unclear for my role.",
]
feedback_neutral = [
    "The work environment is fine, nothing special.",
    "I feel neither satisfied nor dissatisfied.",
    "My tasks are repetitive but manageable.",
    "Work processes are okay but could be improved.",
]

# ---------- EMPLOYEE MASTER ----------
employees = []
for i in range(num_employees):
    dept = random.choice(departments)
    role = random.choice(roles[dept])
    employees.append({
        "EmployeeID": f"E{i+1:03d}",
        "Name": fake.name(),
        "Department": dept,
        "Role": role,
        "Location": random.choice(locations),
        "Tenure_Years": round(random.uniform(0.5, 12), 1)
    })

df_employees = pd.DataFrame(employees)
df_employees.to_csv("Employee_Master.csv", index=False)

# ---------- PERFORMANCE DATA ----------
date_range = pd.date_range(start_date, end_date, freq="D")
performance_records = []

for _, emp in df_employees.iterrows():
    base_min, base_max = dept_eff[emp["Department"]]
    for day in date_range:
        if day.weekday() < 5:  # Monday–Friday only
            # Add monthly drift for realism
            month_factor = 1 + np.sin(day.timetuple().tm_yday / 90) * 0.1
            base_eff = np.random.uniform(base_min, base_max) * month_factor
            eff = np.clip(base_eff + np.random.normal(0, 0.05), 0.2, 0.9)
            hours = np.random.uniform(7, 9)
            tasks = int(hours * np.random.uniform(2.5, 4.0) * eff)
            performance_records.append({
                "EmployeeID": emp["EmployeeID"],
                "Date": day.strftime("%Y-%m-%d"),
                "TasksCompleted": tasks,
                "HoursWorked": round(hours, 2),
                "EfficiencyScore": round(eff, 3)
            })

df_perf = pd.DataFrame(performance_records)
df_perf.to_csv("Performance_Data.csv", index=False)

# ---------- FEEDBACK DATA ----------
feedback_records = []
for _, emp in df_employees.iterrows():
    for month in pd.date_range(start_date, end_date, freq="M"):
        fb_type = random.choices(
            ["positive", "neutral", "negative"], weights=[0.5, 0.3, 0.2]
        )[0]
        fb_text = random.choice({
            "positive": feedback_positive,
            "neutral": feedback_neutral,
            "negative": feedback_negative,
        }[fb_type])
        feedback_records.append({
            "EmployeeID": emp["EmployeeID"],
            "Date": month.strftime("%Y-%m-%d"),
            "FeedbackText": fb_text
        })

df_feedback = pd.DataFrame(feedback_records)
df_feedback.to_csv("Feedback_Data.csv", index=False)

print("✅ Synthetic datasets generated successfully!")
print("Files created:")
print(" - Employee_Master.csv")
print(" - Performance_Data.csv")
print(" - Feedback_Data.csv")
