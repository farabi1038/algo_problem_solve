#best_seat)findsing_conema

def bestSeat(seats):
    leftIdx=0
    max_space=0
    best_seat=-1

    while leftIdx< (len(seats)):
            rightIdx= leftIdx+1
            while rightIdx<len(seats) and seats[rightIdx]==0:
                rightIdx+=1
   
            available=rightIdx-leftIdx-1
            if available>max_space:
                    best_seat= (leftIdx+rightIdx)//2
                    max_space=available
   
            leftIdx=rightIdx
   
           
           
           
               
               
               
    return best_seat