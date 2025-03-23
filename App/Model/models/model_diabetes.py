import pickle
import pandas as pd

model = pickle.load(open('model_dia.pkl', 'rb'))

def predictDiabetes(BMI, HighBP, Age, HighChol, PhysHlth):
    data = pd.DataFrame({
    "BMI": [BMI],
    "HighBP": [HighBP],
    "Age": [Age],
    "HighChol": [HighChol],
    "PhysHlth": [PhysHlth]
    })

    prediction = model.predict(data)
    return(prediction[0])