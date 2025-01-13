import streamlit as st
from model import Model


# Creating a local website for the generating 
def create_streamlit_app(model):
    st.title("Crop Prediction")
    nitrogen= st.number_input("Nitrogen:")
    phosphorus= st.number_input("Phosphorus:")
    potassium= st.number_input("Potassium:")
    temperature= st.number_input("Temperature:")
    humidity= st.number_input("Humidity:")
    ph= st.number_input("Ph:")
    rainfall= st.number_input("Rainfall:")
    
    predict_button= st.button("predict")
    
    if predict_button:
        try:
           if ph >0 and ph <=14 and temperature<100 and humidity<100 and rainfall<100:
                values= [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
                crop_recommendation= model.predict(values)
                st.code(crop_recommendation, language= 'markdown')
        
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
    
    




        
  
if __name__== "__main__":
    model = Model()
    st.set_page_config(layout="wide", page_title= "Crop Prediction", page_icon= "*")
    create_streamlit_app(model)