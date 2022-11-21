

import time
print("WLECOME TO RED BUS")
time.sleep(3)
print("press 1 for booking ")
print("press 2 for exit")
customer_choice=int(input("enter the choice : "))
if customer_choice==2:
    quit()
starting=["banglore(10:00)"]
classes=["SITTING","SLEEPER","SEMI-SLEEPER"]
sitting_list=[1,2,3,4,5,6,7,8,9,10]
sleeper_list=[1,2,3,4,5,6,7,8,9,10]
semi_sleeper_list=[1,2,3,4,5,6,7,8,9,10]
while(customer_choice==1):
    class Redbus:
        def __init__(self,starting, classes, sitting_list, sleeper_list, semi_sleeper_list):
            self.flightslist=starting
            self.Classes_list = classes
            self.sitting_list = sitting_list
            self.sleeper_list = sleeper_list
            self.semi_sleeper_list = semi_sleeper_list
            print("Bus avalible are",self.flightslist)
            print("----------------------------------------------------")
            print("TYPE : ", self.Classes_list)
            print("----------------------------------------------------")
            print("SITTING seats are : ", self.sitting_list)
            print("----------------------------------------------------")
            print("SLEEPER list are : ", self.sleeper_list)
            print("---------------------------------------------------")
            print("SEMI-Sleeper seats are : ", self.semi_sleeper_list)

        def selected_class_seat(self, customer_requested_class, seat_selected):
            self.class_selected = customer_requested_class
            self.seat_selected = seat_selected
            msg1 = ("Bus have the requested seat and will be confirmed to your name")
            msg2 = ("Bus dont have the requested seat and will be not be confirmed to your name")
            if (self.class_selected == 1):
                if (self.seat_selected in self.sitting_list):
                    print(msg1)
                    sitting_list.remove(self.seat_selected)
                    return sitting_list
                else:
                    print(msg2)
                    return sitting_list
            elif (self.class_selected == 2):
                if (self.seat_selected in self.sleeper_list):
                    print(msg1)
                    sleeper_list.remove(self.seat_selected)
                    return sleeper_list
                else:
                    print(msg2)
                    return sleeper_list
            elif (self.class_selected == 3):
                if (self.seat_selected in self.semi_sleeper_list):
                    print(msg1)
                    semi_sleeper_list.remove(self.seat_selected)
                    return semi_sleeper_list
                else:
                    print(msg2)
                    return semi_sleeper_list
            if(self.class_selected==4):
                 quit()
            #else:
                #print("invalid entry")
            return self.class_selected


        def confirm_request(self):
            self.couch_selected = customer_requested_couch
            self.seat_selected = seat_selected
            msg1 = ("Bus have the requested seat and will be confirmed to your name")
            msg2 = ("Bus dont have the requested seat and will be not be confirmed to your name")
            if (self.couch_selected == 1):
                if (self.seat_selected in self.sitting_list):
                    print(msg1)
                    sitting_list.remove(self.seat_selected)
                    return sitting_list
                else:
                    print(msg2)
                    return sitting_list
            elif (self.couch_selected == 2):
                if (self.seat_selected in self.sleeper_list):
                    print(msg1)
                    sleeper_list.remove(self.seat_selected)
                    return sleeper_list
                else:
                    print(msg2)
                    return sleeper_list
            elif (self.couch_selected == 3):
                if (self.seat_selected in self.semi_sleeper_list):
                    print(msg1)
                    semi_sleeper_list.remove(self.seat_selected)
                    return semi_sleeper_list
                else:
                    print(msg2)
                    return semi_sleeper_list


        def cancle_request(self,cancled_class,cancled_info):
            msg1 = ("Bus still has the requested seat hence cant be cancled")
            msg2 = ("Bus doeesnt have the requested seat and will be cancled")
            if (cancled_class == 1):
                if (cancled_info in sitting_list):
                    print(msg1)
                    return sitting_list
                else:
                    print(msg2)
                    sitting_list.append(cancled_info)
                    sitting_list.sort()
                    return sitting_list
            elif (cancled_class == 2):
                if (cancled_info in sleeper_list):
                    print(msg1)
                    return sleeper_list
                else:
                    print(msg2)
                    sleeper_list.append(cancled_info)
                    sleeper_list.sort()
                    return sleeper_list
            elif (cancled_class == 3):
                if (cancled_info in semi_sleeper_list):
                    print(msg1)
                    return semi_sleeper_list
                else:
                    print(msg2)
                    semi_sleeper_list.append(cancled_info)
                    semi_sleeper_list.sort()
                    return semi_sleeper_list


    class Customer:
        def class_request(self):
            print("press 1 for Sitting")
            print("press 2 for Seeper")
            print("press 3 for Semi-Sleeper")
            print("press 4 for exit")
            custo_choice_class = int(input("enter the choice : "))
            return custo_choice_class

        def request_ticket(self, classes, customer_requested_class, sitting_list, sleeper_list, semi_sleeper_list):
            self.request_class = customer_requested_class
            self.sitting_list = sitting_list
            self.sleeper_list = sleeper_list
            self.semi_sleeper_list =semi_sleeper_list
            msg1 = ("seat avilable and confirmed")
            msg2 = ("seat not avalible")
            if (self.request_class == 1):
                seat_number = int(input("enter the seat number"))
                if (seat_number in self.sitting_list):
                    print(msg1)
                else:
                    print(msg2)
                return (seat_number)

            if (self.request_class == 2):
                seat_number = int(input("enter the seat number"))
                if (seat_number in self.sleeper_list):
                    print(msg1)
                else:
                    print(msg2)
                return (seat_number)

            if (self.request_class == 3):
                seat_number = int(input("enter the seat number"))
                if (seat_number in self.semi_sleeper_list):
                    print(msg1)
                else:
                    print(msg2)
                return (seat_number)
            if (self.request_class == 4):
                quit()

            else:
                print("invalid choice of class")

        def cancle_class(self):
            print("press 1 for cancel in Sitting ")
            print("press 2 for cancel in Sleeper")
            print("press 3 for cancel in Semi_sleeper")
            cancle_choice_class = int(input("enter the choice : "))
            return cancle_choice_class


        def cancle_request(self,cancled_class,confirmed_class_seat):
            msg1 = ("seat selcted is valid and will be pushed to canclation")
            msg2 = ("seat selected is invalid and cant be cancle")
            if (cancled_class == 1):
                seat_number = int(input("enter the seat number"))
                if (seat_number in sitting_list):
                    print (msg2)
                else:
                    print (msg1)
                return (seat_number)

            if (cancled_class == 2):
                seat_number = int(input("enter the seat number"))
                if (seat_number in sleeper_list):
                    print (msg2)
                else:
                    print (msg1)
                return (seat_number)

            if (cancled_class == 3):
                seat_number = int(input("enter the seat number"))
                if (seat_number in semi_sleeper_list):
                    print (msg2)
                else:
                    print (msg1)
                return (seat_number)


            else:
                return ("invalid choice of class")


    a1 = Redbus(starting, classes, sitting_list, sleeper_list, semi_sleeper_list)
    #a1 = Airline()
    c1 = Customer()
    customer_requested_class = c1.class_request()
    seat_selected = c1.request_ticket(classes, customer_requested_class,sitting_list, sleeper_list, semi_sleeper_list)
    confirmed_class_seat = a1.selected_class_seat(customer_requested_class, seat_selected)
    print(confirmed_class_seat)
    cancled_class=c1.cancle_class()
    cancled_info = c1.cancle_request(cancled_class,confirmed_class_seat)
    cancled_confirm=a1.cancle_request(cancled_class,cancled_info)
    print(cancled_confirm)
    # print(customer_requested_couch)
    # print(seat_selected)
    # print(confirmed_couch_seat)













