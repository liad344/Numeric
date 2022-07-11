import matplotlib.pyplot as plt

xk = float(1/12) 
prev = float(1/3)

accu = []
semi = []

def accurate (k): 
    return float(4**(1-k))/3

def semi_accurate(k):
    global xk 
    global prev
    
    if(k==1):
        return prev
    if(k==2):
        return xk

    next = 2.25*xk - 0.5*prev
    prev = xk
    xk = next 

    return next 

def plot_accurate():
    global accu
    for x in range(40):
        accu.append(accurate(x+1))

def plot_semi():
    global semi
    for x in range(40):
     semi.append(semi_accurate(x+1))

plot_accurate()
plot_semi()

logk = []
for i in range(40):
    logk.append(i+1)

plt.yscale('log',base=2) 
plt.scatter(logk, accu,  color=("red"))
plt.scatter(logk, semi, color=("blue"))
plt.show()
