import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("career_data.csv")

# -----------------------------
# LOWERCASE
# -----------------------------
df["skills"] = df["skills"].str.lower()
df["career"] = df["career"].str.strip()

# -----------------------------
# FEATURES & LABELS
# -----------------------------
X = df["skills"]
y = df["career"]

# -----------------------------
# BETTER TF-IDF
# -----------------------------
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english",
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

# -----------------------------
# MODEL
# -----------------------------
model = LogisticRegression(
    max_iter=2000
)

model.fit(X_vectorized, y)

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained successfully!")