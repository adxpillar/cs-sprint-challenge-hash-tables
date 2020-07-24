def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    for array in arrays:
        for i in array:
            if i not in cache:
                cache[i] = 1
            else:
                if cache[i] < 2:
                    result.append(i)
                cache[i] += 1
    return result 
   

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
