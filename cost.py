def cost(cities): 
  c = 0
  i = 1
  while i < len(cities) - 1:
    c += LCMdict[cities[i]][cities[i+1]]
    i += 1
  return c
