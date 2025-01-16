# Crop Prediction

This project aims to predict the best crops to plant based on various environmental factors such as soil type, weather conditions, and historical crop yield data.


## Introduction
Crop prediction is essential for optimizing agricultural productivity. This project uses machine learning algorithms to analyze environmental data and provide recommendations for the most suitable crops to the farmer.

## Features
- Data preprocessing and cleaning
- Machine learning model training and evaluation
- Crop recommendation based on input parameters
- Visualization of prediction results

## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Steps Involved in the project
1. Developed a Streamlit application to present the results and predictions of a machine learning model in an interactive and user-friendly interface. 
2. The machine learning model, implemented in the main.ipynb file, is a neural network designed with ReLU activation functions in the input and hidden layers to introduce non-linearity and enhance learning capabilities.
3. The neural network model was trained and fine-tuned to achieve optimal performance, with the parameters and architecture designed to handle the complexity of the dataset effectively. Once the model was finalized, it was serialized and stored in .joblib format.
4. The Streamlit application was then integrated with the saved model to enable seamless predictions. Users can input data through the application interface, and the neural network processes the input to generate predictions in real-time.
5.  The application also includes features for visualizing the predictions, model performance metrics, and insights, making it an end-to-end solution for showcasing the model's capabilities and results.