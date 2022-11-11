from itertools import combinations

data = [[1, 2, 3], [2, 3, 6], [1, 3, 4], [3, 4, 6],
        [1, 5, 6], [2, 4, 6], [1, 2, 5], [2, 4, 5],
        [1, 3, 5], [2, 3, 4], [4, 5, 6], [3, 5, 6]]
min_sup = 0
buckets = 13
all_sets = {}
all_counts = {}

# General Algorithm:
def print_support_k_levels(freq_set, level):
    candidate_set = generate_candidate_sets(freq_set, level)
    set_k, counter_set_k = get_freq_set(candidate_set)
    all_sets[level]  = set_k
    all_counts[level] =  counter_set_k
    if len(set_k) > 0:
        print(str(level) + "-Item sets and their support ")
        for itemset_k in set_k:
            print(set(itemset_k), ":", counter_set_k[itemset_k])
        level = level + 1
        print_support_k_levels(set_k, level)
    else:
        print("No Item Sets in Level:", level)


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
    set_k = set()
    counter_set_k = dict()
    for candidate in candidate_set:
        for item_basket_k in data:
            if candidate.issubset(set(item_basket_k)):
                counter_k = counter_set_k.get(candidate, 0)
                counter_k = counter_k + 1
                counter_set_k[candidate] = counter_k
    for item_k in counter_set_k:
        set_k.add(item_k)
    return set_k, counter_set_k


def custom_hash(list_pair):
    product = 1
    for x in list_pair:
        product = x*product
    return product % buckets


def calculate_buckets(sets_k, counter_k):
    bucket_distribution = dict()
    for item_set in sets_k:
        temp_set = bucket_distribution.get(custom_hash(item_set), list())
        temp_set.append(tuple(item_set))  # Easier to print a tuple than a frozen set
        bucket_distribution[custom_hash(item_set)] = temp_set
    bucket_count = dict()
    for hash_number in bucket_distribution:
        counter_bucket = 0
        for item_set in bucket_distribution[hash_number]:
            counter_bucket = counter_bucket + counter_k[frozenset(item_set)]
        bucket_count[hash_number] = {tuple(bucket_distribution[hash_number]):counter_bucket}
    print(bucket_distribution)
    print(bucket_count)


if __name__ == "__main__":
    all_items = set()
    counter_set_1 = dict()
    # generate first set. Easier to do this to convert any type of input
    for item_basket in data:
        for item in item_basket:
            all_items.add(item)
            counter = counter_set_1.get(frozenset({item}), 0)
            counter = counter + 1
            counter_set_1[frozenset({item})] = counter

    print("All Items in the dataset: ", all_items)
    freq_set_1 = set()
    print("1-Item sets and their support ")
    for itemset in counter_set_1:
        print(set(itemset), ":", counter_set_1[itemset])
    for item in counter_set_1:
        freq_set_1.add(frozenset(item))
    all_sets[1] = freq_set_1
    all_counts[1] =  counter_set_1
    print_support_k_levels(freq_set_1, 2)
    calculate_buckets(all_sets[2], all_counts[2])
