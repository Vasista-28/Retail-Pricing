
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
        
        print("---------------------------------------------------------------")
        
        # if perishability == 0:
            # perishability = 1

        # m = (((cost+OPEX) / inventory ) * perishability )
        # wrtperishability = pricewithprofit / (inventory - (inventory - sellthrough))
        

        # print("Price W.R.T Perishability : ",wrtperishability)
        
        pricewithprofit = (cost+OPEX) + ( ( profitpercentage * cost ) / 100 )
        quantity = inventory - sellthrough
        spoilage =  quantity * (perishability/100)
        SPriceofPerishable = pricewithprofit / (quantity - spoilage)

        print("Price With profit : ", pricewithprofit)


        Sprice = (pricewithprofit - SPriceofPerishable)
        intSprice = int(Sprice)
        print("Sprice : ", Sprice)
        print("int Sprice : ", intSprice)

        manufacturingCost = inventory * cost
        print("Manufacturing : ", manufacturingCost )
        retSP = inventory * Sprice
        print("Selling : ", retSP)
        totalProfit = retSP - manufacturingCost
        print("Total Profit : ", totalProfit)
        print("Quantity = ", quantity)
        print("Spoilage = ", spoilage)
        print("Removed Perishable Price = ", SPriceofPerishable)

print("---------------------------------------------------------------")
















# import json
# import requests
# import numpy as np
# with open('data1.json') as json_file:
#     data = json.load(json_file)
#     # print(data)
#     l = len(data)
#     print("Data Length = ",l)
#     for i in range(l):
#         print("Data of ITEM ", i , " : ", data[i])
    
#     # print("\nPrinting nested dictionary as a key-value pair\n") 
#     for i in data:
#         inventory = i["inventory"]
#         cost = i['cost']
#         OPEX = i['OPEX']
#         sellthrough = i['sellthrough']
#         profitpercentage = i['profitpercentage']
#         perishability = i['perishability']
#         print("inventory = ", inventory)
#         print("cost = ", cost)
#         print("sellthrough = ", sellthrough)
#         print("profitpercentage = ", profitpercentage)
#         print("perishability = ", perishability)
#         print("OPEX = ", OPEX)
#         print("---------------------------------------------------------------")

#         pricewithprofit = (cost+OPEX) + ( ( profitpercentage * cost ) / 100 )
#         quantity = inventory - sellthrough
#         spoilage =  quantity * (perishability/100)
#         SPriceofPerishable = pricewithprofit / (quantity - spoilage)

#         print("Price With profit : ", pricewithprofit)


#         Sprice = (pricewithprofit - SPriceofPerishable)
#         intSprice = int(Sprice)
#         print("Sprice : ", Sprice)
#         print("int Sprice : ", intSprice)

#         manufacturingCost = inventory * cost
#         print("Manufacturing : ", manufacturingCost )
#         retSP = inventory * Sprice
#         print("Selling : ", retSP)
#         totalProfit = retSP - manufacturingCost
#         print("Total Profit : ", totalProfit)
#         print("Quantity = ", quantity)
#         print("Spoilage = ", spoilage)
#         print("Removed Perishable Price = ", SPriceofPerishable)
#         print("---------------------------------------------------------------")
#         print("---------------------------------------------------------------")