# Initial Linear Regression and initial KNN to find relationship between mutation impact and biomass

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler


df_data = pd.read_csv("gene_mut_biomass_for_ml.txt", sep = "\t")

y = df_data["biomass"]
X = df_data.drop(columns="biomass")

scaler = MinMaxScaler(feature_range=(0, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=42)

# X_train_scaled = scaler.fit_transform(X_train)
# X_train = pd.DataFrame(X_train_scaled)
#
# X_test_scaled = scaler.fit_transform(X_test)
# X_test = pd.DataFrame(X_test_scaled)

model_linreg = LinearRegression()
model_linreg.fit(X_train, y_train)

y_pred = model_linreg.predict(X_test)

r2 = model_linreg.score(X_test, y_test)
print(r2)
print(r2_score(y_test, y_pred))




# Calculate regression line equation
coeff = np.polyfit(y_test.squeeze(), y_pred.squeeze(), 1)
line_eq = np.poly1d(coeff)

# Create a scatter plot of actual vs. predicted values
plt.scatter(y_test, y_pred, c='blue', alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values')

# Add a regression line
plt.plot(y_test, line_eq(y_test), color='red', linestyle='-')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score

df_data = pd.read_csv("gene_mut_biomass_for_ml.txt", sep="\t")

y = df_data["biomass"]
X = df_data.drop(columns="biomass")

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

#scaler = MinMaxScaler(feature_range=(0, 1))

#X_train_scaled = scaler.fit_transform(X_train)
#X_train = pd.DataFrame(X_train_scaled)

#X_test_scaled = scaler.fit_transform(X_test)
#X_test = pd.DataFrame(X_test_scaled)

# rmse_val = []
# for K in range(40):
#     K = K + 1
#     model = KNeighborsRegressor(n_neighbors=K)
#     model.fit(X_train, y_train)  # fit the model
#     pred = model.predict(X_test)  # make prediction on test set
#     error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
#     rmse_val.append(error)  # store rmse values
#     print('RMSE value for k= ', K, 'is:', error)
#
# curve = pd.DataFrame(rmse_val) #elbow curve
# curve.plot()
# plt.show()

KNN_model = KNeighborsRegressor(n_neighbors = 5)
KNN_model.fit(X_train, y_train)

pred = KNN_model.predict(X_test)
print(mean_squared_error(y_test, pred))
print(r2_score(y_test, pred))

plt.scatter(y_test, pred)
plt.xlabel("Actual Biomass")
plt.ylabel("Predicted Biomass")
plt.title("Actual vs Predicted Biomass")

plt.show()

