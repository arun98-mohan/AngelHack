import hashlib as hasher
import datetime as date

stock_price={"1":"0","2":"0","3":"0","4":"0","5":"0"}
wish_list={}
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode("UTF-8") +
                   str(self.timestamp).encode("UTF-8")  +
                   str(self.data).encode("UTF-8")  +
                   str(self.previous_hash).encode("UTF-8") )
        return sha.hexdigest()

def add_Stock_to_wish_list(id,price):
    wish_list[id]=price

def disp():
    for key, value in stock_price.items():
        print(key, value)

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(),stock_price, "0")

def next_block(last_block,data):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = data
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the chain
while(True):
    choice=input("buy/sell: ")
    if(choice=="sell"):
        add_Stock_to_wish_list(input("Enter Stock ID: "), input("Enter Price: "))
        print("Displaying Stcok LTPs")
        disp()
    elif(choice=="buy"):
        print("Displaying the available stocks to be bought")
        print("Stock, bid amount")
        for key,v in wish_list.items():
            print(key,v)
        id = input("Enter the Stock ID: ")
        value = input("Enter the Value Desired: ")
        for key,value2 in wish_list.items():
            if(id==key and value>=value2):
                stock_price[key]=value
                del wish_list[id]
                flag=1 #transaction has happend
                break
            else:
                flag=0 #transaction has not happend
        if(flag==1):
            block_to_add = next_block(previous_block,stock_price)
            blockchain.append(block_to_add)
            previous_block = block_to_add
            # Printing the block
            print("Block #{} has been added to the blockchain!".format(block_to_add.index))
            print("Hash: {}\n".format(block_to_add.hash))
            flag=0
        elif(flag==0):
            print("Sorry Re-Bid")
        disp()

