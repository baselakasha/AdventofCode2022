def get_calories_for_each_elf(data):
    elfs_calories = {}
    elf_number = 0
    for item_calories in data:
        if item_calories == "":
            elf_number+=1
            continue

        elfs_calories.setdefault(elf_number, 0)
        elfs_calories[elf_number] += int(item_calories)
    return elfs_calories