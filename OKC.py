# import csv
import math
import pandas as pd
import os

#Get the path of the script
path = os.getcwd()

#Put the data file in the same path of the script to read data
filename = os.path.join(path,'shots_data.csv')

df = pd.read_csv(filename)

#Create a new lable for classification
zone = []

for i in range(len(df)):
    #For Corner 3 shot zone
    if ((abs(df['x'][i])) > 22.0 and df['y'][i] <= 7.8):
        zone.append("C3")
    #For 2 points between the FT line and baseline
    elif(abs(df['x'][i]) <= 22.0 and df['y'][i] <= math.sqrt((23.75)**2-(22.0)**2)):
        zone.append("2P")
    #For 2 points beyond the FT line to 3 point line
    elif((math.sqrt((df['x'][i])**2 + (df['y'][i])**2)) <= 23.75 and df['y'][i] >= math.sqrt((23.75)**2-(22.0)**2)):
        zone.append("2P")
    #For other 3 points shot zone
    else:
        zone.append("NC3")

#Add the new lable to the data
df["zone"] = zone

#Save the data
df.to_csv(os.path.join(path,'Classification.csv'))

#Create variables for saving the Team A and Team B's data
#Include the number of shot they made, and the totle times they tried
numA = 0
num2P_A = 0
numC3_A = 0
numNC3_A = 0
A_make_2 = 0
A_make_C3 = 0
A_make_NC3 = 0


numB = 0
num2P_B = 0
numC3_B = 0
numNC3_B = 0
B_make_2 = 0
B_make_C3 = 0
B_make_NC3 = 0

for i in range(len(df)):

#Calculate for Team A
    if(df['team'][i] == "Team A"):
        numA += 1
        if(df['zone'][i]=="2P"):
            num2P_A += 1
            if(df['fgmade'][i] == 1):
                A_make_2 += 1
        elif(df['zone'][i] == "C3"):
            numC3_A += 1
            if (df['fgmade'][i] == 1):
                A_make_C3 += 1
        else:
            numNC3_A += 1
            if (df['fgmade'][i] == 1):
                A_make_NC3 += 1


#Calculate for Team B
    elif (df['team'][i] == "Team B"):
        numB += 1
        if (df['zone'][i] == "2P"):
            num2P_B += 1
            if (df['fgmade'][i] == 1):
                B_make_2 += 1
        elif (df['zone'][i] == "C3"):
            numC3_B += 1
            if (df['fgmade'][i] == 1):
                B_make_C3 += 1
        else:
            numNC3_B += 1
            if (df['fgmade'][i] == 1):
                B_make_NC3 += 1

#The result for Team A
A_make_3 = A_make_NC3+A_make_C3
A_2PT = num2P_A/numA
A_C3 = numC3_A/numA
A_NC3 = numNC3_A/numA
eFG_A = (A_make_2+A_make_3 + 0.5*A_make_3)/numA
print("The shot distribution percentage for Team A in 2 point zone is: ",A_2PT)
print("The shot distribution percentage for Team A in Corner 3 point zone is: ",A_C3)
print("The shot distribution percentage for Team A in Non_Corner 3 point zone is: ",A_NC3)
print("The eFG% for Team A is: ",eFG_A)
print("eFG% for Team A in 2 point zone: ",A_make_2/num2P_A)
print("eFG% for Team A in C3 point zone: ",(A_make_C3+0.5*A_make_C3)/numC3_A)
print("eFG% for Team A in NC3 point zone: ",(A_make_NC3+0.5*A_make_NC3)/numNC3_A)



#The result for Team B
B_make_3 = B_make_C3+B_make_NC3
B_2PT = num2P_B/numB
B_C3 = numC3_B/numB
B_NC3 = numNC3_B/numB
eFG_B = (B_make_2+B_make_3 + 0.5*B_make_3)/numB
print("The shot distribution percentage for Team B in 2 point zone is: ",B_2PT)
print("The shot distribution percentage for Team B in Corner 3 point zone is: ",B_C3)
print("The shot distribution percentage for Team B in Non_Corner 3 point zone is: ",B_NC3)
print("The eFG% for Team B is: ",eFG_B)
print("eFG% for Team B in 2 point zone: ",B_make_2/num2P_B)
print("eFG% for Team B in C3 point zone: ",(B_make_C3+0.5*B_make_C3)/numC3_B)
print("eFG% for Team B in NC3 point zone: ",(B_make_NC3+0.5*B_make_NC3)/numNC3_B)

