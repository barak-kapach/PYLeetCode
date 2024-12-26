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
        if word != "":
            if res == "":
                res = word
            else:
                res = word + " " + res
    # print(res)
    return res 

reverseWords("the sky is blue")
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
print(reverseWords("  Bob    Loves  Alice   "))
print(reverseWords("Alice does not even like bob"))
