# ================================================
# Employee Feedback Sentiment Analysis (TextBlob)
# ================================================

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# -----------------------------------------------
# 1️⃣ Load feedback dataset
# -----------------------------------------------
df = pd.read_csv("Feedback_Data.csv")
print(f"Loaded {len(df)} feedback records")

# Clean whitespace & lowercase
df["FeedbackText"] = df["FeedbackText"].astype(str).str.strip()

# -----------------------------------------------
# 2️⃣ Sentiment Scoring
# -----------------------------------------------
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # range [-1, 1]

df["Sentiment_Score"] = df["FeedbackText"].apply(get_sentiment)

# Normalize to 0–1 for easier comparison with efficiency
df["Sentiment_Score_Normalized"] = ((df["Sentiment_Score"] + 1) / 2).round(3)

# Label sentiment for visuals
def label_sentiment(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment_Label"] = df["Sentiment_Score"].apply(label_sentiment)

# -----------------------------------------------
# 3️⃣ Save scored dataset
# -----------------------------------------------
output_path = "Feedback_Data_Scored.csv"
df.to_csv(output_path, index=False)
print(f"✅ Sentiment-scored dataset saved as: {output_path}")

# -----------------------------------------------
# 4️⃣ Summary stats & quick visualization
# -----------------------------------------------
sentiment_counts = df["Sentiment_Label"].value_counts()
print("\nSentiment Distribution:")
print(sentiment_counts)

plt.figure(figsize=(6,4))
sentiment_counts.plot(kind="bar", color=["green", "gray", "red"])
plt.title("Employee Feedback Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count of Feedbacks")
plt.tight_layout()
plt.show()

# -----------------------------------------------
# 5️⃣ Export summary
# -----------------------------------------------
summary = (
    df.groupby("Sentiment_Label")
    .size()
    .reset_index(name="Count")
    .sort_values(by="Count", ascending=False)
)
summary.to_csv("Sentiment_Summary.csv", index=False)
print("📊 Summary exported to Sentiment_Summary.csv")

print("🎯 Sentiment analysis complete. Ready for Power BI!")
