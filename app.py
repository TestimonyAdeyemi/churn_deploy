import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import matplotlib.pyplot as plt
# import seaborn as sns
import joblib





#import xgboost as xgb





with open("model.pkl", "rb") as f:
    model = joblib.load(f)
   



# Title
st.title("Telco Custumer Churn Detection")



st.write(
    """
    ## About
    In today's highly competitive telecommunications industry, retaining customers is crucial for maximizing profits and sustaining growth. Customer churn, or the loss of customers to competitors, 
    can significantly impact a company's bottom line. To address this challenge, businesses need effective strategies for identifying and preventing churn.

    This Streamlit app leverages machine learning to predict whether customers of a Telco company are likely to churn. By analyzing various customer attributes and behaviors, the app provides insights 
    that enable the company to take proactive measures to retain at-risk customers and enhance overall customer satisfaction.

    ### How It Works
    1. **Input Customer Data**: Use the sidebar to input relevant customer information, including demographics, service usage, contract details, and payment methods.
    2. **Predict Churn**: Click the "Detect Result" button to run the machine learning model and predict whether the customer is likely to churn or not.
    3. **Receive Insights**: Based on the prediction, the app provides explanations for the outcome and actionable recommendations for retaining customers or improving satisfaction.
    4. **Take Action**: Utilize the insights provided by the app to implement targeted retention strategies and enhance the company's customer retention efforts.

    ### Why It Matters
    - **Cost Savings**: Acquiring new customers is more expensive than retaining existing ones. By accurately predicting churn and implementing retention strategies, companies can save on acquisition costs.
    - **Customer Satisfaction**: Identifying at-risk customers allows companies to address their concerns and improve service quality, leading to higher customer satisfaction and loyalty.
    - **Competitive Advantage**: Companies that effectively manage churn gain a competitive edge by retaining valuable customers and reducing market share loss to competitors.

    By utilizing this app, Telco companies can proactively address customer churn and strengthen customer relationships, ultimately driving long-term business success.

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
        st.success(f"The customer is predicted to churn.")
        st.text(f"Churn Probability: {proba_churn}%")
        st.write("Explanations:")
        st.write("- **High Monthly Charges:** Customers with higher monthly charges may perceive the service as costly, increasing the likelihood of churn.")
        st.write("- **Short Tenure:** Customers with shorter tenure may not have fully integrated into the service or experienced its long-term benefits, making them more susceptible to churn.")
        st.write("- **Lack of Essential Services:** Absence of crucial services like tech support and online security could indicate a lack of value-added features, leading to dissatisfaction and churn.")
        st.write("Recommendations:")
        st.write("### Specific Recommendations:")
        
        # High Monthly Charges
        if monthly_charges > 70:
            st.write("#### High Monthly Charges:")
            st.write("- Offer a personalized discount or loyalty program to reduce monthly charges and incentivize continued usage.")
        else:
            st.write("#### High Monthly Charges:")
            st.write("- Consider reviewing the pricing structure to ensure it remains competitive and aligns with customer expectations.")
        
        # Short Tenure
        if tenure_months <= 1:
            st.write("#### Short Tenure:")
            st.write("- Provide immediate onboarding assistance and personalized support to address any initial issues and establish a positive relationship from the start.")
        else:
            st.write("#### Short Tenure:")
            st.write("- Engage the customer with targeted promotions or loyalty incentives to encourage continued loyalty and enhance the overall experience.")
        
        # Lack of Essential Services
        if tech_support == 0:
            st.write("#### Lack of Tech Support:")
            st.write("- Upsell tech support services to provide customers with assistance and troubleshooting, enhancing their overall experience and reducing churn.")
        else:
            st.write("#### Presence of Tech Support:")
            st.write("- Continue providing excellent technical support services to enhance the customer experience and strengthen loyalty.")
        
        if online_security == 0:
            st.write("#### Lack of Online Security:")
            st.write("- Offer online security packages to protect customers' data and privacy, providing peace of mind and increasing loyalty.")
        else:
            st.write("#### Presence of Online Security:")
            st.write("- Highlight the importance of online security and privacy protection to customers, emphasizing the value-added benefits of the service.")

    elif predictions == 0:
        st.error(f"The customer is predicted to not churn.")
        st.text(f"No Churn Probability: {proba_nochurn}%")
        st.write("Explanations:")
        st.write("- **Stable Tenure:** Customers with longer tenure are likely more satisfied with the service and have developed loyalty over time.")
        st.write("- **Reasonable Monthly Charges:** Competitive pricing and fair monthly charges indicate good value for money, reducing the likelihood of churn.")
        st.write("- **Presence of Value-Added Services:** Services like tech support and online security enhance the overall customer experience, fostering loyalty.")
        st.write("Recommendations:")
        st.write("### Specific Recommendations:")
        
        # Stable Tenure
        if tenure_months >= 12:
            st.write("#### Stable Tenure:")
            st.write("- Offer exclusive rewards or benefits to recognize and appreciate the customer's long-term commitment.")
        else:
            st.write("#### Stable Tenure:")
            st.write("- Continue providing excellent service and personalized support to nurture the customer relationship during the early stages.")
        
        # Reasonable Monthly Charges
        if monthly_charges <= 50:
            st.write("#### Reasonable Monthly Charges:")
            st.write("- Maintain competitive pricing and periodically review pricing strategies to ensure they remain attractive to customers.")
        else:
            st.write("#### Reasonable Monthly Charges:")
            st.write("- Offer value-added services or perks to justify the slightly higher pricing and enhance the overall customer experience.")
        
        # Presence of Value-Added Services
        if tech_support == 1:
            st.write("#### Presence of Tech Support:")
            st.write("- Continue providing excellent technical support services to enhance the customer experience and strengthen loyalty.")
        else:
            st.write("#### Lack of Tech Support:")
            st.write("- Upsell tech support services to provide customers with assistance and troubleshooting, enhancing their overall experience and reducing churn.")
        
        if online_security == 1:
            st.write("*Presence of Online Security:*")
            st.write("- Highlight the importance of online security and privacy protection to customers, emphasizing the value-added benefits of the service.")
        else:
            st.write("*Lack of Online Security:*")
            st.write("- Offer online security packages to protect customers' data and privacy, providing peace of mind and increasing loyalty.")



    

    # if predictions == 1:
    #     st.error(f"The customer is predicted to not churn.")
    #     st.text(f"No Churn Probability: {proba_nochurn}%")
    #     st.write("Explanations:")
    #     st.write("- **High Monthly Charges:** Customers with higher monthly charges may perceive the service as costly, increasing the likelihood of churn.")
    #     st.write("- **Short Tenure:** Customers with shorter tenure may not have fully integrated into the service or experienced its long-term benefits, making them more susceptible to churn.")
    #     st.write("- **Lack of Essential Services:** Absence of crucial services like tech support and online security could indicate a lack of value-added features, leading to dissatisfaction and churn.")
    #     st.write("Recommendations:")
    #     st.write("- **Retention Offers:** Offer tailored discounts or incentives to encourage customers to stay, such as loyalty discounts or free service upgrades.")
    #     st.write("- **Proactive Outreach:** Reach out to churn-prone customers to understand their concerns and offer solutions before they decide to leave.")
    #     st.write("- **Enhanced Customer Support:** Invest in improving customer service and support channels to address issues promptly and enhance customer satisfaction.")

    # elif predictions == 0:
    #     st.success(f"The customer is predicted to churn.")
    #     st.text(f"Churn Probability: {proba_churn}%")
    #     st.write("Explanations:")
    #     st.write("- **Stable Tenure:** Customers with longer tenure are likely more satisfied with the service and have developed loyalty over time.")
    #     st.write("- **Reasonable Monthly Charges:** Competitive pricing and fair monthly charges indicate good value for money, reducing the likelihood of churn.")
    #     st.write("- **Presence of Value-Added Services:** Services like tech support and online security enhance the overall customer experience, fostering loyalty.")
    #     st.write("Recommendations:")
    #     st.write("- **Customer Loyalty Programs:** Reward loyal customers with exclusive perks, discounts, or early access to new features.")
    #     st.write("- **Upselling Opportunities:** Identify opportunities to upsell or cross-sell additional services based on the customer's usage patterns and preferences.")
    #     st.write("- **Personalized Engagement:** Engage customers with personalized communications and offers to strengthen the relationship and encourage long-term loyalty.")

        



    

    



