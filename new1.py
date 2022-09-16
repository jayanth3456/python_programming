print("welcome to beta restuarant")
a = input("costumer entry : yes/no")
if a == "yes":
    print("welcome sir")
    b = input("emteesukuntaru sir-veg/non-veg")
    if b == "veg":

        e = input("starters/biriyani : ")

        if  e == "starters":
            print("list of items")
            starters = ["veg manchurian","gobi manchurian","mini pizza"]
            print(starters)
            d = input("choose your starter")

            if d == "veg manchurian":
                print("veg manchurian : 140,"+"gst 10% : 14,"
                      "total : 154")
                amount = 154
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif d == "gobi manchurian":
                print("veg manchurian : 160,"+"gst 10% : 16,"
                      "total : 176")
                amount = 176
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif d == "mini pizza":
                print("veg manchurian : 180,"+"gst 10% : 10,"
                      "total : 198")
                amount = 198
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")
                 
        elif e == "biriyani":
            print("list of items")
            print("[veg biriyani    : 200]")
            print("[paneer biriyani : 250]")
            print("[kaju biriyani   : 300]")
            c = input("i want :")
            
            if c == "veg biriyani" or "veg":
                print("veg biriyani : 200 ,"+"gst 10% : 20 ,"
                  "total : 220")
                amount = 220
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")
                    
            elif c == "paneer biriyani" or "paneer":
                print("paneer biriyani : 250 ,"+"gst 10% : 25 ,"
                  "total : 275")
                amount = 275
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")
                    
            elif c == "kaju biriyani" or "kaju":
                print("kaju biriyani : 300 ,"+"gst 10% : 30 ,"
                  "total : 330")
                amount = 330
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")
                    

    elif b == "non-veg":
         e = input("starters/biriyani")
         
         if e == "starters":
            print("list of items")
            starters = ["egg manchurian","chilli chicken","chicken manchurian"]
            print(starters)
            d = input("choose your stater")
            if  e == "starters":
                print("list of items")
            starters = ["veg manchurian","gobi manchurian","mini pizza"]
            print(starters)
            d = input("choose your starter")

            if d == "egg manchurian":
                print("egg manchurian : 150,"+"gst 10% : 15,"
                      "total : 165")
                amount = 165
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif d == "chilli chicken":
                print("chilli chicken : 190,"+"gst 10% : 19,"
                      "total : 209")
                amount = 209
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif d == "chicken manchurian":
                print("chicken manchurian : 240,"+"gst 10% : 24,"
                      "total : 264")
                amount = 264
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

         elif e == "biriyani":
            print("list of items")
            print("[egg biriyani      :220]")
            print("[chicken biriyani  :250]")
            print("[mutton biriyani   :320]")
            c = input("i want :")
            
            if c == "egg biriyani" or "egg": 
                print("egg biriyani : 220 ,"+"gst 10% : 22 ,"
                  "total : 242")
                amount = 242
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif c == "chicken biriyani" or "chicken":
                print("chicken biriyani : 250 ,"+"gst 10% : 25 ,"
                  "total : 275")
                amount = 275
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

            elif c == "mutton biriyani" or "mutton":
                print("mutton biriyani : 320 ,"+"gst 10% : 32 ,"
                  "total : 352")
                amount = 352
                v = input("cash/card")

                if v == "cash":
                    z = int(input("give amount"))
                    x = str(z-amount)
                    if z>amount:
                        print("remaining change : " + x)
                        print("thank you" + " visit again")
                    else:
                        print("please check the cost")
                else:
                    s = input("enter pin")
                    if len(s)==4:
                        print("transaction success")
                        print("thank you , visit again")
                    else:
                        print("enter correct pin,please try again")

elif a == "no":
    print("food ready sir")

else:
    print("give valid input")
    
    
    




