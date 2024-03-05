#sunset view 

def sunsetViews(buildings, direction):
    # Write your code here.
    stack=[]
    maxH=0
    candidateBuildings=[]
    startIdx= 0 if direction == "EAST" else len(buildings)-1
    step = 1 if direction == "EAST" else -1 
    idx =startIdx
    while idx>=0 and idx<len(buildings):
        maxH=buildings[idx]

        while len(candidateBuildings)>0 and buildings[candidateBuildings[-1]]<=maxH:
            candidateBuildings.pop()
        
        candidateBuildings.append(idx) 
        idx+=step
    if direction=="WEST":
        return candidateBuildings[::-1]
    return candidateBuildings