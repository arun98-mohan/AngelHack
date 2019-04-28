#Prototyping with Five Farms and each farm considered to be one single share
#For Development Purpose - One Farm = One Share
#Stocks file format - stock_id,ltp

import csv
wish_list={}

def read_Share_values():
    #Reading the Share Values
    with open("share_values.csv","r") as f:
        print("Share Values")
        lis=[line.split() for line in f] #creating list of list
        print("Share ID , Last Traded Price")
        for i,x in enumerate(lis):
            print("{1}".format(i,x))
        for i in f:
            print(i)

#When a person is interested in selling the stock, he adds his stock
#to the wish list

def add_Stock_to_wish_list(id,price):
    wish_list[id]=price

#Buy a stock
#buy when wish list has a stock of same ID and value less than or equal to requested amount

def buy_Stock(id,price):
    for key,value in wish_list:
        if(id==key and value<=price):
            del wish_list[id]
            return 0
        else:
            return 1


choice=input("Buy or Sell [Enter buy || sell] or see for Current Value ")
if(choice=="buy"):
    id=input("Enter the Stock ID: ")
    value=input("Enter the Value Desired: ")
    temp=buy_Stock(id,value)
    if(temp==1):
        print("Sorry Enter a better Amount")
elif(choice=="sell"):
    id=input("Enter the Stock ID: ")
    value=input("Enter the Minimum amount to be sold for: ")
    add_Stock_to_wish_list(id,value)
elif(choice=="see"):
    read_Share_values()

