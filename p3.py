from election import est_percentages

trials = 1000000

b_ground_votes = [6,3,25,22,7,4,18,10,11,4,4,7,23,11,11,5,11]
b_ground_probs_actual = [.395,.143,.893,.999,.42,.5,.997,.999,.236,.146,.731,.602,.989,.289,.753,.302,.946]
b_ground_probs_naive = [.5 for k in range(len(b_ground_votes))]

gore = 146

dem,ties,rep = est_percentages(b_ground_votes,trials,b_ground_probs_naive,gore)
print("3.a")
print("Probability Gore Wins: ",dem)
print("Probability of Tie: ",ties)
print("Probability Bush Wins: ",rep)

dem,ties,rep = est_percentages(b_ground_votes,trials,b_ground_probs_actual,gore)
print("3.b")
print("Probability Gore Wins: ",dem)
print("Probability of Tie: ",ties)
print("Probability Bush Wins: ",rep)
