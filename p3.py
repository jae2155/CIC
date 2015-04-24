#######################
# Jane Doe
# jd1234
# Computing in Context Spring '15, Assignment 5
# This script estimates the number of ways there could have been a tie in the
# 2000 presidential elections given some prior information about which states
# were in the bag for each party and which were battleground states.
#######################

from election import est_probs

def main():
    battleground_votes = [6, 3, 25, 22, 7, 4, 18, 10, 11, 4, 4, 7, 23, 11, 11, 5, 11]
    battleground_probs_naive = [.5]*len(battleground_votes)
    battleground_probs_actual = [
        .395, .143, .893, .999,  .42,   .5, .997, .999, .236, 
        .146, .731, .602, .989, .289, .753, .302, .946
    ]
    
    gore_votes = 146
    trials = 1000000

    def print_simulation_results(probs):
        """
        Calculates and prints results of simulating election with given probs

        Parameters:
            probs - a list of probabilities that the democrats will win each state
        """
        dem, tie, rep = est_probs(battleground_votes, trials, probs, gore_votes)
        
        print("\tProbability Gore Wins:\t", dem)
        print("\tProbability of Tie:   \t", tie)
        print("\tProbability Bush Wins:\t", rep)    
    
    print("3.a -- naive probabilities")
    print_simulation_results(battleground_probs_naive)

    print("3.b -- polled probabilities")
    print_simulation_results(battleground_probs_actual)    

main()