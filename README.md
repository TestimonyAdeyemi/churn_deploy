# DermDetect-AI
[Video Explanation Link](https://drive.google.com/file/d/1as6MMSMYEVFnZnWdBXr5mtlMo0kCDZkb/view?usp=sharing)

[Deployed Project](https://churndeploy-4meaar682vipmw8fysqvds.streamlit.app/)

Table of Contents
- [Introduction and Background](#introduction-and-background)
- [The Problem](#the-problem)
- [Motivation and Significance](#motivation-and-significance)
- [The Solution](#the-solution)
- [The Datasets Used](#the-datasets-used)
- [Model Architecture and Optimization](#model-architecture-and-optimization)

## Project Overview

### Introduction and Background
Telecom churn, the turnover of customers switching from one service provider to another, poses significant challenges and financial implications for telecom companies worldwide. Predicting churn allows companies to identify at-risk customers and implement retention strategies proactively.

### The Problem
<hr>
The telecom industry faces intense competition, with customer retention being a pivotal aspect of maintaining market share and revenue(Liao et al., 2011). Traditional methods for identifying potential churners are often reactive and inefficient, relying on customer complaints or direct feedback, which might be too late to prevent the customer's departure (M'Baye et al., 2020).

### Motivation and Significance
<hr>
The motivation for this project stems from the need for a proactive approach to identify potential churners, allowing telecom companies to engage with these customers through personalized retention strategies before they decide to leave. This project's significance lies in leveraging advanced machine learning techniques to predict customer churn, which can significantly impact customer satisfaction, loyalty, and company revenue (Park, 2001).

### The Solution
<hr>
Our solution involves developing a predictive model using machine learning techniques such as XGBoost, LightGBM, and KNN. The models are trained on historical customer data to identify patterns and predict the likelihood of churn. By implementing an ensemble method and optimizing the models through hyperparameter tuning with [Optuna](https://github.com/optuna/optuna-examples) (Akiba et al., 2019), we aim to achieve high accuracy and generalizability in predicting churn.

## The Datasets Used
This project utilized a comprehensive telecom churn dataset available on [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn), which includes a wide range of features related to customer demographics, account information, and usage statistics. The dataset provides a realistic representation of a telecom company's customer base, making it suitable for developing a churn prediction model.

## Model Architecture and Optimization

-  ### Model Selection
The project initially explored various models, including Logistic Regression, KNN, XGBoost, and LightGBM, to evaluate their performance in predicting customer churn. Based on initial validation set results, the focus shifted towards optimizing XGBoost, LightGBM, and KNN due to their superior performance.

-  ### Handling Class Imbalance
Given the imbalanced nature of churn datasets, where the number of churners is typically much lower than non-churners, we considered applying SMOTE to balance the classes, enhancing the model's ability to predict the minority class accurately.

-  ### Hyperparameter Tuning
We employed [Optuna](https://github.com/optuna/optuna-examples) , a hyperparameter optimization framework, to fine-tune the models. [Optuna](https://github.com/optuna/optuna-examples)'s efficient search capabilities allowed us to explore a wide range of parameter configurations to find the optimal settings for each model, focusing on maximizing the AUC score as it provides a robust measure for evaluating binary classification models, especially in the presence of class imbalance.

-  ### Future Directions: Ensemble Methods
As part of the ongoing optimization, we are exploring ensemble methods to combine the strengths of individual models. By leveraging the diverse predictions from XGBoost, LightGBM, and potentially KNN, we aim to develop a more robust and accurate ensemble model that improves overall prediction performance.

## Citations
- Liao, Y., Li, S., & Wang, J. (2011). A survey of churn prediction in telecommunication service providers. Expert Systems with Applications, 38(1), 863-874.
- M'Baye, M., Hussain, F. K., & Boulet, M. (2020). A survey on churn prediction in telecommunication networks: Recent trends and future challenges. Journal of King Saud University - Computer and Sciences, 32(6), 1201-1225.
- Park, M. S., & Kim, J. H. (2001). An artificial neural network model for customer An artificial neural network model for customer churn prediction in telecommunications. Expert Systems with Applications, 20(3), 271-280.
- Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A Next-generation Hyperparameter Optimization Framework. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.

