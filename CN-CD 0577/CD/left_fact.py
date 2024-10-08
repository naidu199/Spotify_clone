from itertools import takewhile

def groupby(ls):
    """Group rules by their starting character."""
    d = {}
    for rule in ls:
        if rule[0] not in d:
            d[rule[0]] = []
        d[rule[0]].append(rule)
    return d

def prefix(x):
    """Check if all elements in x are the same."""
    return len(set(x)) == 1

def left_factoring(s):
    """Perform left factoring on the given grammar."""
    alphabetset = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
        "X", "Y", "Z"
    ]

    # Clean up the input string
    s = s.replace(" ", "").replace("\t", "").replace("\n", "")

    split = s.split("->")
    starting = split[0]
    rules = split[1].split("|")

    # Logic for taking commons out
    group = groupby(rules)
    for char, rules_list in group.items():
        common_prefix = ''.join([l[0] for l in takewhile(prefix, zip(*rules_list))])

        # Create a new rule for the common prefix
        if common_prefix:
            new_non_terminal = alphabetset.pop(0)
            print(f"{starting}->{common_prefix}{new_non_terminal}")
           
            # Create rules for the remaining suffixes
            suffixes = [rule[len(common_prefix):] for rule in rules_list]
            print(f"{new_non_terminal}->", end="")
            for suffix in suffixes[:-1]:
                if suffix == "":
                    print("\u03B5", "|", end="")
                else:
                    print(suffix, "|", end="")
            if suffixes[-1] == "":
                print("\u03B5", "", end="")
            else:
                print(suffixes[-1], "", end="")
            print("")

    # Handle remaining rules without common prefixes
    remaining_rules = [rule for rule in rules if rule[0] not in group]
    for rule in remaining_rules:
        print(f"{starting}->{rule}")

# Test the function
s = "S->iEtS|iEtS|eS|la"
left_factoring(s)

