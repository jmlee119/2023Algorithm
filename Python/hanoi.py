def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)

hanoi(3, "A", "C", "B")