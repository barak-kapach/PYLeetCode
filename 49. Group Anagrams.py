def groupAnagrams(strs):
        #we can order a string by this 
        #we generate every string into the order key like that 
        # sorted_string = ''.join(sorted(s)
        d = dict()

        for s in strs:
            sorted_string = str(''.join(sorted(s)))
            if sorted_string in d:
                d[sorted_string] += [s]
            else:
                d[sorted_string] = [s]
        res = []
        for key in d:
            res.append(d[key])
        return res

def groupWithCountingStrategy(strs):

    d = dict()
    #we use hash but the key will be seq of zeros and ones
    for s in strs:
        arr = [0] *(ord('z') - ord('a') + 1)
        for c in s:
            arr[ord(c) - ord('a')] += 1
        d[tuple(arr)] = d.get(tuple(arr), []) + [s]
    res = []
    for key in d:
        res.append(d[key])
    return res

#tests
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupWithCountingStrategy(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupWithCountingStrategy([""]))
print(groupAnagrams(["a"]))
print(groupWithCountingStrategy(["a"]))
print(groupAnagrams(["ab","ba"]))
print(groupWithCountingStrategy(["ab","ba"]))
print(groupAnagrams(["ab","ba",""]))
print(groupWithCountingStrategy(["ab","ba",""]))
print(groupAnagrams(["ab","ba","a"]))
print(groupWithCountingStrategy(["ab","ba","a"]))