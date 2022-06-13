
import json
 
with open('data.json') as json_file:
    data = json.load(json_file)

    print("Data of ITEM 1 : ", data['item1'][0])
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['item1']:
        inventory = i['inventory']
        cost = i['cost']
        OPEX = i['OPEX']
        sellthrough = i['sellthrough']
        profitpercentage = i['profitpercentage']
        perishability = i['perishability']
        print("inventory = ", inventory)
        print("cost = ", cost)
        print("sellthrough = ", sellthrough)
        print("profitpercentage = ", profitpercentage)
        print("perishability = ", perishability)
        print("OPEX = ", OPEX)
        if perishability == 0:
            perishability = 1

        m = (((cost+OPEX) / inventory ) * perishability )
        pricewithprofit = cost + ( ( profitpercentage * cost ) / 100 )
        wrtperishability = pricewithprofit / (inventory - (inventory - sellthrough))
        
        print(pricewithprofit)

        print(wrtperishability)
        
        Sprice = (pricewithprofit - wrtperishability)
        intSprice = int(pricewithprofit - wrtperishability)
        print(Sprice)
        print(intSprice)

        manufacturingCost = inventory * cost
        print("Manufacturing : ", manufacturingCost )
        retSP = inventory * Sprice
        print("Selling ", retSP)
        totalProfit = retSP - manufacturingCost
        print("Total Profit : ", totalProfit)

print("--------------------------------------------------------")
















# # import pandas as pd

# # def retailPricing(imp, *args):
# #     inv=100
# #     sellthrough=20
# #     cost=10
# #     profitpercentage=2
# #     perishability=0
# #     OPEX=25
# #     print(OPEX + cost)
# #     print(inv+sellthrough+cost+profitpercentage+perishability+OPEX)
# # retailPricing(inv,sellthrough,cost,profitpercentage,perishability,OPEX)



# def fn(a):
#     return 10 * a

# lst = [1, 2, 3, 4, 5, 6]

# for i in lst:
#     lst[0] = lst[0]*10
#     print(lst[0])
#     print(lst[1])




# lst[1] = (10*lst[0])+50


# ans = []

# for lst[0] in lst:
#     x = fn(lst[0])
#     ans.append(x)
# print(ans)