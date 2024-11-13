def bottom_up_m_sort(list_x: list[int], show_steps: bool = False) -> list[int]:
    if show_steps:
        print(f"Current list: {list_x}")
    
    n = len(list_x)
    if n <= 1:
        return list_x

    # Initialize the list of sorted sublists
    sorted_sublists = [[x] for x in list_x]

    # Merge pairs of sublists until we have one sorted list
    while len(sorted_sublists) > 1:
        tmp = []
        for i in range(0, len(sorted_sublists), 2):
            left = sorted_sublists[i]
            right = sorted_sublists[i + 1] if i + 1 < len(sorted_sublists) else []
            merged = merge(left, right)
            tmp.append(merged)
            if show_steps:
                print(f"Merging {left} and {right} -> {merged}")
        sorted_sublists = tmp

    return sorted_sublists[0]

def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# Example usage
if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = bottom_up_m_sort(sample_list, show_steps=True)
    print(f"Sorted list: {sorted_list}")
