from address import number

num = number()
try:
    ip_address = input("Enter address: ")
    print(num.getAddress(int(ip_address)))
    for x in ip_address:
        print(x)
except:
    print("Your address is invalid")
else:
    print("everything is okay!")
finally:
    print("The final block")

                                                                                                                                                                                                                                                                                                                                                

    
    