'''x= ("CSTE", "EEE", "ICE")
print(type(x), x)
Y= 36.36
print(x ,Y)
Z= True
M= False
print(Z,M,M,M,M)
x=35
p=55
print(f"My age is {x} & her age is {p} ")

list= [2,5,60,90]
b=bytearray(list)
print(b[3])
x= ["Dell","Samsung", "Hp"]
x[2]= "Asus"
x[0]= "Mac"
print(x)
print(type(x))

import math
x= range(1000)
for i in x:
    print(math.factorial(i))






x=90
d=4

x,d=d,x
x+=3
print("The new value is ", x)






y= input("Enter your email: ")
x= input("Enter your password:")

print(y,x)

x=90.09
print(str(x))

x=[42,2,'Russel',"Alexander"]
x.append(78)
x.insert(5,52)
x.pop(0)
x.clear()
x.insert(0,"lollipop")
print(x)




x=[42,2,'Russel',25,"Alexander"]
i=0
while i< len(x):
    print (x[i])
    i=i+1





x=[42,2,'Russel',"Alexander"]
i=0
x.insert(2,"Meem")
while i< len(x):
    print (x[i])
    i+=1




x=[42,2,20,1.25,3.1416]
x.sort(reverse=True)
print(x)
y=x.copy()
y.sort()
print(y)
x.extend(y)
print(x)



x=[42,2,20,1.25,47,3.1416]
print(x[2:5])
for i in x:
    print(i)




x= [[2,5,3,4],
    [6,9],
    [2,"Cancer", "Typhoid"]]
print(x[2][1])






x=(4,2,1,2,"Mountain","Regret","Depression","Frustration","Sadness")
y=list(x)
y.insert(4,"Hope");
y[9]=45
x=tuple(y)
*a,b,c,d,e= x


'''
#
# x= "And there were none."
# i=0
# while i<1000:
#     print(x)
#     i+=1


#
# x={"GOT":{
#     "Year":2024,
#     "Rating": 5,
#     "Length": "Long"
# },
#     "Peaky Blinders":{
#     "Year":2021,
#     "Rating": 5,
#     "Length": "Long"
# },
#         "GOT":{
#
#     "Year":2024,
#     "Rating": 4,
#     "Length": "Long"
# },
#             "Forest Gump":{
#
#     "Year":2020,
#     "Rating": 5,
#     "Length": "Short"
# }            }
# x.update({"GOT":{"Year":2024,
#     "Rating": 4.5,
#     "Length": "Long"}})
# x.pop("Forest Gump")
# for a in x.items():
#     print(a)
# # a=x.get("Money Heist")
# # print(a)
# # # print(x["Peaky Blinders"]["Rating"])




# def ist(a,b):
#     x=a/b
#     print(x)
# ist(22,7)
#
# import math
# print(math.tan(math.pi/2))



# for x in range(100):
#     print(x)
#     if x==11:
#         continue
#
#
# def re(a,b):
#     ans=a**b
#     print(ans)
#     re(2,3)
#
# re(2,3)
#

#
#
# variables=["magnitude","angle","direction","True/False?"]
# ans=[21.20,"30 degree west with north","west","True"]
# print(list(zip(variables,ans)))
#

# a=lambda x,y: x**y
# print(a(10,2),a(5,1), a(5,3))





#
# class EEE:          #class
#     Batch="16th"
#     ID= "MUH2117031M"
#     Hometown=""
#     Semester="5"
# Istihad= EEE()     #These 4 items are objects
# Anik= EEE()
# Shaon= EEE()
# Rasel= EEE()
# Istihad.ID= 31
# Rasel.ID=2
# Istihad.Hometown="Cumilla"
#
#
# class ACCE(EEE):
#     Age=25
#     Marital_Status="Unmarried"
# Rabbi=ACCE()
#
# class SWE(ACCE):
#     Internship_Result="4.0"
# Maruf=SWE()
# Mission= SWE()
# x=SWE()
# print(Mission.Batch)
# print(Maruf.Age)
# print(Rabbi.ID)
# print(Istihad.Hometown)
# print(Istihad.ID)







#Python Iterator
# x=[10,25,"Mymensingh","Thailand"]
# y=iter(x)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
#







#
# a,b=10,58   #global variable
# def vombol():
#     x=587         #local variable
#     global b
#     b=33
#     print(x,b)
# vombol()
# print(b)










#
#
# from math import factorial
# import datetime
# x=factorial(5)
# print(x)
# print(datetime.datetime.now())




#
# print(5**3)





#
# import re
# x="Once upon a time there lived a ghost!"
# a= re.findall("[a-e]",x)
# print(a)
#

# import re
# y="Alexander became legendary as a classical hero in the mould of Achilles, featuring prominently in the historical and mythical traditions of both Greek and non-Greek cultures. His military achievements and unprecedented enduring successes in battle made him the measure against which many later military leaders would compare themselves,[f] and his tactics remain a significant subject of study in military academies worldwide.[7] Legends of Alexander's exploits coalesced into the third-century Alexander Romance which, in the premodern period, went through over one hundred recensions, translations, and derivations and was translated into almost every European vernacular and every language of the Islamic world.[8] After the Bible, it was the most popular form of European literature."
# z= re.findall("as",y)
# if z:
#     print("Match found")
# else:
#     print("No match")
# try:
#     print("hoo")
# except:
#        print("Hello")
#


#
# import os
# os.rmdir("")



#
# import One



#normal function
# class YouTube:
#     def Insta(self,Name,ID,BG):
#         print(f"{Name} \n ID: {ID} \n Blood Group: {BG} \n")
# x=YouTube()
# x.Insta("Istihad","MUH2117031M","A+")
# x.Insta("Badhan", "MUH2117017M","B+")
# x.Insta("Fahim","MUH2117028M","A-")
#



#constructor
# class YouTube:
#     def __init__(self,Name,ID,BG):
#         print(f"{Name} \n ID: {ID} \n Blood Group: {BG} \n")
#
# x=YouTube("Istihad","MUH2117031M","A+")
# x=YouTube("Badhan", "MUH2117017M","B+")
# x=YouTube("Fahim","MUH2117028M","A-")



#
# import math
# from math import factorial
#
# x=factorial(5)
#
# class Bench():
#     @classmethod
#     def XYZ(cls):
#         print(x)
#     @staticmethod
#     def Sheela():
#         pi=math.pi
#         print(pi)
# Bench.XYZ()
# Bench.Sheela()
#



#
#
# class vehicle():
#     def __init__(self,Brand,Model,Price):
#         self.Brand=Brand
#         self.Model=Model
#         self.Price=Price
# class Car(vehicle):
#     pass
# class Bike(vehicle):
#     pass
# x= Car("Rolls-Royce","Phantom","50M")
# y= Car("Range Rover","Land Rover","2M")
# z= Bike("Royal Enfield  ","Hunter 350  ","  56k")
# print(x.Price)
# print(z.Brand)
# print(y.Brand,y.Model,y.Price)



#merge pdf
# from PyPDF2 import PdfMerger
# import os
#
# pdf_files = [r"C:\Users\DELL\OneDrive\Desktop\DL\Current Bill.pdf", r"C:\Users\DELL\OneDrive\Desktop\DL\Driving licence medical.pdf"]
# output_file = r"D:\Assignment\Merge.pdf"
#
# x = PdfMerger()
#
# for pdf in pdf_files:
#         x.append(pdf)
#
# x.write(output_file)
# x.close()
#







#
# import random
# x= random.randrange(1,10)
# ip= int(input("Guess a number btn 1 to 10- "))
# if x==ip:
#         print("GOD! You guessed Correctly")
# else:
#      print(f"Better Luck Next Time.The correct number was {x}")
#
#
#

#
# import random
# x=random.randrange(0,33,2)
# print(x)
#





#Dice Game
# import random
# Dice  = True
# while Dice:
#     x=random.randrange(1,7)
#     print(x)
#     if x==6:
#         print("\n You've Nailed It!")
#         break
#     else:
#         again=input("\n Play Again? [y/n]: ")
#         if again=="y":
#             continue
#         else:
#             break
#


# import time
# from win10toast import ToastNotifier
#
# def show_notification():
#     x = ToastNotifier()
#     x.show_toast("STOP BROWSING", "Istihad! It's time to learn. Come back ASAP.", duration=100)
#
# while True:
#     show_notification()
#     time.sleep(30 * 60)







#
#
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[]
# for i in x:
#     y.append(i**2)
# print(y)



#
# with open('Number.txt', 'r') as file:
#     Number = file.readlines()
#
# x = [str(int(num.strip()) ** 2) + "\n" for num in Number]
#
# with open('op.txt', 'w') as file:
#     file.writelines(x)
#



#
# import pandas as pd
#
# xl= pd.read_excel(r'C:\Users\DELL\OneDrive\Desktop\Book1.xlsx')
#
# columns_to_show = ['Name','Age', 'Sex']
#
# if all(col in xl.columns for col in columns_to_show):
#     print(xl[columns_to_show].head())






#
# import pandas as pd
#
# xl= pd.read_excel(r'C:\Users\DELL\OneDrive\Desktop\Book1.xlsx')
#
# result = ['Name','Age','Sex']
#
# if all(col in xl.columns for col in result):
#     selected_columns= xl[result]
#     selected_columns.to_csv(r'C:\Users\DELL\OneDrive\Desktop\output.csv',index=False)
#     print(f"Output written to 'output.csv'.")






# import pandas as pd
# xl= pd.read_excel(r'C:\Users\DELL\OneDrive\Desktop\Book1.xlsx')
# result = ['Name', 'Age', 'Sex']
# if all(col in xl.columns for col in result):
#     selected_columns= xl[result]
#     selected_columns.to_csv(r'C:\Users\DELL\OneDrive\Desktop\output.csv',index=False)
#     print(f"Output written to 'output_2.csv'.")





pip install scikit-learn


import pandas as pd

# Create a dictionary with the data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [22, 23, 24, 21, 22],
    'GPA': [3.5, 3.7, 3.8, 3.6, 3.9],
    'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany'],
    'Age': [22, 23, 24, 21, 22]  # This is a duplicate of 'Age'
}

# Create a DataFrame
df = pd.DataFrame(data)


# Write the DataFrame to an Excel file
df.to_excel(r'C:\Users\DELL\OneDrive\Desktop\BasicExcelFile.xlsx', index=False)

print("Excel file created successfully!")
