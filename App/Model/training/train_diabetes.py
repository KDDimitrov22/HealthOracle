import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

df = pd.read_csv("../datasets/diabetes_train.csv")
df = df.dropna()
df["diabetes_binary"] = df['Diabetes_012'].apply(lambda x: 1 if x in [1.0, 2.0] else 0)
top_features = ["diabetes_binary", "BMI", "HighBP", "Age", "HighChol", "PhysHlth"]
X = df[top_features].drop("diabetes_binary", axis=1)
y = df["diabetes_binary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

model = RandomForestClassifier(
    n_estimators=100,         # number of trees
    max_depth=10,             # reasonable max depth
    class_weight='balanced',  # put more focus on the minority class
    random_state=42
)

model.fit(X_train_res, y_train_res)

y_pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

pickle_out = open("../models/model_dia.pkl","wb")
pickle.dump(model, pickle_out)
pickle_out.close()