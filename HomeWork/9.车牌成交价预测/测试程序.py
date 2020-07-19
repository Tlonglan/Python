# Required Packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model

# Function to get data.csv
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    Z_parameter = []
    for time, p_low_price in zip(data['time'], data['p_low_price']):
        X_parameter.append([float(time)])
        Y_parameter.append(float( p_low_price ))
    return X_parameter, Y_parameter

# Function for Fitting our data.csv to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

X, Y = get_data('car_price.csv')
predictvalue_69 = 69
predictvalue = 70
result_69 = linear_model_main(X, Y, predictvalue_69)
result = linear_model_main(X, Y, predictvalue)
# print("Intercept value ", result['intercept'])
# print("coefficient", result['coefficient'])
print('reference:',result_69['predicted_value'],'\n',"Predicted value: ", result['predicted_value'])

# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # LinearRegression()
    plt.figure(figsize=(10, 5))

    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='green' )
    plt.plot(X_parameters, Y_parameters, color='red', linewidth=1, label=u'个人最低价')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)

    # regr.fit(X_parameters, Z_parameters)
    # plt.scatter(X_parameters, Z_parameters, color='blue' )
    # plt.plot(X_parameters, Z_parameters, color='green', linewidth=1, label=u'个人平均价')
    # plt.plot(X_parameters, regr.predict(X_parameters), color='green', linewidth=4)

    plt.xlabel(u'时间')
    plt.ylabel(u'价格')
    plt.legend()
    # plt.xticks(())
    # plt.yticks(())
    plt.show()

# show_linear_line(X,Y)
show_linear_line(X,Y)