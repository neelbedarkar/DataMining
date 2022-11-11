from itertools import combinations

data = [['A', 'B', 'C', 'D'],
        ['B', 'E'],
        ['A', 'B', 'C', 'E'],
        ['A', 'B', 'F'],
        ['A', 'C', 'F'],
        ['B', 'C', 'D', 'E'],
        ['A', 'C'],
        ['A', 'B', 'C', 'D', 'E'],
        ['A', 'B', 'F'],
        ['C', 'D']]
# data = [[1, 2, 3], [2, 3, 6], [1, 3, 4], [3, 4, 6],
#         [1, 5, 6], [2, 4, 6], [1, 2, 5], [2, 4, 5],
#         [1, 3, 5], [2, 3, 4], [4, 5, 6], [3, 5, 6]]
min_sup = 0


# General Algorithm:
def level_k_apriori(freq_set, level):
    candidate_set = generate_candidate_sets(freq_set, level)
    # print(candidate_set)
    freq_set_k, counter_set_k = get_freq_set(candidate_set)
    if len(freq_set_k) > 0:
        print("Level", level, "frequent sets and their support ")
        # print(counter_set_k)
        # print(freq_set_k)
        for itemset_k in freq_set_k:
            print(set(itemset_k), ":", counter_set_k[itemset_k])
        level = level + 1
        level_k_apriori(freq_set_k, level)
    else:
        print("No Frequent Item Sets in Level:", level)

def generate_candidate_sets(item_set, length):
    all_possible_values = set()
    for i in item_set:
        for j in item_set:
            if len(i.union(j)) == length:
                all_possible_values.add(i.union(j))
    candidate_set = all_possible_values.copy()
    for each_set in all_possible_values:
        all_combinations = combinations(each_set, length - 1)
        for combination in all_combinations:
            if frozenset(combination) not in item_set:
                candidate_set.remove(each_set)
                break
    return candidate_set


def get_freq_set(candidate_set: set[frozenset]):
    freq_set_k = set()
    counter_set_k = dict()
    for candidate in candidate_set:
        for item_basket_k in data:
            if candidate.issubset(set(item_basket_k)):
                counter_k = counter_set_k.get(candidate, 0)
                counter_k = counter_k + 1
                counter_set_k[candidate] = counter_k
    for item_k in counter_set_k:
        if counter_set_k[item_k] >= min_sup:
            freq_set_k.add(item_k)
    return freq_set_k, counter_set_k


# generate first frequent set. Easier to do this to convert any type of input
all_items = set()
counter_set_1 = dict()
for item_basket in data:
    for item in item_basket:
        all_items.add(item)
        counter = counter_set_1.get(frozenset({item}), 0)
        counter = counter + 1
        counter_set_1[frozenset({item})] = counter

print("All Items in the dataset: ", all_items)
freq_set_1 = set()

for item in counter_set_1:
    if counter_set_1[item] >= min_sup:
        # frozen set because set is not hashable
        freq_set_1.add(frozenset(item))

print("Level 1 frequent sets and their support ")
for itemset in freq_set_1:
    print(set(itemset), ":", counter_set_1[itemset])

level_k_apriori(freq_set_1, 2)
