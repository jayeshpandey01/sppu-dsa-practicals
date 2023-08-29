'''
Write a python program to store 12th class percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using bucket sort 
and display top five scores.
'''

def bucket_sort(arr):
    # create buckets
    num_buckets = len(arr)
    min_value = min(arr)
    max_value = max(arr)
    range_buckets = (max_value - min_value) / num_buckets
    buckets = [[] for _ in range(num_buckets)]

    # distribute elements into buckets
    for num in arr:
        index = int((num - min_value) / range_buckets)
        if index >= num_buckets:
            index = num_buckets - 1
        buckets[index].append(num)

    # sort elements within buckets and concatenate the result
    sorted_arr = []
    for i in range(num_buckets):
        buckets[i].sort()
        sorted_arr += buckets[i]

    return sorted_arr


# store 12th class percentage of students in an array
percentages = [85.5, 92.3, 89.2, 77.8, 95.1, 81.2, 83.7, 87.6, 90.4, 93.8, 79.5, 88.9]

# sort the array using bucket sort
sorted_percentages = bucket_sort(percentages)

# display top five scores
top_five_scores = sorted_percentages[-5:]
print("Top five scores:", top_five_scores)
