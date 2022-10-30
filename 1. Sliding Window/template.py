'''
Slinding Window Template
'''

def find_substring(s : str):
    start = end = 0 # two pointers 
    counter = 0  # to check if the substring is valid 
    d = 0 # the length of substring 
    mp = {} 
    for i in s : # to initialize hash map
        mp[i] = mp.get(i,0) + 1
    while end < len(s):
        if mp.get(mp[s[end]], 0) == condition: #modify counter here 
            pass 
        
        #counter condition
        while counter : 
            #update d if minimum is required 
            # increase begin to make it invalid/valid again
            if(mp[s[begin++]]++ ?){ /*modify counter here*/ }

        # update d if maximum is required 
        end += 1
    return d 