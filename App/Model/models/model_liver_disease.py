import pickle
import pandas as pd

model = pickle.load(open('model_liver.pkl', 'rb'))

def predictDiabetes(Age, TB, DB, Alkphos, Sgpt, Sgot, AGRat):
    data = pd.DataFrame({
    "Age": [Age],
    "TB": [TB],
    "DB": [DB],
    "Alkphos": [Alkphos],
    "Sgpt": [Sgpt],
    "Sgot": [Sgot],
    "A/G Ratio": [AGRat]
    })

    prediction = model.predict(data)
    return(prediction[0])