from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    result = []
    
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])
    
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])
    
    return result

if name == "main":
    list1 = list(map(int, input("Enter first list (space-separated): ").split()))
    list2 = list(map(int, input("Enter second list (space-separated): ").split()))
    print("Uncommon elements:", uncommon_elements(list1, list2))