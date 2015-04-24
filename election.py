#######################
# Jane Doe
# jd1234
# Computing in Context Spring '15, Assignment 5
# These are just some handy dandy helper functions
#######################

import random

def election(electoral_votes, probs, dem_votes = 0):
    """
    Simulates a single election.

    Parameters:
        electoral_votes - a list of electoral votes for the election year
        probs - a list of probabilities that the democrats will win each state
        dem_votes - the number of electoral votes the democrats already have

    Returns:
        The number of electoral votes the democrats win in this election
    """
    for num_votes, prob in zip(electoral_votes, probs):
        if random.random() < prob: # Flip a coin for each state
            dem_votes += num_votes
    
    return dem_votes

def est_ties(votes, n, probs):
    """
    Estimates the total number of ways to tie in a given election year

    Parameters:
        votes - a list of electoral votes for the election year
        n - the number of simulations to run 
        probs - a list of probabilities that the democrats will win each state

    Returns: 
        The estimated number of ways there are to tie the election
    """
    num_ties = 0

    for k in range(n): # n elections
        if election(votes,probs) == 269: # tie
            num_ties += 1
    
    total_posibilities = 2**51
    return (num_ties/n)*total_posibilities

def est_probs(votes, n, probs, dem_votes):
    """
    Estimates the probabilities of each party winning the election

    Parameters:
        votes - a list of electoral votes for the election year
        n - the number of simulations to run 
        probs - a list of probabilities that the democrats will win each state
        dem_votes - the number of electoral votes the democrats already have

    Returns:
        dem_prob - the probability that the democrats will win the election
        tie_prob - the probability that the election will result in a tie
        rep_prob - the probability that the republicans will win the election
    """
    dem_wins = 0
    rep_wins = 0
    
    for k in range(n): # n elections
        new_dem_votes = election(votes, probs, dem_votes=dem_votes)
        if new_dem_votes > 269:
            dem_wins += 1
        elif new_dem_votes < 269:
            rep_wins += 1

    dem_prob = dem_wins/n
    rep_prob = rep_wins/n
    tie_prob = 1 - (dem_prob + rep_prob)

    return (dem_prob, tie_prob, rep_prob)





