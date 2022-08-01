import json
import requests
# import numpy as np
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
        print("inventory = ", inventory, "Units")
        print("cost = ", cost, "Rupees")
        print("sellthrough = ", sellthrough, "Units" )
        print("profitpercentage = ", profitpercentage, "%")
        print("perishability = ", perishability)
        print("OpEx = ", OPEX, "Rupees")
        print("---------------------------------------------------------------")

        pricewithprofit = (cost+OPEX) + ( ( profitpercentage * (cost+OPEX) ) / 100 )
        quantity = inventory - sellthrough
        spoilage =  quantity * (perishability/100)
        SPriceofPerishable = pricewithprofit / (quantity - spoilage)

        print("MSRP : ", pricewithprofit, "Rupees")


        Sprice = (pricewithprofit - SPriceofPerishable)
        intSprice = int(Sprice)

        print("Selling price : ", round(Sprice,2), "Rupees")

        manufacturingCost = inventory * cost
        # print("Total Manufacturing Cost : ", manufacturingCost )
        retSP = inventory * Sprice
        # 
        totalProfit = retSP - manufacturingCost
        print("Quantity = ", round(quantity,2), "Units")
        print("Spoilage = ", round(spoilage,2) )
        print("Removed Perishable Price = ", round(SPriceofPerishable,2) , "Rupees")
        print("---------------------------------------------------------------")

        print("Selling price : ", round(Sprice,2))
        # print("int Sprice: ", intSprice)

        print("---------------------------------------------------------------")
        # print("int Sprice : ", intSprice)
        print("Total Profit : ", round(totalProfit,2), "Rupees")
        print("Total Selling Price : ", round(retSP,2), "Rupees")

    #STRATERGIES IMPLEMENTATION

        num_str = repr(intSprice)
        last_digit_str = num_str[-1]
        last_digit = int(last_digit_str)
        # if Sprice > 500:
        #     x = 9 - int(last_digit_str)
        #     global a
        #     a = Sprice + x
        #     print("Final Price : ", int(a))

            
        # else:
        #     print("Final Price : ", int(Sprice))
        if int(last_digit_str) == 1:
            a1 = round(Sprice-2,2)
            print("Final Price : ", a1, "Rupees")
            # print("Final Price: ", round(Sprice - 2,2), "Rupees")
        elif int(last_digit_str) == 2:
            a1 = round(Sprice - 3,2)
            print("Final Price: ", round(Sprice - 3,2), "Rupees")
        elif int(last_digit_str) == 3:
            a1 = round(Sprice - 4,2)
            print("Final Price: ", round(Sprice - 4,2), "Rupees")
        elif int(last_digit_str) == 4:
            a1 = round(Sprice - 5,2)
            print("Final Price: ", round(Sprice - 5,2), "Rupees")
        elif int(last_digit_str) == 5:
            a1 = round(Sprice - 6,2)
            print("Final Price: ", round(Sprice - 6,2), "Rupees")
        elif int(last_digit_str) == 6:
            a1 = round(Sprice - 7,2)
            print("Final Price: ", round(Sprice - 7,2), "Rupees")
        elif int(last_digit_str) == 7:
            a1 = round(Sprice - 8,2)
            print("Final Price: ", round(Sprice - 8,2), "Rupees")
        elif int(last_digit_str) == 8:
            a1 = round(Sprice - 9,2)
            print("Final Price: ", round(Sprice - 9,2), "Rupees")
        elif int(last_digit_str) == 0:
            a1 = round(Sprice - 1,2)
            print("Final Price: ", round(Sprice - 1,2))
        elif int(last_digit_str) == 9:
            a1 = round(Sprice,2)
            print("Final Price: ", round(Sprice,2))
        
            # print("a = ", a)
            # x = ((a / pricewithprofit)*100)
            # discountpercent = 100-x
            # print(" Discount percentage : ", discountpercent)
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        # print("---------------------------------------------------------------")