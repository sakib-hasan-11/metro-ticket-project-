import qrcode as qr
import pandas as pd 
import os
from datetime import datetime
import random

station  = {
    1: "Uttara North",
    2: "Uttara Center",
    3: "Uttara South",
    4: "Pallabi",
    5: "Mirpur 11",
    6: "Mirpur 10",
    7: "Kazipara",
    8: "Shewrapara",
    9: "Agargaon",
    10: "Bijoy Sarani",
    11: "Farmgate",
    12: "Karwan Bazar",
    13: "Motijheel"
    }












def save_data(user_data):
    # convert set into pandas csv file 
    df=pd.DataFrame([user_data])
    # giving a file name to save in laptop 
    file_name = "metro_ticket_data.csv"
    # saving new data in metro ticket file 
    if os.path.exists(file_name): 
        df.to_csv(file_name,mode="a",index=False,header=False)
    else: 
        df.to_csv(file_name,mode="w",index=False,header=True)


def cancel_ticket():
    df=pd.read_csv("metro_ticket_data.csv") # read the file to access data 
    tcketID=input("enter your ticket id here : ")
    if tcketID in df["ticket_id"].values:
        cost=df.loc[df["ticket_id"]==tcketID, "total_cost"].values[0] # access to the total cost cell using ticket id
        df.loc[df["ticket_id"]==tcketID,["cancel_ticket","total_cost"]] = [True,cost*.2] # updating the data 
        df.to_csv("metro_ticket_data.csv",index=False) # saving update to the main file 
        print("your ticket is canceled and 80% taka is refunded through the gateway used .")
    else: 
        print("ticket id not found in the data set ")



def qrcode(data): 
    code= qr.QRCode(
        version= 1,
        box_size=5,
        border=1,
    )
    code.add_data(data)
    code.make(fit=True)
    image= qr.make()
    image.show()

def single_ticket(silent=False):
    # printing stations 
    print("fill the form here : ")
    for key,value in station.items(): 
        print(f"{key}: {value}")


    # taking user input 
    name= input("Enter your name: ")
    number = int(input("enter your number: "))
    current_location = int(input("From (enter the  current station number) : "))
    destination = int(input("To (enter the station number) : "))
    ticket_id =genarate_ticket_id()


    # counting total tickets 
    if selection == 1: 
        total_ticket=1
    else: 
        total_ticket=n


    # counting total amount
    cost_per_station=20
    if destination in station and current_location in station:
        total_distance = abs(current_location-destination)
    else: 
        print("wrong destination")
        return None
    total_cost = total_distance*cost_per_station
    if not silent:
        print(f"you have to pay {total_cost} taka")

        # makieing qr code
        qrcode_data = f"Ticket ID: {ticket_id}\nName: {name}\nFrom: {station[current_location]} To: {station[destination]}\nTotal Cost: {total_cost} BDT"
        qrcode(data=qrcode_data)

    #csv data 
    userdata = {
    "ticket_id": ticket_id,
    "name": name,
    "number": number,
    "current_location": station[current_location],
    "destination": station[destination],
    "total_cost": total_cost,
    "total_ticket": total_ticket,
    "canceled ticket": False

    }

    save_data(user_data=userdata)
    return userdata

def multi_ticket(n):
    multi_amount=0
    all_ticket=[]
    for i in range(1,n+1):
        print(f"person {i} :")
        ticket=single_ticket(silent=True)
        multi_amount += ticket["total_cost"]
        print(f"\nTotal cost for {n} tickets: {multi_amount} Taka.")

def genarate_ticket_id(): 
    now = datetime.now()
    date_str = now.strftime("%y%m%d%H%M%S")  
    random_int = random.randint(10,99)
    return f"MT{date_str}_{random_int}"



print("welcome to metro ticket service")
print("select your option : \n 1.single ticket \n 2.multiple tickets \n 3.cancel ticket")
selection = int(input("your choise in number: "))
if selection == 1: 
    single_ticket()
elif selection == 2: 
    n=int(input("how many ticket do you want: "))
    multi_ticket(n)
elif selection == 3: 
    cancel_ticket()






















