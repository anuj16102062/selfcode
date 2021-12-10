# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    i = 1 
    j = 0
    ##lps = [0,0,1,2,0,1,2,3,4] first always zero if match put 1 and i++,j++ if not match and j != 0 then j = lps[j-1] other wise lps[i]= 0 i++
    while i < M:
        if pat[j] == pat[i]:
            j +=1
            lps[i] = j
            i+=1
        else:
            if j !=0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i+=1
  
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
  
# This code is contributed by Bhavya Jain
