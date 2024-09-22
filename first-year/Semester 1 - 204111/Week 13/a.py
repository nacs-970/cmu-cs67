def sand_towers(list_a: list[int]) -> str:
    max_height = max(list_a)
    tower_width = max_height // 2
    total_width = len(list_a) * (tower_width + 1) + 1

    # Start building the output
    output = []

    # Top empty line
    output.append(" " * (total_width // 2))

    # Add the flag
    output.append(" " * (total_width // 2) + "|>>~")
    output.append(" " * (total_width // 2) + "|")

    # Construct the towers
    for height in range(max_height, 0, -1):
        line = []
        for h in list_a:
            if h >= height:
                line.append(" " * (tower_width - 1) + "/^^^\\" + " " * (tower_width - 1))
            else:
                line.append(" " * (tower_width) + " " * 5)
        output.append("".join(line))

    # Base line
    base_line = "/:" + ":".join(["/" + ":" * (tower_width * 2) + "\\"] * len(list_a))
    output.append(base_line)

    return "\n".join(output)

# Function call example
print(sand_towers([9, 12, 6]))

