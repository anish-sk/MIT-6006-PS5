def count_anagrams(strings):
    "Return the number of pairs of anagrams in a tuple of strings"
    ##################
    # YOUR CODE HERE #
    ##################
    distinct_strings={}
    for string in strings:
        distinct_strings[string]=1
    table_of_frequency_table={}
    for string in distinct_strings.keys():
        freq=[0 for i in range(26)]
        for ch in string:
            freq[ord(ch)-ord('a')]+=1
        freq=tuple(freq)
        if(freq not in table_of_frequency_table):
            table_of_frequency_table[freq]=1
        else:
            table_of_frequency_table[freq]+=1
    ans=0
    for freq in table_of_frequency_table:
        m=table_of_frequency_table[freq]
        ans+=(m*(m-1))/2   

    return ans
