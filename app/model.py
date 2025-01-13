import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
class Model:
    
    def __init__(self):
        self.model = joblib.load(open('model.joblib', 'rb'))
    
    def predict(self, values):
        sample_input = np.array([values])
        scaler = joblib.load(open('scaler.joblib', 'rb'))
        encoder = joblib.load(open('label_encoder.joblib', 'rb'))
        sample_input_scaled = scaler.transform(sample_input)
        prediction = self.model.predict(sample_input_scaled)
        predicted_label = encoder.inverse_transform([np.argmax(prediction)])
        return predicted_label[0]
        
        
        
        
        