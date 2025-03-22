from sklearn.linear_model import LogisticRegression
import pickle

model = pickle.load(open('Model/model.pkl', 'rb'))

def predictCardiovascular(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi):
    prediction = model.predict([[age,gender,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,bmi]])
    return(prediction)