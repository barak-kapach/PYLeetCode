def all_vals_in_dict_are_zero(d):
    for val in d.values():
        if val > 0:
            return False
    return True


def minWindow(s, t):

    #basic cases that we havnt solution without check 
    if len(s) < len(t):
        return ""
    if t == s:
        return t
    #initialize to non able val for the res
    win = s + t
    l = 0
    r = 0
    #we can initialize a dictionary
    chars_dict = dict()
    for c in t:
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            chars_dict[c] = 1
    
    temp_dict = chars_dict.copy()

    # the idea is if all the values is 0 so we can we have valid sol of window 
    while l < len(s) and r < len(s):
        #next opening index
        while s[l] not in chars_dict and l < len(s):
            l += 1
        r = l
        while not all_vals_in_dict_are_zero(temp_dict) and r < len(s):
            if s[r] in temp_dict:
                temp_dict[s[r]] -= 1
            r += 1
        if all_vals_in_dict_are_zero(temp_dict):
            if len(win) > (r - l + 1): 
                win = s[l: r]
                l = r
                temp_dict = chars_dict.copy()
        else:
            temp_dict = chars_dict.copy()
            l = r - 1
    return win 

# s = "bdab"
# t = "ab"
# print(minWindow(s, t))



def minWindowNeetCode(s,t):
    if t == "":
        return ""

    counterDict = dict()
    window = dict()
    res, resLen = [-1,-1], float("infinity")
    for c in t:
        if c in counterDict:
            counterDict[c] += 1
        else:
            counterDict[c] = 1 
    have, need = 0, len(counterDict)
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in counterDict and window[c] == counterDict[c]:
            have += 1
        
        while have == need:
            #update out res
            if (r - l + 1) < resLen:
                res = [l , r]
                resLen = (r - l + 1)
            #pop from left
            window[s[l]] -= 1
            if s[l] in counterDict and window[s[l]] < counterDict[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l: r + 1] if resLen != float("infinity") else ""
