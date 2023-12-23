class Offer():
    def __init__(self, start, end, price):
        self.start, self.end, self.price = start, end, price

    def is_overlapping(self, other):
        return other.start < self.end and other.end > self.start
    
    def __repr__(self):
        return 'Start={0}, End={1}, Price={2}'.format(self.start, self.end, self.price)
        
def find_optimal_schedule(offers, accepted_offers = []):
    results = [(0, offers, accepted_offers)]
    for i, offer in enumerate(offers):
        if all([not offer.is_overlapping((accepted_offer))
                    for accepted_offer in accepted_offers]):
            new_accepted_offers = list(accepted_offers) + [offer]
            new_offers = offers[:i] + offers[(i + 1):]
            new_total_price, new_offers, new_accepted_offers = \
                find_optimal_schedule(new_offers, new_accepted_offers)
            new_total_price += offer.price
            results.append((new_total_price, new_offers, new_accepted_offers))
    return max(results, key = lambda x: x[0])
