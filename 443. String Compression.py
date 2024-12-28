def compressWithExtraSpace(chars):
    """
    this sol is naive because we store the result in a new  string
    now after we know how to do it we can do it in place
    :param chars:
    :return:
    """
    i = 0
    n = len(chars)
    stres = ""

    while i < n:

        c = chars[i]
        counter = 0
        # we run on the same char until we find a new one
        #if we have only one char we dont need to add the counter
        while i < n and chars[i] == c:
            i += 1
            counter += 1
        stres += c + (str(counter) if counter > 1 else "")
    # print(stres)

    return len(stres), list(stres)


# check
# print(compressWithExtraSpace(["a", "a", "b", "b", "c", "c", "c"]))
c = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# print(compressWithExtraSpace(c))


def compareWithoutExtraSpace(chars):
    i = 0
    n = len(chars)
    ind_to_write = 0
    if n < 2:
        return n
    while i < n:
        counter = 0
        c = chars[i]
        while i < n and c == chars[i]:
            i += 1
            counter += 1
        #now we know the letter and the number of letter occurrences
        # seperate to cases

        #to each case we need to write the letter - all cases start with write the letter
        chars[ind_to_write] = c
        ind_to_write += 1
        #case the counter is bigger than 1
        if counter > 1:
            for strig_digit in str(counter):
                chars[ind_to_write] = strig_digit
                ind_to_write += 1
    return ind_to_write, list(chars)

print(compareWithoutExtraSpace(c), "this is the test ")
print(compareWithoutExtraSpace(["a", "a", "b", "b", "c", "c", "c"]))

