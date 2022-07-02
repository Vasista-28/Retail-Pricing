import json
import requests
import numpy as np
import webbrowser
import time


with open('data1.json') as json_file:
    data = json.load(json_file)
    # print(data)
    l = len(data)
    print("Data Length = ",l)
    print("Printing nested dictionary as a key-value pair") 

    for i in range(l):
        print("Data of ITEM ", i + 1 , " : ", data[i])
        print("---------------------------------------------------------------")

    

    for i in data:
        inventory = i["inventory"]
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
        print("---------------------------------------------------------------")
        print("Sprice : ", Sprice)
        print("int Sprice: ", intSprice)


    #STRATERGIES IMPLEMENTATION

        num_str = repr(intSprice)
        last_digit_str = num_str[-1]
        last_digit = int(last_digit_str)
        if Sprice > 500:
            x = 9 - int(last_digit_str)
            global a
            a = Sprice + x
            print("Final Price : ", int(a))
            
        else:
            print("Final Price : ", int(Sprice))
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")