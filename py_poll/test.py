candidates = ['Clooney','Kahn','Kletter','Kletter','Kletter','Kletter','Clooney','Poch','Poch','Kahn','Kletter']

winner = max(set(candidates), key=candidates.count)
total_votes = candidates.count(winner)

print(f'The winner is {winner} with {total_votes} votes')
