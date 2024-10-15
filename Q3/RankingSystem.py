class College:
    def __init__(self, name, location, fees, ranking):
        self.name = name
        self.location = location
        self.fees = fees
        self.ranking = ranking

def rank_colleges(colleges, preferred_location, max_fees, ranking_weight, fees_weight):
    # Filter colleges based on location and fees
    eligible_colleges = [college for college in colleges 
                         if college.location == preferred_location and college.fees <= max_fees]

    # Calculate score for each eligible college
    ranked_colleges = []
    for college in eligible_colleges:
        score = (college.ranking * ranking_weight) + ((college.fees / max_fees) * fees_weight)
        ranked_colleges.append((college, score))
    
    # Sort colleges by score (lower score is better)
    ranked_colleges.sort(key=lambda x: x[1])
    for college, score in ranked_colleges:
        print(f"Name: {college.name}, Location: {college.location}, Fees: {college.fees}, Ranking: {college.ranking}, Score: {score:.2f}")

colleges = [
    College("College A", "New York", 20000, 1),
    College("College B", "California", 15000, 2),
    College("College C", "New York", 25000, 3),
    College("College D", "New York", 10000, 4)
]

# User preferences
preferred_location = "New York"
max_fees = 20000
ranking_weight = 2
fees_weight = 1
rank_colleges(colleges, preferred_location, max_fees, ranking_weight, fees_weight)



# Time Complexity

# O(nlogn)

# Space Complexity

# O(n)