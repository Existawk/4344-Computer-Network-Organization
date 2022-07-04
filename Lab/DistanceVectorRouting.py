# Parker Skinner
# ID:1001541467
# 11/21/2021

import numpy as np
import sys
import time
from datetime import datetime

#this function simulates the running network
def NetSim(network):
    print("\nOPTIONS:\n\"send packet\"\n\"exit\"")
    userinput = input()

    #simulation of a packet being sent
    if(userinput=="send packet"):
        print("\nWhat node is the source?")
        src = int(input())
        print("\nWhat node is the destination?")
        dest = int(input())
        
        length = -1
        for i in range(len(network[src])):
            if int(network[src][i][0]) == dest:
                length = network[src][i][1]
        if length == -1:
            print("Route not found")
        else:
            start = time.time()
            print("\nSending Packet at ",datetime.now().time())
            time.sleep(length*.1)
            end = time.time()
            print("\nPacket Recievedat ",datetime.now().time())
            print("\nPacket transmition time: {:f}".format(end-start))
        return True
    
    #exit the simulation
    elif(userinput=="exit"):
        print("\n=====Exiting Simulation=====\n")
        return False

    #invalid user input
    else:
        print("\nInvalid Input")
        return True

# read in data
data = np.loadtxt(sys.argv[1]).tolist()

# create the initial network with data
network = {}
for i in range (len(data)):
    if int(data[i][0]) not in network:
        network[int(data[i][0])] = []
    network[int(data[i][0])].append(data[i][1:])
    if int(data[i][1]) not in network:
        network[int(data[i][1])] = []
    network[int(data[i][1])].append([data[i][0],data[i][2]])

# main run loop
run = True
print("Welcome to the Distance Vector Routing Program!")

while(run):
    print("OPTIONS:\n\"show nodes\"\n\"show network\"\n\"optimize routes\"\n\"simulate network\"\n\"exit\"")
    userinput = input()

    #show all current routers in the network
    if(userinput=="show nodes"):
        print("\n====Current Nodes====")
        for i in range (len(network)):
            print("Node {:d}".format(i+1))
        print("==========\n")

    #show all current connections for each router in the network
    elif(userinput=="show network"):
        print("\n====Current Network====")
        for i in range (len(network)):
            print("Router {:d} Links:".format(i+1))
            for j in range(len(network[i+1])):
                print("Router {:d} to Router {:d} Cost => {:d}".format(i+1,int(network[i+1][j][0]),int(network[i+1][j][1])))
        print("==========\n")

    #optimize current connections and create new connections in the network
    elif(userinput=="optimize routes"):
        print("\n====Optimizing Routes====")
        # for i in range (len(network)):
            
        #     for j in range(len(network[i+1])):
               
        print("==========\n")

    #simulate a package being sent accross the network by giving it a start and endpoint
    elif(userinput=="simulate network"):
        print("\n====Network Simulation====")
        sim = True
        while(sim):
            sim = NetSim(network)

    #exit out of the program
    elif(userinput=="exit"):
        run = False

    #invalid input handler
    else:
        print("Invalid Input\n")