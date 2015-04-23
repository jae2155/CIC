import random

#A function to simulate 1 election
def election( votes, probs, dem = 0):
    for k in range(len(votes)):
        #Flip a coin for each state
        if random.random() < probs[k]:
            #Add the votes if the democrats win the state
            dem += votes[k]
    #determining the outcome of the election
    if dem > 269:
        return 1
    if dem < 269:
        return 0
    else:
        return 2

#A function to estimate the total
#number of possible ways to tie
def est_ties(votes,n,probs):
    num_ties = 0
    #simulate n elections
    for k in range(n):
        if election(votes,probs) == 2:
            #if a tie occurs increment num_ties
            num_ties += 1
    #return (%ties)*2^51
    return num_ties/n*2**51

#A function to estimate the probabilities
#of the three possible outcomes of the eletion
def est_percentages(votes,n,probs,gore):
    dem_wins = 0
    ties = 0
    #simulate n election
    for k in range(n):
        result = election(votes,probs,gore)
        #We only need to keep track of ties and democratic wins
        if result == 1:
            dem_wins += 1
        if result == 2:
            ties += 1
    dem_prob = dem_wins/n
    ties_prob = ties/n
    #Prob(rep win) = 1-Prob(dem win) - Prob(tie)
    #I.E. the sum of all probs is 1
    rep_prob = 1-dem_prob-ties_prob
    return dem_prob,ties_prob,rep_prob




