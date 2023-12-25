from scheduling import Offer, find_optimal_schedule
from from_chatgpt import find_maximal_sum_subset

offers = [
    Offer(1, 7, 20),
    Offer(2, 4, 20),
    Offer(3, 6, 40),
    Offer(5, 7, 40),
    Offer(4, 8, 40),
    Offer(6, 9, 50),
    Offer(8, 9, 20)]

price, not_accepted_offers, accepted_offers = find_optimal_schedule(offers)

print('Best price is {0}'.format(price))

print('\nAccepted offers are:')
for accepted_offer in accepted_offers:
    print(accepted_offer)

print('\nNot accepted offers are:')
for not_accepted_offer in not_accepted_offers:
    print(not_accepted_offer)

# Check ChatGPT's answer
set(accepted_offers) == set(find_maximal_sum_subset(offers))
