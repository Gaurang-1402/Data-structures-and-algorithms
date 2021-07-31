def minRewards(scores):
    # Write your code here.
    rewards = []
    i=0

    while i < len(scores):
        curr_score = scores[i]
        if curr_score == scores[-1] and curr_score < scores[i-1]:
            rewards.append(1)
            print('whippe')
            i+=1
            continue
        elif curr_score == scores[-1] and curr_score > scores[i-1]:
            rewards.append(rewards_minima + 1)
            print('whoppe')
            i+=1

            continue

        rewards_maxima = 1

        while (i+1 < len(scores)) and scores[i + 1] < scores[i]:
            rewards_maxima += 1
            i += 1

        while rewards_maxima > 0:
            if rewards_maxima == 2:
                print(i)

            rewards.append(rewards_maxima)
            rewards_maxima -= 1

        rewards_maxima = 1

        i+=1


        rewards_minima = rewards_maxima + 1

        while (i+1 < len(scores)) and scores[i + 1] > scores[i]:
            print("i is " + str(scores[i]) + " " + str(i)+ " i+1 item is " + str(scores[i+1]))
            rewards.append(rewards_minima)
            rewards_minima += 1
            i += 1




    print(rewards)



    return sum(rewards)


out = minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])

print(out)
