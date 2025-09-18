list_tesk = []
#اینجا یه حلقه بینهایت تعریف کردم
while True: 
    #از کاربر خواستم برنامه شو وارد کنه 
    add_tesk = input("mikhaye barnameh emruz vard kony?: y or n: ")
    
    if add_tesk == "y":
        input_task = input("barnameh emruz vard kon: ")
        list_tesk.append(input_task)   
        print(list_tesk)
    #اینجا خواستم اگه خواست میتونه برنامشو حذف کنه
    elif add_tesk == "n":
        remove_tesk = input("mikhaye barnameh ro hazf kony?: y or n: ")
        if remove_tesk == "y":
            item = input("kodomo mikhaye hazf kony? ")
            if item in list_tesk:
                list_tesk.remove(item)
                print("hazf shod")
        #اینجا خواست میتونه برنامشو ببینه
        elif remove_tesk == "n":       
            show_teske = input("mikhaye barname bebini?: y or n: ")
            if show_teske == "y":
                print(list_tesk)
    # اینجام حلقه میشکنه و دوباره اجرا میشه
    else:
        break
