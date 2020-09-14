from random import choices
ntrials=15000
player1wins = 0
ndice_a=2
ndice_b=3
for i in range(ntrials):
    dice_a=choices(range(1,7),k=ndice_a)
    if dice_a[0]==dice_a[1]:
        continue
    else:
        dice_a_sum =dice_a[0]+dice_a[1]
    dice_b=choices(range(1,7),k=ndice_b)
    dice_b.sort(reverse=True)
    dice_b_sum =dice_b[0]+dice_b[1]
    if dice_b_sum > dice_a_sum:
        player1wins+=1
print("Average roll=",player1wins/ntrials)
