import joblib
class Model:
    
    def __init__(self):
        self.model = joblib.load(open('model.joblib', 'rb'))
    
    def predict(self, values):
        sample_input_scaled = scaler.transform(sample_input)
        prediction = model.predict(sample_input_scaled)
        predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
        self.model.predict([[values]])[0]