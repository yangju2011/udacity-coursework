def popularity (t,p):# p is a person
    if t == 0:
        return 1
    else:
        score = 0
        for f in friend(p):
            score = score + popularity (t-1,p)
        return score
