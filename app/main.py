import streamlit as st


# Creating a local website for the generating 
def create_streamlit_app():
    st.title("Crop Prediction")
    nitrogen= st.text_input("Nitrogen:")
    phosphorus= st.text_input("Phosphorus:")
    potassium= st.text_input("Potassium:")
    temperature= st.text_input("Temperature:")
    humidity= st.text_input("Humidity:")
    ph= st.text_input("Ph:")
    rainfall= st.text_input("Rainfall:")
    label= st.text_input("Label:")
    
    predict_button= st.button("predict")
    
    




        
  
if __name__== "__main__":

    st.set_page_config(layout="wide", page_title= "Crop Prediction", page_icon= "*")
    create_streamlit_app()