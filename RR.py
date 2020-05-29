import json 
with open('C:/Users/USER/Desktop/testdata_A21E4AD02B443C4908941028B57DCBE4test.json','r') as load_f:
    load_dict=json.load(load_f)

readyqueue=[]
brustTime={}
execute=[]
time=0
Quantum=load_dict['Quantum']
readyqueue=load_dict['Order']
brustTime = load_dict['BurstTime']


for j in range (0,1000):
    
    if readyqueue and execute == []:
        execute=readyqueue[0]
        del readyqueue[0]
        if brustTime[execute] == 0:
            execute = []
            time = 0
    elif brustTime[execute] == 0 and readyqueue:
        print("====================")
        execute = readyqueue[0]
        del readyqueue[0]
        time = 0
    elif readyqueue and execute != []:
        if time==Quantum:
            print("====================")
            readyqueue.append(execute)
            execute = readyqueue[0]
            del readyqueue[0]
            time=0
    

    if brustTime[execute]>0 and time<Quantum:
       print ("second "+str(j)+"~"+str(j+1)," process ",execute) 
       brustTime[execute]=brustTime[execute]-1
       time=time+1

    if readyqueue==[] and execute == []:
        break