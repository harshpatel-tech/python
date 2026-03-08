import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([0,0,0,1,1])
model=LinearRegression()
model.fit(x,y)
prediction=model.predict([[6]])
print(prediction)

