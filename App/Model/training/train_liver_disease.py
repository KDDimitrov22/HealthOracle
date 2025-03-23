import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pickle

df = pd.read_csv("../datasets/liver_disease_train.csv")
df.dropna(inplace=True)
df.drop(["TP", "Gender", "ALB"], axis=1, inplace=True)

X = df.drop("Selector", axis=1)
y = df["Selector"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)
model.fit(X_train_res, y_train_res)

y_pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))    

pickle_out = open("../models/model_liver.pkl","wb")
pickle.dump(model, pickle_out)
pickle_out.close()