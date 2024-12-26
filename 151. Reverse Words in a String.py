def reverseWords(s):
    # we can run on the original array and when we found the next word we 
    #can add to the res like that res = new_word + " " + res

    ind = 0
    res = ""
    while ind < len(s):
        word = ""
        while ind < len(s) and s[ind] == " ":
            ind += 1
        while ind < len(s) and s[ind] != " ":
            word += s[ind]
            ind += 1
        res = word + " " + res
    # print(res)
    return res 

reverseWords("the sky is blue")
