import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import joblib





#import xgboost as xgb





with open("model.pkl", "rb") as f:
    model = joblib.load(f)
   



# Title
st.title("Telco Custumer Churn Detection")

# Image
#st.image("img/churn-image.jpeg")
# About
st.write(
    """
    ## About
    The globalization and advancements of telecommunication industry, exponentially raises the number of operators in the market that escalates the competition. 
    In this competitive era, it has become mandatory to maximize the proﬁts periodically, for that various strategies have been proposed, namely, acquiring newcustomers, 
    up-selling the existing customers & increasing the retention period of existing customers. Among all the strategies, retention of existing customers is least expensive as compared to others. 
    In order to adopt the third strategy, companies have to reduce the potential customer churn. In this sense, the main reason of churn is the dissatisfaction of consumer service and support system. 
    The key to unlock solutions to this problem is by forecasting the customers which are at risk of churning.

    **This Streamlit App  utilizes our trained Machine Learning model in order to detect whether the customers from a Telco company will churns or not the company.**

    
    """
)

######################################## Funtions ###########################################################
# Binary variables
def create_binary(content):
    if content == "Male":
        content = 1
    elif content == "Female":
        content = 0
    elif content == "Yes":
        content = 1
    elif content == "Not":
        content = 0
    return content
# Covert Multiple Lines, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV and Streaming Movies
def convert_muliples_var(content):
    if content == "No phone service":
        content = 1
    elif content == "Not":
        content = 0
    elif content == "Yes":
        content = 2
    return content

def convert_internet_ser(content):
    if content == "Fiber optic":
        content = 1
    elif content == "DSL":
        content = 0
    elif content == "No":
        content = 2
    return content

def convert_contract(content):
    if content == "One year":
        content = 1
    elif content == "Month-to-month":
        content = 0
    elif content == "Two year":
        content = 2
    return content

def convert_payment_method(content):
    if content == "Credit card (automatic)":
        content = 1
    elif content == "Bank transfer (automatic)":
        content = 0
    elif content == "Electronic check":
        content = 2
    elif content == "Mailed check":
        content = 3
    return content


########################################################### Inputs ######################################################################
st.sidebar.title("Customer's Data")

# Categorical and binary variables
var_gender = ("Male", "Female")
var_bool = ("Yes", "Not")
var_multiple = ("Yes", "Not", "No phone service")
var_internet = ("DSL", "Fiber optic", "No")
var_contract = ("Month-to-month", "One year", "Two year")
var_payment_m = ("Credit card (automatic)", "Bank transfer (automatic)", "Electronic check", "Mailed check")

gender = st.sidebar.selectbox("Customer's Gender", var_gender)
partner = st.sidebar.selectbox("Partner", var_bool)
dependents = st.sidebar.selectbox("Does the customer live with any dependents(children, parents, etc.)?", var_bool)
mutiple_lines = st.sidebar.selectbox("Does the customer have multiple telephone line services?", var_multiple)
internet_services = st.sidebar.selectbox("Does the customer have multiple Internet line services?", var_internet)
online_security = st.sidebar.selectbox("Does the customer have online security service?", var_multiple)
online_backup = st.sidebar.selectbox("Does the customer have online backup service?", var_multiple)
device_protection = st.sidebar.selectbox("Does the customer have device protection service?", var_multiple)
tech_support = st.sidebar.selectbox("Does the customer have tech support service?", var_multiple)
streaming_tv = st.sidebar.selectbox("Does the customer have streaming tv service?", var_multiple)
streaming_movies = st.sidebar.selectbox("Does the customer have streaming movies service?", var_multiple)
contract = st.sidebar.selectbox("Which customer's current contract type?", var_contract)
paperless_billing = st.sidebar.selectbox("Paperless billing", var_bool)
payment_method = st.sidebar.selectbox("Payment method", var_payment_m)

# Numerical variables
tenure_months = st.sidebar.number_input("Tenure Months", min_value = 0, max_value = 80)
monthly_charges = st.sidebar.number_input("Monthly Charges")
cltv = st.sidebar.number_input("Customer Lifetime Value(CLTV)")

######################################################### Inference #########################################################

prediction = st.button("Detect Result")

if prediction:

    data = {
        "Gender" : create_binary(gender),
        "Partner" : create_binary(partner),
        "Dependents" : create_binary(dependents),
        "Tenure Months" : tenure_months,
        "Multiple Lines" : convert_muliples_var(mutiple_lines),
        "Internet Service" : convert_internet_ser(internet_services),
        "Online Security" : convert_muliples_var(online_security),
        "Online Backup" : convert_muliples_var(online_backup),
        "Device Protection" : convert_muliples_var(device_protection),
        "Tech Support": convert_muliples_var(tech_support),
        "Streaming TV": convert_muliples_var(streaming_tv),
        "Streaming Movies" : convert_muliples_var(streaming_movies),
        "Contract" : convert_contract(contract),
        "Paperless Billing" : create_binary(paperless_billing),
        "Payment Method": convert_payment_method(payment_method),
        "Monthly Charges" : monthly_charges,
        "CLTV": cltv
    }




    
    #from pydantic import BaseModel


    ## Schema validation
    # class Features(BaseModel):
    #     Gender: int
    #     Parther: int
    #     Dependents: int
    #     Tenure_Months: int
    #     Mutiple_lines: int
    #     Internet_services: int
    #     Online_Security: int
    #     Online_Backup: int
    #     Device_Protection: int
    #     Tech_support: int
    #     Streaming_tv: int
    #     Streaming_movies: int
    #     Contract: int
    #     Paperless_billing: int
    #     Payment_method: int
    #     Monthly_charges: float
    #     cltv: float





    # Features
    #features = data.dict()
    # Dataframe from features
    data_f = pd.DataFrame(data, index = [0])
    print(data_f)
    # predictions
    predictions = model.predict(data_f)

    proba = model.predict_proba(data_f)
    proba_nochurn = np.round((proba[0][0])*100, 2)
    proba_churn = np.round((proba[0][1])*100, 2)

    if predictions == 1:
        st.success(f"The customer is predicted to churn")
        st.text(proba_churn)
        
    elif predictions == 0:
        st.error(f"The customer is predicted to not churn")
        st.text(proba_nochurn)

     



    

    



