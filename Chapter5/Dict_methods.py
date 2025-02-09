Marks = {
          "Rohit" : 87,
          "Rohan" : 90,
          "Rahul" : 97,
          0 : "Harry"
}

print(Marks.items())                 #Returns a list in tuple format...

print(Marks.keys())                  #Returns a list containing dictionary's keys...

print(Marks.values())                #Returns a list containing dictionary's values...

Marks.update({"Rohit" : 81})          #Update the existing record...
print(Marks)




