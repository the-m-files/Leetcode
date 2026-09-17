def longest_common_pre(words):
    master_list = [tuple(word) for word in words]

    total_prefix = list(master_list[0])
    del master_list[0]
    for word in master_list:
        total_prefix = str(list(word).intersection())
        print(word)

    return total_prefix



test1 = ["Hello", "Card", "Smart"]
print(longest_common_pre(test1))
