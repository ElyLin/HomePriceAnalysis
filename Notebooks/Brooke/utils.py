import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as stats
import numpy as np


def model1(ind_variable, data):
    
    ''' 
    Create a multiple linear regression model using a list of independent 
    variables and a dataframe
    ind_variable: a list of strings which correspond to the column names of the
    dataframe which are to be used as independent variables
    data = a dataframe which includes all of the relevant independent variables
    and the dependent variable   
    '''
    formula = 'price ~ ' + ' + '.join(ind_variable)
    multi_model = ols(formula, data).fit()
    multi_model_summ = multi_model.summary()
    return multi_model,multi_model_summ

# subfunction that does the assessment of the model
def assess1(model):
    
    '''
    This function takes in a model which was which was created by using statsmodels
    ols to fit, and and returns Mean Absolte Error and Root Mean Squared Error, as well
    as a residual plot.
    important: X training data (independent variables training data) in your 
    notebook/platform must be called "X_train" and X testing data 
    (independent variables training data) must be called "X_test". 
    Also, y training data must be called "y_train" (dependent variable) and y testing data must be called
    "y_test" (dependent variable). 
    '''
    tr_preds=model.predict(X_train)
    te_preds=model.predict(X_test)
    y_tr = y_train
    y_te = y_test
    print(f"Train R2: {r2_score(y_tr, tr_preds)}")
    print(f"Test R2: {r2_score(y_te, te_preds)}")
    print('----')
    print(f"Train RMSE: {mean_squared_error(y_tr, tr_preds, squared = False)}")
    print(f"Test RMSE: {mean_squared_error(y_te, te_preds, squared = False)}")
    print('----')
    print(f"Train MAE: {mean_absolute_error(y_tr, tr_preds)}")
    print(f"Test MAE: {mean_absolute_error(y_te, te_preds)}")

    tr_res= y_tr - tr_preds
    te_res= y_te - te_preds
    
    plt.scatter(tr_preds, tr_res, label = 'Train')
    plt.scatter(te_preds, te_res, label = 'Test')
    
    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show

# subfunction that scales the model
def scaled_model1(ind_variable, data):
    ''' 
    Create a scaled multiple linear regression model using a list of independent 
    variables and a dataframe
    ind_variable: a list of strings which correspond to the column names of the
    dataframe which are to be used as independent variables
    data = a dataframe which includes all of the relevant independent variables
    and the dependent variable.   
    '''
    formula = 'price ~ ' + ' + '.join(ind_variable)
    data_scaled = (data - np.mean(data)) / np.std(data)
    model_scaled = ols(formula, data_scaled).fit()
    model_scaled_summ = model_scaled.summary()
    return model_scaled_summ

# the main function
def model_and_assess1(ind_variable,data):
   '''
   Function which uses two other functions in order to create a multiple linear 
   regression, print the Root Mean Squared Error, Mean Absolute Error, R2, residual plot,
   and qqplot, as well as print out a statistical summary for both scaled and unscaled
   data which includes info about R2, p-values, multicollinearity, and coefficients.
    ind_variable: a list of strings which correspond to the column names of the
    dataframe which are to be used as independent variables
    data = a dataframe which includes all of the relevant independent variables
    and the dependent variable.  
    '''
    multi_model = model(ind_variable,data)[0]
    multi_model_summ = model(ind_variable,data)[1]
    assessment = assess(multi_model)
    scaled_summ = scaled_model(ind_variable,data)
    qq = sm.graphics.qqplot(multi_model.resid, dist=stats.norm, line='45', fit=True)
    print('        ')
    print('This is the summary of the model')
    print('        ')
    print(multi_model_summ)   
    print('        ')
    print('This is the summary of the scaled model')
    print('        ')
    print(scaled_summ)        
    print('        ')
    print('This is the correlation table between variables')
    print('        ')
    print(data[ind_variable].corr())    
    print('        ')
    print('This is the residual plot and qq plot')
    print('        ')
    print(assessment)
    print(qq)

