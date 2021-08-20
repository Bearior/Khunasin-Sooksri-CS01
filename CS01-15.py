def Chang_list(List):
    for i in range(len(List)):
        if List[i] == 20:
            List[i] = 200
    print(List)
thislist = [5,10,15,20,25,50,20]
Chang_list(thislist)
