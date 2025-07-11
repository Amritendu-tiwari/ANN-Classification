import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import  StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# load the trained model 
model = tf.keras.models.load_model('model.h5')


## load the encoder and scaler
with open ('onehot_enocder_geo.pkl','rb') as file:
    onehot_enocder_geo=pickle.load(file)
    
with open('label__encoder_gender.pkl','rb') as file:
    label__encoder_gender = pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)
    
    
## streamlit app
st.title('Customer Churn Predition')

## user input 
geography = st.selectbox('Geography',onehot_enocder_geo.categories_[0])
gender = st.selectbox('Gender',label__encoder_gender.classes_)
age = st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure  = st.slider('Number of tenure',1 ,4)
num_of_products = st.slider('Number of Products',1,4)
has_cr_card = st.selectbox('Has Credit card',[0,1])
is_active_member = st.selectbox('Is active Member',[0,1])

#prepare the input data
input_data = pd.DataFrame( {
    'CreditScore':[credit_score],
    'Gender':[label__encoder_gender.transform([gender])[0]],\
    'Age' : [age],
    'Tenure' : [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
} )

##one hot encoder " Geography"
geo_encoded = onehot_enocder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_enocder_geo.get_feature_names_out(['Geography']))

#combine one-hot encoded colums with input data
input_data = pd.concat([input_data.reset_index(drop=True),geo_encoded_df], axis=1)

#Scale the input data
input_data_scaled = scaler.transform(input_data)

## Prediction churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

st.write(f'Churn Probability: {prediction_proba: .2f}')

if prediction_proba > 0.5:
    print('the customer is likely to churn')
else:
    print('the customer is not likely to churn')