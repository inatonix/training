def binary_search(arr, d, offset=0):
    mid = len(arr) // 2
    print(mid, offset, arr)
    if d == arr[mid]:
        return offset+mid

    if mid == 0:
        print("No Number in this array")
        return None

    l = arr[:mid]
    r = arr[mid:]

    if d < arr[mid]:
        print('left')
        return binary_search(l, d, offset)
    print('right')
    offset += mid
    return binary_search(r, d, offset)

if __name__ == '__main__':
    print(binary_search([2,4,5,5,5,8,10,20,100], 1))