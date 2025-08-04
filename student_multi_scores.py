import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
#Read the data
df = pd.read_csv('student_multi_score.csv')
#seperate features(X) & Label(Y)
X = df[['Hours_Studied', 'Attendance_Percentage', 'Practice_Tests_Taken']]
Y = df['Score']
#split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, Y_train)
#make prediction
Y_pred = model.predict(X_test)
#Evaluate the model
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R^2 Score:",r2_score(Y_test, Y_pred))
# Take input from user
hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance percentage: "))
tests_taken = int(input("Enter number of practice tests taken: "))
custom_input = [[hours, attendance, tests_taken]]
predict_score = model.predict(custom_input)
print(f"Predicted score for {custom_input[0]}={predict_score[0]:2f}")

