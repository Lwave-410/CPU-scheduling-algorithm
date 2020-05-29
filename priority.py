import json 
with open('C:/Users/USER/Desktop/測試資料/priority/t1/test1.json','r') as load_f:
    load_dict=json.load(load_f)

readyqueue=[]
execute = []
for j in range(0,10000): #開始
    for k in list(load_dict.keys()):    
        if load_dict[k]['ArrivalTime'] <= j: #將到達的Process放進ReadyQueue
            readyqueue.append(list(load_dict[k].values()))
            load_dict.pop(k)

    for x in readyqueue: #對ReadyQueue排序
        readyqueue = sorted(readyqueue, key=lambda r: r[2])#priority

        #--------------------------------------#
        # 如果readyqueue裡的process可被執行 就放到 execute裡面
        if readyqueue and execute==[]:
            execute = readyqueue[0]
            del readyqueue[0]
            if execute[1]==0:#brusttime
                execute = []
        elif readyqueue and execute != []:
            if readyqueue[0][2] < execute[2]:#priority
                print('====================')
                if execute[1]!=0:#brusttime
                    readyqueue.append(execute)
                execute = readyqueue[0]
                del readyqueue[0]
        #如果被執行的process結束了 就換下一個process執行        
        if execute[1]==0:#brusttime
            print('====================')
            execute=readyqueue[0]
            del readyqueue[0]
        #--------------------------------------#

    #執行execute process
    if execute[1]>0:#brusttime
        print ("second "+str(j)+"~"+str(j+1)," process p"+str(execute[0]))
        execute[1] -=1