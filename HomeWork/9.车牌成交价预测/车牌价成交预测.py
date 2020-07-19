# Required Packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model

# Function to get data.csv
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for time, p_low_price in zip(data['time'], data['p_ave_price']):
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

# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    plt.figure(figsize=(10, 5))

    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='green' )
    plt.plot(X_parameters, Y_parameters, color='red', linewidth=1, label=u'个人平均价')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)

    plt.xlabel(u'时间')
    plt.ylabel(u'价格')
    plt.legend()

    plt.show()

X, Y = get_data('car_price_s.csv')
# 参考最近一次拟合的数据与实际数据的差值，给出该次拟合的误差
predictvalue_69 = 69
result_69 = linear_model_main(X, Y, predictvalue_69)
predictvalue = 70
result = linear_model_main(X, Y, predictvalue)
print('reference_69:',result_69['predicted_value'],'\n',"Predicted value: ", result['predicted_value'])

# show_linear_line(X,Y)
show_linear_line(X,Y)