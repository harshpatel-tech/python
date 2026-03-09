import math 
X=[1,2,3,4,5]
y=[0,0,0,1,1]
def sigmoid(x):
    return 1/(1+math.exp(-x))
w=0
b=0
learning_rate=0.1
for epoch in range(1000):
    for i in range(len(X)):
        x=X[i]
        target=y[i]
        z=w*x+b
        prediction=sigmoid(z)
        error=prediction-target
        w-=learning_rate*error*x
        b-=learning_rate*error
test_input=3.8
z=w*test_input+b
prediction=sigmoid(z)
print(prediction)
