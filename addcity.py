numba.njit
def addcity(path,cities,mincost,n):
    for city in cities[path[-1]]:
        if city not in path:
            if path[-1]!=1 or sneakers(city,path,cities):
                newPath = path + [city]
                newPath[0] += LCMdict[newPath[-1]][newPath[-2]]
                newPath[0]-=newPath[-1]
                if newPath[0] <= mincost:
                    tempPaths.append(newPath)
                    if sos(newPath,n):
                        mincost = newPath[0]
        elif city==1 and path[-1]!=1:
            newPath = path + [city]
            newPath[0] += newPath[-2]
            newPath=simplify(newPath)
            if not (newPath in tempPaths):
                if newPath[0] <= mincost:
                    tempPaths.append(newPath)
                    if sos(newPath,n):
                        mincost = newPath[0]