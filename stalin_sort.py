import random

# Sorting function
def stalin_sort(arr: list | set, asc: bool = True) -> list | tuple:
    if isinstance(arr, list):
        rtrn = [arr[0],]
    elif isinstance(arr, set):
        rtrn = {arr[0],}
    else:
        raise TypeError("arr is not of type list or set")
    for n in range(len(arr)):
        if asc:
            if arr[n] > rtrn[-1]:
                if isinstance(rtrn, list):
                    rtrn.append(arr[n])
                else:
                    rtrn.add(arr[n])
        else:
            if arr[n] < rtrn[-1]:
                if isinstance(rtrn, list):
                    rtrn.append(arr[n])
                else:
                    rtrn.add(arr[n])
    return rtrn


# Example
if __name__ == "__main__":
    arr = [random.randint(0, 200) for _ in range(50)]
    print(stalin_sort(arr))
    print(stalin_sort(arr, False))