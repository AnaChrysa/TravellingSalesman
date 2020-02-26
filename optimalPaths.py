def optimalPaths(n,a,b):
    mincost=a
    paths=[[]]
    leaves=[]
    L = 8
    paths=[[69+littlegauss(n),1,11,1,13,1,7,14]]
    paths[0][0]-=11+13+7+14
    cities =[0]
    for city in range(1,n+1):
        next=[]
        for x in range(1,n+1):
            if city+x>LCMdict[city][x]:
                next.append(x)
        cities.append(next)
    while len(paths):
        tempPaths=[]
        print(L-1,len(paths))
        newPaths = []
        while len(paths):
            path=paths.pop()
<<<<<<< HEAD:optimalPaths.py
            addcity(path,cities,mincost,n)
=======
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
>>>>>>> parent of cc45d8b... Update optimalPaths:optimalPaths
        for path in tempPaths:
            if path[0]<=mincost:
                if path.count(1)<b:
                    if sos(path,n):
                        mincost=path[0]
                        leaves.append(path)
                    else:
                        newPaths.append(path)
        paths = newPaths
        L += 1
    print('The minimum cost to visit', n,'cities is:', mincost)
    # prune out suboptimal paths from leaves
    leaves = [path for path in leaves if path[0]==mincost]
    for path in leaves:
        path.pop(0)
        print(path)
