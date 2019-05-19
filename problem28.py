def justify(arr, k):

    current_left_space = k
    blank_space_pos = []  # store index of ' ' in list
    current_line = []

    for x in arr:
        if len(x) >= current_left_space:
            # before jumping to a new line we have to balance the blank spaces in the line

            current_line = balance_line(current_line, current_left_space, blank_space_pos)

            print(''.join(current_line))  # print and create new line
            current_line.clear()  # reset current line

            current_line.append(x)
            current_left_space = k - len(x)

            blank_space_pos.clear()  # reset for the new line
        else:
            if current_line:  # if before the first word in the line add blank space
                current_line.append(' ')
                current_left_space -= 1
                blank_space_pos.append(len(current_line) - 1)

            current_line.append(x)
            current_left_space -= len(x)

            if current_left_space == 0:  # Fits perfectly
                print(''.join(current_line))
                current_line.clear()

                current_left_space = k
                blank_space_pos.clear()  # reset for the new line

    if current_line:
        print(''.join(balance_line(current_line, current_left_space, blank_space_pos)))


def balance_line(current_line, current_left_space, blank_space_pos):
    n_blank_spaces = current_left_space
    i = 0
    n_loops = 0  # count the number of loops
    if not blank_space_pos: # this happens when there is only one word
        for c in range(current_left_space + 1):
            current_line.append(' ')
        return current_line

    while n_blank_spaces >= 1:
        if i >= len(blank_space_pos):
            i = 0  # restart putting blank spaces
        current_line.insert(blank_space_pos[i]+(n_loops +i)*i ,  # add i because each time we add the words after the index i is moved i*n_loops index
                            '&')  # insert a blank space at blank space position by the number of left spaces
        n_blank_spaces -= 1
        i += 1
        n_loops += 1

    return current_line


test = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
test2 = ["thae", "quickaaa", "braaown", "foxaa", "jumaaps", "oaaver", "tahe", "laaaaazy", "daaaaog"]
k = 16
justify(test, k)
justify(test2, k)
