def valid_brackets(s):
    #  "([)]" is invalid because have two different brackets facing each other
    #  "((()" is invalid because they have different numbers of brackets

    count_curly1 = 0  # count {
    count_curly2 = 0  # count }

    count_square1 = 0  # count [
    count_square2 = 0  # count ]

    count_round1 = 0  # count (
    count_round2 = 0  # count )

    for i in range(len(s)):

        if i <= len(s) - 2:
            if check_facing_diff_brackets(s[i:i+2]):
                return False

        if s[i] == '(':
            count_round1 += 1

        elif s[i] == '{':
            count_curly1 += 1

        elif s[i] == '[':
            count_square1 += 1

        elif s[i] == ')':
            count_round2 += 1

        elif s[i] == '}':
            count_curly2 += 1

        elif s[i] == ']':
            count_square2 += 1

    if (count_curly1 == count_curly2) and (count_round1 == count_round2) and (count_square1 == count_square2):
        return True
    else:
        return False


def check_facing_diff_brackets(brackets):
    if brackets[1] == ')':
        second_type = "round"
    elif brackets[1] == '}':
        second_type = "curly"

    elif brackets[1] == ']':
        second_type = "square"
    else:
        second_type = "dontcare"

    if brackets[0] == '(':
        first_type = "round"

    elif brackets[0] == '{':
        first_type = "curly"

    elif brackets[0] == '[':
        first_type = "square"

    else:
        first_type = "dontcare"

    if first_type == second_type or second_type == "dontcare" or first_type == "dontcare":
        return False
    else:
        return True


test1 = "([])[]({})"
test2 = "([)]"
test3 = "((()"
test4 = "((([][])))"
print(valid_brackets(test1))
print(valid_brackets(test2))
print(valid_brackets(test4))