import math

def euclidean_distance(x, y) :
   distance = math.sqrt(sum([(a-b)**2 for a, b in zip(x, y)]))
   return distance

def manhattan_distance(x, y) :
   distance = sum(abs(a-b) for a, b in zip(x, y))
   return distance

if __name__ == "__main__" :
   x = eval(input("input x : "))
   y = eval(input("input y : "))

   print("euclidean distance: ", euclidean_distance(x, y))
   print("manhattan distance: ", manhattan_distance(x, y))
   
