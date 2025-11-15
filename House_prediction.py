# import linearregression sub-module from sklearn libeary
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# mention flat type 1bhk or 2bhk or 3bhk
price = [[20],[35],[45],[55],[85],[95]]

# and mention the particuler flat price
bhk = [1,1.5,2,2.5,3,3.5]

# import the linear regression model to predict value
model = LinearRegression()

# fit the model to accoding to the flat size and price 
model.fit(price,bhk)

# enter the amount
your_money = float(input("Enter Your Amount in Lakh:- "))

# if budget s <20lac can't buy a flat 
if your_money < 20:
    print(f"Opps You Can't Buy any Flat in This Budget{your_money} Lakh/-")
else:
    # predict the actual flat size accoding to the amount
    bhk_flat = model.predict([[your_money]])
    print(f"if you budget is {your_money}Lakh/- you buy {bhk_flat[0]:.2f}Bhk Flat in kolkata")
