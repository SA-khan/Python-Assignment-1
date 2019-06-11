users = {"SAAD":"Avanza123", "WAQAS":"bafl123","ZAFAR":"Avanza123"}
flag = 0
count = 0;
uid = ""
while count < 3:
    if count == 1:
        print("Attept # 2")
    elif count == 2:
        print("Attept # 3")
    userid = input("Enter User ID: ").upper()
    for x in users:
        if x == userid:
            userpass = input("Enter Password: ")
            if x == userid and users[x] == userpass:
                uid = x
                flag = 1
                count = 3
                break
            else:
                flag = 0
                count += 1
                print("Access Denied. ")
                print("Please Try Again. ")
                break
        else:
            flag = -1
            #count += 1

                    
if flag == 1:
    print("Access Granted! ")
    print("Welcome " + uid)
elif flag == 0 and count == 3:
    print("Account Blocked. ")
elif flag == -1:
    print("Access Denied. ")
    print("Invalid User!")


    
        
            
                
                
                    
                

         


    
