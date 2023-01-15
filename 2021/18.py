import utils


def reduce_snailfish(full_pair_str, debug=False):
    new_full_pair_str = full_pair_str
    nest_lvl = 0
    explode_left = explode_right = None
    last_seen_value = None
    operated = False
    if debug:
        print(new_full_pair_str)
    for i, ch in enumerate(new_full_pair_str):
        if ch == "[":
            nest_lvl += 1
            if nest_lvl >= 5:
                j = new_full_pair_str.index("]", i)
                explode_left, explode_right = explode(new_full_pair_str, i, j)
                new_full_pair_str = f"{new_full_pair_str[:i]}0{new_full_pair_str[j+1:]}"
                next_value, next_indices = get_next_value(new_full_pair_str, i + 1)
                last_value, last_indices = get_last_value(new_full_pair_str, i - 1)
                if next_value is not None:
                    new_full_pair_str = replace_value(
                        new_full_pair_str, next_indices, next_value + explode_right
                    )
                if last_value is not None:
                    new_full_pair_str = replace_value(
                        new_full_pair_str, last_indices, last_value + explode_left
                    )
                nest_lvl -= 1
                operated = True
                if debug:
                    print(f"EXPLODED [{explode_left},{explode_right}]!")
                break
        if ch == "]":
            nest_lvl -= 1
        if ch == ",":
            continue
    if not operated:
        for i, ch in enumerate(new_full_pair_str):
            if next_value_index := get_next_value(new_full_pair_str, i):
                value, indices = next_value_index
                if value is not None and value >= 10:
                    # split
                    new_pair = f"[{value//2},{value//2+value%2}]"
                    new_full_pair_str = replace_value(
                        new_full_pair_str, indices, new_pair
                    )
                    operated = True
                    if debug:
                        print(f"SPLIT {value}!")
                    break
    if operated:
        return reduce_snailfish(new_full_pair_str, debug=debug)
    return new_full_pair_str


def explode(full_pair_str, pair_start, pair_end):
    return map(int, full_pair_str[pair_start + 1 : pair_end].split(",", maxsplit=1))


def get_next_value(full_pair_str, idx):
    # Get first numeric value starting at idx, returns it and its start and end indices
    # If none exists, returns None, None
    remaining_str = full_pair_str[idx:]
    value = ""
    for j, ch in enumerate(remaining_str):
        if ch.isdigit():
            k = j
            while remaining_str[k].isdigit():
                value += remaining_str[k]
                k += 1
            return int(value), (idx + j, idx + k)
    return None, None


def get_last_value(full_pair_str, idx):
    # Get last numeric value up to index idx, returns it and its index and its end index
    # If none exists, returns None, None
    value = ""
    for j in range(idx, -1, -1):
        ch = full_pair_str[j]
        if ch.isdigit():
            k = j
            while full_pair_str[k].isdigit():
                value = full_pair_str[k] + value
                k -= 1
            return (
                int(value),
                (k + 1, j + 1),
            )
    return None, None


def replace_value(full_pair_str, idx, new_value):
    # Remove numeric value starting at idx, replaces it with new_value
    new_str = f"{full_pair_str[: idx[0]]}{new_value}{full_pair_str[idx[1] :]}"
    return new_str


def calc_magnitude(value):
    if isinstance(value, int):
        return value
    return 3 * calc_magnitude(value[0]) + 2 * calc_magnitude(value[1])

fff=open("input.txt", "r")
aaa=fff.readline()
xxx=""
while aaa!="":
    xxx+=aaa
    aaa=fff.readline()






input_data = xxx.strip().split("\n")

# Part 1:
reduced = input_data[0]
for row in input_data[1:]:
    pair_sum = f"[{reduced},{row}]"
    reduced = reduce_snailfish(pair_sum, debug=False)
print(calc_magnitude(eval(reduced)))

# Part 2:
reduced_rows = [
    reduce_snailfish(f"[{row_i},{row_j}]", debug=False)
    for row_i in input_data
    for row_j in input_data
    if row_i != row_j
]
magnitudes = [calc_magnitude(eval(reduced)) for reduced in reduced_rows]
print(max(magnitudes))
