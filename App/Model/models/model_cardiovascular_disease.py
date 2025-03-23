import pickle
import pandas as pd

model = pickle.load(open('model_cardio.pkl', 'rb'))

def predictCardiovascular(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi):
    data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "ap_hi": [ap_hi],
    "ap_lo": [ap_lo],
    "cholesterol": [cholesterol],
    "gluc": [gluc],
    "smoke": [smoke],
    "alco": [alco],
    "active": [active],
    "bmi": [bmi]
    })

    prediction = model.predict(data)
    return(prediction[0])