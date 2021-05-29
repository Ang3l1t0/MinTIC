list_ = [('Vaibhhav',86), ('Manav',86) , ('Rajesh',88) , ('Sam',86), ('Richie',89)]

#sort by second element of tuple
pos = 1
list_length = len(list_)

for i in range(0, list_length):
    for j in range(0, list_length-i-1):  
        if (list_[j][pos] < list_[j + 1][pos]):  
            temp = list_[j]  
            list_[j]= list_[j + 1]  
            list_[j + 1]= temp  

print(list_)