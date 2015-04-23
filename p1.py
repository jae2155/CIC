from election import est_ties

votes_2000 = [  9,  3,  8,  6, 54,  8,  8,  3,  3, 25, 13,  4,  4, 22,
12,  7,  6,  8,  9,  4,10, 12, 18, 10,  7, 11,  3,  5,  4,
4, 15,  5, 33, 14,  3, 21,  8,  7, 23,  4, 8,  3, 11, 32,
5,  3, 13, 11,  5, 11,3 ]

votes_2004 = [  9, 3, 10, 6,  55, 9,  7,  3,  3,  27,
       15, 4,  4,21,  11, 7,  6,  8,  9,   4,
       10, 12,17, 10,  6, 11, 3,  5,  5,   4,
       15, 5, 31, 15,  3, 20, 7,  7, 21,   4,
        8, 3, 11, 34,  5,  3, 13, 11, 5,  10,
        3]

votes_2012 = [9,3,11,6,55,9,7,3,3,29,16,4,4,20,11,6,6,8,8,4,10,11,
          16,10,6,10,3,5,6,4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3
          ,13,12,5,10,3]

trials = 1000000
probs = [.5 for k in range(len(votes_2000))]
print("Number of ways to tie in 2000: " ,est_ties(votes_2000,trials,probs))
print("Number of ways to tie in 2004/2008: " ,est_ties(votes_2004,trials,probs))
print("Number of ways to tie in 2012: " ,est_ties(votes_2012,trials,probs))