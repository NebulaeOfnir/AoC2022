# PART 1

# Read input txt into string - seperated by \n\n - split into another list of str for each elf
elves = [elf.split() for elf in
         open(r"input.txt").read().split('\n\n')]

# String to int cast, use sum on generator to get sum of each elf, use max on list of calories per elf to get most
# calories per elf
elves_biggest = max([sum([int(calorie) for calorie in elf]) for elf in elves])

print(elves_biggest)

# PART 2

# Same as above - except sort list of elves and add top 3 by size together
elves_biggest3 = sorted([sum([int(calorie) for calorie in elf]) for elf in elves])

print(sum(elves_biggest3[-3:]))
