numba.njit
def sneakers(city,path,cities):
  i=1
  while i<(len(path)-1):
    if i!=len(path)-1 and i!=1:
      if city in cities[path[i-1]]or city in cities[path[i+1]]:
        return False
      elif i==1:
           if city in cities[path[2]]:
               return False
      elif i==len(path)-1:
           if city in cities[path[-2]]:
               return False
      i+=(path[i+1:].index(1)+1)
  return True
  
