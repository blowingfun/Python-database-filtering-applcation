import csv
    
class avocado:
    def __init__(self,priceaverage,dates,years,amount,types):
        self.average = priceaverage
        self.date = dates
        self.year = years
        self.total_amount = amount
        self.type = types

    def _average(self):
        return self.average

    def _date(self):
        return self.date

    def _year(self):
        return self.year

    def _amount(self):
        return self.total_amount

    def _types(self):
        return self.type
    

class control:

    def __init__(self):
        self.dictionary = {}
   
    def createdictionary(self,user):
        with open ("avocado.csv") as filein:
            reader = csv.DictReader(filein)
            for line in reader:
                tempavocado = avocado(line["AveragePrice"],line["Date"],line["year"],line["Total Volume"],line["type"]) 
                if user == "1":
                    self._avocado_dictionary1(tempavocado)
                else:
                    self._avocado_dictionary2(tempavocado)

    def _avocado_dictionary1(self,newavocado):
        self.dictionary.setdefault(newavocado._year(),[])
        self.dictionary[newavocado._year()].append(newavocado)

    def _avocado_dictionary2(self,newavocado):
        self.dictionary.setdefault(newavocado._types(),[])
        self.dictionary[newavocado._types()].append(newavocado)

    def _dictionary(self):
        return self.dictionary
    
class option1:
    
    def __init__(self,user,dictionary):
        self.user = user
        self.dictionary = dictionary
        self.list1 = []
        self.list2 = []

    def filter1(self):
        for i in self.dictionary:
            if i == self.user:
                self.list1 = self.dictionary[i]
                
    def filter2(self,nowuser):
        for i in self.list1:
            if nowuser == "over 1":
                if float(i._average()) >= 1:
                    self.list2.append(i)
            else:
                if float(i._average()) < 1:
                    self.list2.append(i)         
        return self.list2
                
class option2:

    def __init__(self,user,dictionary):
        self.user = user
        self.dictionary = dictionary
        self.list1 = []
        self.list2 = []
        
    def filter3(self):
        for i in self.dictionary:
            if i == self.user:
                self.list1 = self.dictionary[i]

    def filter4(self,nowuser):
        for i in self.list1:
            if nowuser == "over 100,000":
                if float(i._amount()) >= 100000:
                    self.list2.append(i)
            else:
                if float(i._amount()) < 100000:
                    self.list2.append(i)
        return self.list2
            
            

#main
print("     Black Friday Dataset")
print("*"*30)
print("*PLEASE TYPE YOUR CHOICE EXACTLY AS WRITTEN IN PROVIDED OPTIONS*")
print("OPTION 1 = See all days with their average pricing within a selected year")
print("OPTION 2 = See all days with their total amount of avocados sold, grown either organically or conventionally")
print("Options: '1' , '2'")
User = input("Please enter your number:")
control = control()
control.createdictionary(User)
display = None
if User == "1":
    print("*"*30)
    
    print("Please select what year you would like to look at")
    print("Options: '2015' ,'2016' , '2017' , '2018'")
    temp = option1(input("Please enter your choice: "),control._dictionary())
    temp.filter1()
    print("*"*30)
    print("Select whether you want to see average prices over or exactly 1 dollar or under 1 dollar")
    print("Options: 'over 1' , 'under 1'")
    display = temp.filter2(input("Please enter your choice: "))
    print("*"*30)
    for i in display:
        print (f'Date: {i._date()}   Average: ${i._average()}\n')

elif User == "2":
    print("*"*30)
    print("Please select what type of grown avocados you would like to look at")
    print("Options: 'conventional' , 'organic")
    temp = option2(input("Please enter your choice: "),control._dictionary())
    temp.filter3()
    print("*"*30)
    print("Please select whether you want to see over or exactly 100,000 amount or less than 100,000 amount")
    print("Options: 'over 100,000' , 'under 100,000'")
    display = temp.filter4(input("Please enter your choice: "))
    print("*"*30)
    for i in display:
        print (f'Date: {i._date()}   Amount: {i._amount()}\n')

else:
    print("sorry we dont accept that, please restart the program")
    
    

    
   
    
            

