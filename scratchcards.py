with open("scratchcardsinput.txt") as f:
    
    # all_points = 0
    for line in f:
        card_points = 0
        card, nums = [x for x in line.split(": ")]
        y = [x for x in nums.split(" | ")]
        played_nums = [int(x) for x in y[0].split()]
        winning_nums = [int(x) for x in y[1].split()]
        multiplier = 1
        for x in played_nums:
            if x in winning_nums:
                '''
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
                '''
                pass
        # all_points += card_points
    # print(all_points)