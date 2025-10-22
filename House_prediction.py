# import linearregression sub-module from sklearn libeary
from sklearn.linear_model import LinearRegression

# mention flat type 1bhk or 2bhk or 3bhk
bhk = [1],[1.5],[2],[2.5],[3],[3.5],[4],[5]

# and mention the particuler flat price
price = [2000000,3500000,4500000,5500000,8500000,9500000,120000000,150000000]

# import the linear regression model to predict value
model = LinearRegression()

# fit the model to accoding to the flat size and price 
model.fit(bhk,price)

# enter the amount
your_money = float(input("Enter Your Amount:- "))

# if budget s <20lac can't buy a flat 
if your_money < 2000000:
    print(f"Opps You Can't Buy any Flat in This Budget{your_money}/-")
else:
    # predict the actual flat size accoding to the amount
    predict_price = model.predict([[your_money]])
    print(f"if you budget is {your_money}/- you buy {predict_price} Flat in kolkata")
