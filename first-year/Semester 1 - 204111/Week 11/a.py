
def last_one(name_list: list[str], rhyme_len: int = 4) -> str:
    # Concatenate names into a single string and keep track of the cumulative lengths
    concatenated_names = ''.join(name_list)
    cumulative_lengths = [0] + [len(name) for name in name_list]
    
    # Update cumulative lengths to reflect start positions of names in the concatenated string
    for i in range(1, len(cumulative_lengths)):
        cumulative_lengths[i] += cumulative_lengths[i - 1]

    # Initial index in the concatenated string
    index = rhyme_len - 1
    
    while len(name_list) > 1:
        # Wrap index if it exceeds the length of the concatenated string
        index %= len(concatenated_names)
        
        # Find the name associated with the current index
        for i, start in enumerate(cumulative_lengths[:-1]):
            end = cumulative_lengths[i + 1]
            if start <= index < end:
                # Remove the name and replace its segment with underscores
                name_list.pop(i)
                concatenated_names = concatenated_names[:start] + '_' * (end - start) + concatenated_names[end:]
                cumulative_lengths = [length for length in cumulative_lengths if length != end]
                cumulative_lengths = [start + (length - start) for start in cumulative_lengths]
                break
        else:
            # Replace current index character with '_'
            concatenated_names = concatenated_names[:index] + '_' + concatenated_names[index + 1:]

        # Move to the next index based on `rhyme_len`
        index = (index + rhyme_len - 1) % len(concatenated_names)

    return name_list[0]

# Test the function
assert last_one(['John', 'Ann', 'Tom'], 5) == 'Tom'
