x=[1,2,3,4,5]
y=[0,0,0,1,1]
m=0
b=0
learning_rate=0.01
for epoch in range(1000):
    for i in range(len(x)):
        y_pred=m*x[i]+b
        error=y[i]-y_pred
        m+=learning_rate*error*x[i]
        b+=learning_rate*error
print("learned slope m:",m)
print("learned interscept b:",b)
