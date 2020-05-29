import json 
with open('C:/Users/USER/Desktop/測試資料/Shortest-Job First/test_3/test_3.json','r') as load_f:
    load_dict=json.load(load_f)


readyqueue=[]
execute = []
for j in range(0,1000): #開始
    for k in list(load_dict.keys()):    
        if load_dict[k]['ArrivalTime'] <= j: #將到達的Process放進ReadyQueue
            readyqueue.append(list(load_dict[k].values()))
            load_dict.pop(k)

    for x in readyqueue: #對ReadyQueue排序
        readyqueue = sorted(readyqueue, key=lambda r: r[2])
    #print(readyqueue)
    
    if readyqueue and execute==[]:
        execute = readyqueue[0]
        del readyqueue[0]
        if execute[2]==0:
            execute = []
    elif readyqueue and execute != []:
        if readyqueue[0][2] < execute[2]:
            print("====================")
            if execute[2] != 0:
                readyqueue.append(execute)
            execute = readyqueue[0]
            del readyqueue[0]
    if execute[2]== 0 and readyqueue:
        print("====================")
        execute=readyqueue[0]
        del readyqueue[0]
     
    if execute[2]>0:
         print ("second "+str(j)+"~"+str(j+1)," process:"+str(execute[0]))
         execute[2] -=1
          