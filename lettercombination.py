def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}

    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        for n in digits:
            for letter in letters[n]:
                path += letter
                backtrack(digits[1:], path, res)
                path = path[:-1]


    res = []
    backtrack(digits, '', res)
    return print(res)
letterCombinations('23')