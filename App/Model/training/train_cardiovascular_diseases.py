import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("../datasets/cardio_train.csv", sep=";")

data.drop("id",axis=1,inplace=True)
data.drop_duplicates(inplace=True)

data["bmi"] = round(data["weight"] / (data["height"]/100)**2)
data.drop("weight", axis=1,inplace=True)
data.drop("height", axis=1,inplace=True)

data["age"] = round(data["age"]/365.25)

#filtering out extremes
out_filter = ((data["ap_hi"]>250) | (data["ap_lo"]>200))
data = data[~out_filter]
out_filter2 = ((data["ap_hi"] < 0) | (data["ap_lo"] < 0))
data = data[~out_filter2]


target_name = 'cardio'
data_target = data[target_name]
data = data.drop([target_name], axis=1)

train, test, target, target_test = train_test_split(data, data_target, test_size=0.2, random_state=0)
logreg = LogisticRegression(max_iter=10000)
logreg.fit(train, target)


acc_log = round(logreg.score(train, target) * 100, 2)
print(acc_log)
acc_test_log = round(logreg.score(test, target_test) * 100, 2)
print(acc_test_log)

pickle_out = open("../models/model_cardio.pkl","wb")
pickle.dump(logreg, pickle_out)
pickle_out.close()