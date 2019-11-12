'''
In this question we'll run through a problem that can be solved with dynamic programming, known as the knapsack problem. 
Suppose you wish to fill a knapsack with items to maximize the total value of the contents of your knapsack. The problem is as follows:

Input: a sequence of n items,  𝑖1,…,𝑖𝑛 .  Each item  𝑖𝑖  has an associated value,  𝑣𝑖 , and a weight,  𝑤𝑖 .  
Additionally, you are given a capacity W.

Output: The total value of a subset of the  𝑛  items,  𝑖𝑠1,𝑖𝑠2,…,𝑖𝑠𝑘  with value  ∑𝑘𝑗=1𝑣𝑠𝑘 , 
such that this total value of items is maximized, while keeping the total weight of these items  ≤  the capacity W.
'''


def knapsack(d={1:{4:12}, 2:{2:1}, 3:{2:2}, 4:{1:1}, 5:{10:4}}, W=15): # dictionary key is unique ID for item, value is dictionary {$pesos:kg}

	dictionary_densities = {}
	# {1: 0.3333333333333333, 2: 2.0, 3: 1.0, 4: 1.0, 5: 2.5} # # dictionary key is unique ID for item, value is density $pesos/kg

	for id_item in d:
		density = [x[0]/x[1] for x in d[id_item].items()] # $pesos/kg
		dictionary_densities[id_item] = density[0]

	list_ordered_densities = sorted(dictionary_densities.items(), key=lambda x: x[1], reverse=True) # dictionary ordered by densities
	# [(5, 2.5), (2, 2.0), (3, 1.0), (4, 1.0), (1, 0.3333333333333333)] ## [(id, density), ...


	total_money = 0
	total_kilogram = 0

	for id_density in list_ordered_densities:
		el_id = id_density[0]
		en_kg = [x for x in d[el_id].values()][0]
		en_pesos = [x for x in d[el_id].keys()][0]
		total_kilogram = total_kilogram + en_kg

		if total_kilogram < W:
			total_money = total_money + en_pesos

	return total_money

if __name__ == "__main__":
    assert knapsack() == 15, "max money, is not 15, sth wrong"
