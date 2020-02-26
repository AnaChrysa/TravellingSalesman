numba.njit
def simplify(path):
  path=path[::-1]
  del path[0]
  m=-path.index(1)
  path=path[::-1]
  lesandwich=[]
  while m<0:
    lesandwich.append(path.pop(m))
    m+=1 
  if lesandwich[0]>lesandwich[-1]:
    lesandwich=lesandwich[::-1]
  i=1
  while i<(len(path)-1):
    if path[i+1]>lesandwich[0]:
      break
    else:
      i+=(path[i+1:].index(1)+1)
  path=path[0:i]+[1]+lesandwich+path[i:]
  return path
