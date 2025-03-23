import os
import pickle
from sklearn.linear_model import LogisticRegression

model_path = os.path.join(os.path.dirname(__file__), "model_cardio.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

def predictCardiovascular(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi):
    prediction = model.predict([[age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi]])
    return int(prediction[0])