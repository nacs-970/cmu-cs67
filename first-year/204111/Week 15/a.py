import math

def histogram(scores: tuple[int]) -> None:
    # Create bins
    bins = [0] * 11
    for score in scores:
        if score <= 100:
            bins[score // 10] += 1
            
    # Combine the 90-100 bin
    bins[9] += bins[10]
    bins.pop()  # Remove the last bin (10)

    # Determine maximum height
    max_height = max(bins) if bins else 0
    max_height = math.ceil(max_height / 5) + 2 if max_height else 3

    # Build histogram bars
    histogram_lines = []
    for bin_count in bins:
        bar_height = math.ceil(bin_count / 5)
        bar_lines = [' ' * (6 - len(str(bin_count))) + str(bin_count)]
        
        # Top of the bar
        bar_lines.append(' _____' if bar_height > 0 else '_____')
        
        # Add the star bars
        for h in range(max_height - 1):
            bar_lines.append('|' + '*****' if h < bar_height else ' ' + '*****|')
        
        # Align with max height
        histogram_lines.append([' ' * 6] * (max_height - len(bar_lines)) + bar_lines)

    # Print the histogram
    for level in range(max_height):
        print(''.join(line[level] for line in histogram_lines))

    # Print x-axis
    print('0' + ' ' * 5 + ''.join(f'{i:<4}' for i in range(10, 101, 10)))

# Example usage
histogram((23, 45, 67, 12, 90, 23, 45, 90, 88, 76, 95, 82))
