import joblib
import numpy as np

model = joblib.load("models/equip_failure_rf.joblib")

sample = np.array([[75, 3.2, 80, 4.1, 150, 200, 1000, 150, 4000, 5000, 12]])
pred = model.predict(sample)
prob = model.predict_proba(sample)

print("Failure Prediction:", pred)
print("Failure Probability:", prob[:,1])
