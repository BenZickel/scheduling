def find_maximal_sum_subset(offers):
    # Sort the offers based on end time
    sorted_offers = sorted(offers, key=lambda x: x.end)
    
    # Initialize variables
    n = len(sorted_offers)
    dp = [0] * n  # dp[i] represents the maximal sum of prices for the first i offers
    last_non_overlap = [-1] * n  # last_non_overlap[i] stores the index of the last non-overlapping offer
    
    # Fill the dp and last_non_overlap arrays
    for i in range(n):
        current_price = sorted_offers[i].price
        
        # Find the latest non-overlapping offer
        latest_non_overlap = -1
        for j in range(i - 1, -1, -1):
            if sorted_offers[j].end <= sorted_offers[i].start:
                latest_non_overlap = j
                break
        
        last_non_overlap[i] = latest_non_overlap
        
        # Update dp[i] based on whether including the current offer or not
        if latest_non_overlap != -1:
            dp[i] = max(dp[i - 1], dp[latest_non_overlap] + current_price)
        else:
            dp[i] = max(dp[i - 1], current_price)
    
    # Reconstruct the optimal subset
    optimal_subset = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            optimal_subset.append(sorted_offers[i])
            i = last_non_overlap[i]
        else:
            i -= 1
    
    # Reverse the subset to get the correct order
    optimal_subset.reverse()
    
    return optimal_subset
