#BlackJack_prob

def blackjackProbability(target, startingHand):
    # Write your code here.
    memo={}
    return round(calProb(startingHand,target,memo),3)
def calProb(currentH,target,memo):
    if currentH in memo:
        return memo[currentH]
    if currentH>target:
        return 1
    if  currentH+4>=target:
        return 0
    total=0
    for cards in range (1,11):
        total+= 1/10 * calProb(currentH + cards,target,memo)

    memo[currentH]=total
    return total
