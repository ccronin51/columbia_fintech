# Module 12 Report Template

## Overview of the Analysis

The purpose of this analysis is to build a model that will identify the creditworthiness of borrowers. 

The financial information is a dataset of historical lending activity from a peer-to-peer lending services company. 

In order to predict whether the status of a loan was healthy (value=0) or high-risk (value=1), the model looks at predictive features.

These features include:
* loan_size
* interest_rate
* borrower_income 
* debt_to_income
* num_of_accounts 
* derogatory_marks 
* total_debt

The loan status dependent variable is very imbalanced with 97% (75036) healthy loans and 3% (2500) high-risk loans

To predict loan status, this analysis separated the data into training and testing datasets, and then fit a logistic regression classification model on training datasets. After training, the logistic regression model was used to predict the testing dataset without the loan status dependent variable. These results were then compared to the actual loan status dependent variables in the testing dataset.
Next, this analysis was repeated but with resampling the dataset using random oversampling to balance the loan status dependent variable, now with more but equal rows of data: 50% (56,271) healthy loans and 50% (56,271) high-risk loans. 

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Model 1 - Logistic Regression Without Resampling:
  * Accuracy: .99
  * Healty Loans (0): Precision 1.00 and Recall 0.99
  * High Risk (1):    Precision 0.85 and Recall 0.91

* Model 2 - Logistic Regression With Resampling:
  * Accuracy: .99
  * Healty Loans (0): Precision 1.00 and Recall 0.99
  * High Risk (1):    Precision 0.84 and Recall 0.99
  

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:

* Model 1 - Logistic Regression Without Resampling:
This model predicts the healthy loan (0) very well with high precision (1.00) and recall (0.99). The model doesn't do as great a job at predicting the high-risk loan. It doesn't predict as well whether the high risk loan is actually a high risk loan with .85 precision (has some False Positives) and doesn't do asgood job at identifying when a loan isn't a high risk loan wtih .91 recall (has some False Negatives).

* Model 2 - Logistic Regression With Resampling:
This model predicts the healthy loan (0) very well with high precision (1.00) and recall (0.99). The model doesn't do as great a job at predicting whether the high risk loan is actually a high risk loan with .84 precision (has some False Positives) but does do a good job at identifying when a loan isn't a high risk loan with .99 recall (very few False Negatives).

* Explanation of FP & FN for High-Risk Loans:
FP - Predicted it was high risk when it wasn't high risk
FN - Predicted it was not high risk when it was high risk 

* Recommendation:
It is more important to predict '1's or High-Risk Loans than '0's or healthy loans. Model 2 performs the best because it has similar precision (just 1 lower) but higher recall compared to Model 1. Model 2 does a better job at identifying when a loan is not a high risk loan than Model 1; it has fewer False Negatives. With Model 1, more loans were predicted not to be high-risk loans when they actually were high-risk loans. This impacts the lender more because they couldn't address these loans by changing the terms or stopping their lending. This has less of a cost of predicting a loan is high risk when it is not (False Positive). It will take preventive steps and come to realize that this borrower is not causing issues. 

