

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True

    rotated = arr2[:]

    for _ in range(len(arr1)):

        element = arr2.pop(len(arr2) - 1)
        arr2.insert(0, element)

        if arr1 == arr2:
            return True
    return False


# test_cases = [
#     ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], True),
#     ([1, 2, 3, 4], [1, 2, 3, 4], True),
#     ([1, 2, 3, 4], [4, 1, 2, 3], True),
#     ([1, 2, 3, 4], [2, 1, 4, 3], False),
#     ([1, 2, 3], [1, 2], False),
#     ([], [], True),
#     ([7], [7], True),
#     ([7], [8], False),
#     ([1, 1, 2], [1, 2, 1], True),
#     ([1, 1, 2], [1, 2, 2], False),
#     ([1, 2, 1, 2], [2, 1, 2, 1], True),
#     ([1, 2, 3, 4], [2, 1, 4, 3], False)
# ]

# for arr1, arr2, expected in test_cases:
#     result = array_rotation_detector(arr1, arr2)
#     print(
#         f"{'PASS' if result == expected else 'FAIL'}: "
#         f"{arr1} -> {arr2} | "
#         f"expected={expected}, got={result}"
#     )
