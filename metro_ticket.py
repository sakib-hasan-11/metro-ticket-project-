import qrcode as qr
import pandas as pd 
import os

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
    13: "Motijheel"}

def save_data(name,number,current_location,destination,total_cost,total_ticket):
    user_data= { # saving user data in a set 
        "name":name,
        "number":number,
        "current_location":station[current_location],
        "destination":station[destination],
        "total_cost": total_cost,
        "total_ticket":total_ticket
    }
    # convert set into pandas csv file 
    df=pd.DataFrame([user_data])
    # giving a file name to save in laptop 
    file_name = "metro_ticket_data.csv"
    # saving new data in metro ticket file 
    if os.path.exists(file_name): 
        df.to_csv(file_name,mode="a",index=False,header=False)
    else: 
        df.to_csv(file_name,mode="w",index=False,header=True)


def qrcode(): 
    code= qr.QRCode(
        version= 1,
        box_size=5,
        border=1,
    )
    code.add_data("thanks to be with us")
    code.make(fit=True)
    image= qr.make()
    image.show()


def single_ticket(silent=False):
    print("fill the form here : ")
    for key,value in station.items(): 
        print(f"{key}: {value}")
    name= input("Enter your name: ")
    number = int(input("enter your number: "))
    current_location = int(input("From (enter the  current station number) : "))
    destination = int(input("To (enter the station number) : "))
    cost_per_station = 20 
    if selection == 1: 
        total_ticket=1
    else: 
        total_ticket=n
    if destination in station and current_location in station:
        total_distance = abs(current_location-destination)
    else: 
        print("wrong destination")
        return None
    total_cost = total_distance*cost_per_station
    if not silent:
        print(f"you have to pay {total_cost} taka")
        qrcode()
    save_data(name,number,current_location,destination,total_cost,total_ticket)
    ticket_info={
        "name":name,
        "number":number,
        "current_location":current_location,
        "destination":destination,
        "total_cost":total_cost,
        "total_ticket":total_ticket
    }
    return ticket_info




def multi_ticket(n):
    multi_amount=0
    all_ticket=[]
    for i in range(1,n+1):
        print(f"person {i} :")
        ticket=single_ticket(silent=True)
        multi_amount+= ticket["total_cost"]
        print(f"\nTotal cost for {n} tickets: {multi_amount} Taka.")

    

print("welcome to metro ticket service")
print("select your option : \n 1.single ticket \n 2.multiple tickets")
selection = int(input("your choise in number: "))
if selection == 1: 
    single_ticket()
elif selection == 2: 
    n=int(input("how many ticket do you want: "))
    multi_ticket(n)
























