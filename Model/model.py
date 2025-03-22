from sklearn.linear_model import LogisticRegression
import pickle

model = pickle.load(open('model.pkl', 'rb'))

def predictCardiovascular(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi):
    prediction = model.predict([[age,gender,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,bmi]])
    print(prediction)

predictCardiovascular(16, 2, 120, 81, 1, 1, 0, 0, 0, 23.4)