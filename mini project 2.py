org_adm_psw="Naveen"
veg=['brinjal','tomato','onion']
quantity=[10,15,20]
price=[45,15,20]
cost_price=[40,13,18]
cost=0

total_bill=0
total_revenue=0
total_profit=0

profit_item=[]
each_profit=[]

user_names=[]
user_mobile=[]
each_bill=[]
print("----------------------Login Page----------------------")
while True:
    person=input("Are you Admin or Customer:?").strip().lower()
    if person == "admin":
        print("----------------------Admin Page----------------------")
        adm_psw=input("Enter Password:")
        if adm_psw==org_adm_psw:
            print("Welcome!!! Admin\n")
            print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
            for i,j,k in zip(veg,quantity,price):
                print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
            print()
            
            while True:
                ch=int(input("1.Add new vegetables\n2.Remove new Vegetables\n3.Modify Vegetables\n4.View Inventory\n5.View user details\n6.View report\n7.Total Revenue and Itemized Profit\n8.exit\nChoose the operation:"))
                if ch==1:
                    while True:
                        item=input("Enter the vegetable that you want to add:?").strip().lower()
                        if item not in veg:
                            veg.append(item)
                            qnty=int(input("How many kgs you want to add?:"))
                            crt=int(input("Enter the cost Price of the given item :"))
                            cost_price.append(crt)
                            quantity.append(qnty)
                            prc=int(input("Enter the selling Price of the given item :"))
                            price.append(prc)

                            print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                            for i,j,k in zip(veg,quantity,price):
                                print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                            print()
                            
                        else:
                            ch=input("Do you want to modify the quantity:(yes/no)")
                            if ch=="yes":
                                qnty=int(input("How many kgs you want to add:?"))
                                idx=veg.index(item)
                                quantity[idx]=quantity[idx]+qnty
                                print(item,"added")

                            print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                            for i,j,k in zip(veg,quantity,price):
                                print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                            print()
                        op=input("Do you want to add more?(yes/no):")
                        if op=="no":
                            break
                            
                elif ch==2:
                    while True:
                        item=input("Enter the veg that you want to remove:").strip().lower()
                        if item in veg:
                            idx=veg.index(item)
                            qnty=int(input("How many kgs you want to remove:"))
                            if qnty<quantity[idx]:
                                quantity[idx]=quantity[idx]-qnty
                            elif qnty==quantity[idx]:
                                quantity.remove(quantity[idx])
                                cost_price.remove(cost_price[idx])
                                price.remove(price[idx])
                                veg.remove(item)
                            else:
                                print("quantity that you entered is exceeding\n")
                                print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                                for i,j,k in zip(veg,quantity,price):
                                    print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                        else:
                            print("Item not available to remove")
                        rr=input("Do you want to remove more?(yes/no):")
                        if rr=="no":
                            break
                elif ch==3:
                    while True:
                        op=input("For what veg you want to change the price?:").strip().lower()
                        if op not in veg:
                            print(op,"not available")
                        else:
                            cp=int(input("1.cost price?\n2.selling price?"))
                            if cp==1:
                                st=int(input("1.Increase the price\n2.Decrease the price\n Choose the operation:\n"))
                                pr=int(input("How much you want to change:?"))
                                idx=veg.index(op)
                                if st==1:
                                    cost_price[idx]=cost_price[idx]+pr
                                else:
                                    cost_price[idx]=cost_price[idx]-pr
                                '''for i,j in zip(cost_price,price):
                                    print("cost_price=",i,'-',"selling-price=",j)'''
                            else:
                                st=int(input("1.Increase the price\n2.Decrease the price\n Choose the operation:\n"))
                                pr=int(input("How much you want to change:?"))
                                idx=veg.index(op)
                                if st==1:
                                    price[idx]=price[idx]+pr
                                else:
                                    price[idx]=price[idx]-pr
                                print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                                for i,j,k in zip(veg,quantity,price):
                                    print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                                print()
                        rr=input("Do you want to modify more?(yes/no):")
                        if rr=="no":
                            break
                            
                elif ch==4:
                    print("*"*10+"INVENTORY"+"*"*10)
                    print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                    for i,j,k in zip(veg,quantity,price):
                        print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                    print()
                        
                elif ch==5:
                    print("*"*10+"USER DETAILS"+"*"*10)
                    print("{:<20} {:<10} {:<10}".format("USER_NAME", "MOBILE", "BILL"))
                    for i,j,k in zip(user_names,user_mobile,each_bill):
                        print("{:<20} {:<10} {:<20}".format(i, j,k))
                    print()
                    
                elif ch==6:
                    print("*"*10+"REPORT"+"*"*10)
                    print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                    for i,j,k in zip(veg,quantity,price):
                        print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                    print()
                    
                elif ch==7:
                    print("*"*10+"REVENUE"+"*"*10)
                    print(total_revenue)
                    print()
                    print()

                    
                    print("*"*10+"ITEMIZED_PROFIT"+"*"*10)
                    for i,j in zip(profit_item,each_profit):
                        print(i,'-',j)
                            
                    print("*"*24)

                elif ch==8:
                    break
                else:
                    print("Choose the correct operation:")
                    break
                            
        else:
            print("password incorrect")

    elif person=="customer":
        cart=[]
        cart_price=[]
        cart_qty=[]
        print("----------------------Customer Page----------------------")
        print("Welcome!! Customer...\n")
        user_name=input("Enter Your Name:")
        mobile_no=int(input("Enter Your Mobile number:"))
        user_names.append(user_name)
        user_mobile.append(mobile_no)

        print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
        for i,j,k in zip(veg,quantity,price):
            print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
        print()
        while True:
            op=(input("1.Add to cart\n2.Remove from cart\n3.Modify the cart\n4.View cart\n5.Billing\n6.Exit\n\nChoose the operation:"))
            if op.isalpha():
                print('enter valid option')
            elif op==1:
                while True:
                    item=input("What vegetable you want add:?").strip().lower()
                    if item in veg:
                        if item in cart:
                            ch=input(f"{item} already in the cart. Do you want to buy ?(yes/no):")
                            if ch=="yes":
                                qty=int(input("How many kgs you want:?"))
                                idx=cart.index(item)
                                idx1=veg.index(item)
                                if qty<quantity[idx1]:
                                    cost=price[idx1]*qty
                                    cart_price[idx]=cart_price[idx]+cost
                                    cart_qty[idx]=cart_qty[idx]+qty
                                    quantity[idx1]=quantity[idx1]-qty
                                elif qty==quantity[idx1]:
                                    cost=price[idx1]*qty
                                    cart_price[idx]=cart_price[idx]+cost
                                    cart_qty[idx]=cart_qty[idx]+qty
                                    quantity.remove(quantity[idx1])
                                    cost_price.remove(cost_price[idx1])
                                    price.remove(price[idx1])
                                    veg.remove(item)
                                else:
                                    print(f"Out of stock..{item} has only {quantity[idx1]} kgs")
                        else:
                            qty=int(input("How many kgs you want:?"))
                            idx=veg.index(item)
                            if qty<quantity[idx]:
                                cart.append(item)
                                cost=price[idx]*qty
                                cart_price.append(cost)
                                cart_qty.append(qty)
                                quantity[idx]=quantity[idx]-qty
                            elif qty==quantity[idx]:
                                cart.append(item)
                                cost=price[idx]*qty
                                cart_price.append(cost)
                                cart_qty.append(qty)
                                #cost_price_new[idx]=cost_price_new[idx]+cost_price[idx]
                                cost_price.remove(cost_price[idx])
                                quantity.remove(quantity[idx])
                                price.remove(price[idx])
                                veg.remove(veg[idx])
                            else:
                                print(f"Out of stock..{item} has only {quantity[idx]} kgs")
                    else:
                        print(item,"not available\n")
                    ch=input("Do you want to buy more..?")
                    print()
                    if ch=="no":
                        print("*"*20+"STORE"+"*"*20)
                        print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                        for i,j,k in zip(veg,quantity,price):
                            print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                        print()
                        print("*"*20+"CART"+"*"*20)
                        print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                        for i,j,k in zip(cart,cart_qty,cart_price):
                            print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                        print()
                        break
            elif op==2:
                while True:
                    item=input("What do you want remove:?").strip().lower()#
                    if item in cart:#yes
                        if item in veg:#
                            idx1=veg.index(item)#
                            idx=cart.index(item)#
                            qty=int(input("How many kgs you want to remove:?"))#
                            if qty<cart_qty[idx]:#
                                cost=price[idx1]*qty#
                                cart_price[idx]=cart_price[idx]-cost##
                                cart_qty[idx]=cart_qty[idx]-qty#
                                quantity[idx1]=quantity[idx1]+qty#
                                        
                            elif qty==cart_qty[idx]:#
                                cart_price.remove(cart_price[idx])#
                                cart_qty.remove(cart_qty[idx])
                                cart.remove(item)
                                quantity[idx1]=quantity[idx1]+qty#

                            else:
                                print(f"{item}you want to remove has only {cart_qty[idx]}kgs left")
                                print()
                        else:
                            qty=int(input("How many kgs you want to remove:?"))
                            idx=cart.index(item)
                            if qty<cart_qty[idx]:
                                cost=cart_price[idx]//cart_qty[idx]
                                cart_price[idx]=cart_price[idx]-(cost*qty)
                                cart_qty[idx]=cart_qty[idx]-qty
                                veg.append(item)
                                quantity.append(qty)
                                price.append(cost)
                                        
                            elif qty==cart_qty[idx]:
                                cost=cart_price[idx]//cart_qty[idx]
                                veg.append(item)
                                quantity.append(qty)
                                price.append(cost)
                                        
                                cart_qty.remove(cart_qty[idx])
                                cart_price.remove(cart_price[idx])   
                                cart.remove(item)
                                                                      
                            else:
                                print(f"{item} you want to remove has only {cart_qty[idx]}kgs left")
                                print()
                    else:
                        print(item,"not available in the cart\n")
                        print()
                    ch=input("Do you want to remove more..?")
                    print()
                    if ch=="no":
                        print()
                        print("*"*20+"STORE"+"*"*20)
                        print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE/KG"))
                        for i,j,k in zip(veg,quantity,price):
                            print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                        print()
                        print("*"*20+"CART"+"*"*20)
                        print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                        for i,j,k in zip(cart,cart_qty,cart_price):
                            print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                        print()
                        break
            elif op==3:
                while True:
                    item=input("For what vegetable do you want to change the quantity:").strip().lower()
                    if item in cart:
                        if item in veg:
                            idx1=veg.index(item)
                            idx=cart.index(item)
                            rr=int(input("1.Increase\n2.Decrease:"))
                            if rr==1:
                                qty=int(input("How many kgs you want to add:?"))
                                if qty<quantity[idx1]:
                                    cost=price[idx1]*qty
                                    cart_price[idx]=cart_price[idx]+cost
                                    cart_qty[idx]=cart_qty[idx]+qty
                                    quantity[idx1]=quantity[idx1]-qty
                                elif qty==quantity[idx1]:
                                    cost=price[idx1]*qty
                                    cart_price[idx]=cart_price[idx]+cost
                                    cart_qty[idx]=cart_qty[idx]+qty
                                    price.remove(price[idx1])
                                    quantity.remove(quantity[idx1])
                                    veg.remove(item)
                                else:
                                    print(f"{item}you want to remove has only {cart_qty[idx]}kgs left")
                                    print()
                                print("*"*20+"CART"+"*"*20)
                                print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                                for i,j,k in zip(cart,cart_qty,cart_price):
                                    print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                                print()
                                print("*"*10+"COST-PRICES"+"*"*10)
                                for i,j in zip(cost_price,price):
                                    print("cost_price=",i,'-',"selling-price=",j)
                                break
                    

                            elif rr==2:
                                qty=int(input("How many kgs you want to remove:?"))
                                idx=cart.index(item)
                                if qty<cart_qty[idx]:
                                    cost=price[idx1]*qty
                                    cart_price[idx]=cart_price[idx]-cost
                                    cart_qty[idx]=cart_qty[idx]-qty
                                    quantity[idx1]=quantity[idx1]+qty
                                elif qty==cart_qty[idx]:
                                    cart_price.remove(cart_price[idx])
                                    cart_qty.remove(cart_qty[idx])
                                    cart.remove(item)
                                    quantity[idx1]=quantity[idx1]+qty
                                else:
                                    print(f"{item}you want to remove has only {cart_qty[idx]}kgs left")
                                    print()
                            else:
                                print("choose the correct operation:")
                                break
                            print("*"*20+"CART"+"*"*20)
                            print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                            for i,j,k in zip(cart,cart_qty,cart_price):
                                print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                            print()
                            break
                                
                        else:
                            rr=int(input("1.Increase\n2.Decrease:"))
                            if rr==1:
                                print("Out of Stock!!!")
                            elif rr==2:
                                qty=int(input("How many kgs you want to remove:?"))
                                idx=cart.index(item)
                                if qty<cart_qty[idx]:
                                    cost=cart_price[idx]//cart_qty[idx]
                                    #cost=cart_price[idx]*qty
                                    cart_price[idx]=cart_price[idx]-cost*qty
                                    cart_qty[idx]=cart_qty[idx]-qty
                                    veg.append(item)
                                    quantity.append(qty)
                                    price.append(cost)
                                elif qty==cart_qty[idx]:
                                    price=cart_price[idx]//cart_qty[idx]
                                    cart_rice.remove(cart_price[idx])
                                    cart_qty.remove(cart_qty[idx])
                                    cart.remove(item)
                                    veg.append(item)
                                    quantity.append(qty)
                                    price.append(price*qty)
                                else:
                                    print(f"{item}you want to remove has only {cart_qty[idx]}kgs left")
                                    print()
                            else:
                                print("choose the correct operation:")
                                break
                            print("*"*20+"CART"+"*"*20)
                            print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                            for i,j,k in zip(cart,cart_qty,cart_price):
                                print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                            print()
                            break
                    else:
                        print(item,"not avaliable in the cart.")
                    ss=input("DO you want to modify the cart again?(yes/no):")
                    if ss=="yes":
                        break
            elif op==4:
                print("*"*20+"CART"+"*"*20)
                print("{:<20} {:<10} {:<10}".format("VEGETABLE", "QUANTITY", "PRICE"))
                #for i,j,k in zip(cart,cart_qty,cart_price):
                   # print("{:<20} {:<10.1f} {:<20.2f}".format(i, j, k))
                print()
                
                
            elif op==5:
                total_bill=0
                for i in cart_price:
                    total_bill=total_bill+i
                each_bill.append(total_bill)
                total_revenue=total_revenue+total_bill
                
                print("*" * 26)
                print("{:^26}".format("BILL")) 
                print("*" * 26)
                print("{:<15} {:>10}".format("Item", "Price (₹)"))
                print("-" * 26)

                for i, j in zip(cart, cart_price):
                    print("{:<15} {:>10}".format(i, j))

                print("-" * 26)
                print("{:<15} {:>10}".format("Total Bill", total_bill))
                print("*" * 26)


                for i in cart:#tomato
                    idx=cart.index(i)#0
                    idx1=veg.index(i)#1
                    cqty=cart_qty[idx]#4
                    cprice=cart_price[idx]#60
                    coprice=cost_price[idx1]
                    if i in profit_item:#[]
                        idx2=profit_item.index(i)#0
                        each_profit[idx2]=each_profit[idx2]+((cprice)-(coprice*cqty))
                    else:
                        profit_item.append(i)
                        idx3=profit_item.index(i)
                        each_profit.append((cprice)-(coprice*cqty))
                        
                
            elif op==6:
                break
            else:
                print("Choose the correct operation")
                
                    
     
    
