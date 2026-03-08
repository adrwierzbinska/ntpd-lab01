import joblib
import numpy as np

loaded_model = joblib.load('model_v1.joblib')
sample_data = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = loaded_model.predict(sample_data)
print(f"Predykcja dla próbki {sample_data}: {prediction[0]}")