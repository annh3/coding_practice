# the solve function 
# the solve function 
def solve(word, i, j, words_list, crossword, n, m, solution):
    # base case is if we correctly place the last word
    
    # first go right
    # then go down
    if j+1 < m and crossword[i][j+1] != '+':
        # go right
        count = 0
        for k in enumerate(word):
            count += 1
            # check consistency
            if crossword[i][j+k] == '+':
                return
            if crossword[i][j+k] != '-':
                if crossword[i][j+k] != word[k]:
                    return
        if j+count < m and crossword[i][j+count] != '+':
            return 
        
        for k in enumerate(word):
            crossword[i][j+k] = word[k]
            
    else:
        # go down
        for k in enumerate(word):
            count += 1
            # check consistency
            if crossword[i+k][j] == '+':
                return
            if crossword[i+k][j] != '-':
                if crossword[i+k][j] != word[k]:
                    return
        if j+count < n and crossword[i+count][j] != '+':
            return 
        
        for k in enumerate(word):
            crossword[i+k][j] = word[k]
    
    if len(words_list) == 0:
        solution.append(crossword)
        return
        
    # recurse
    flag = False
    while i < n:
        while j < m:
            j += 1
            if crossword[i][j] == '-':
                flag = True
                break
        if flag == True:
            break
        # j = m
        j = -1
        i += 1
                
        
    cross_copy = copy.deepcopy(crossword)
    for i, word in enumerate(words_list):
        solve(words_list[i], i, j, words_list[:i]+words_list[i+1:], cross_copy, n, m, solution)
            

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    words_list = words.split(';')
    solution = list()
    
    n = len(crossword)
    m = len(crossword[0])
        
    # once we find a '-' we need to figure out which direction it goes in
    # based on the structure of our search, it will go down or to the right
    # we can check for '--' to make a decision
    # then we will need to try one of our remaining words
    
    # constraints
    # if the next contiguous block is a letter, it must conform with a word
    # the word must fit into the space exactly, leaving no '-' or letters behind
    
    # goal 
    # we have placed all the words
    
    # we need a backtrack function
    # we need we need a check constraints per word function
    solve(words_list, crossword, n, m, solution)
    
    # do something to solution


def test1():
    sample = """
    ++++++-+++
    ++------++
    ++++++-+++
    ++++++-+++
    +++------+
    ++++++-+-+
    ++++++-+-+
    ++++++++-+
    ++++++++-+
    ++++++++-+
    ICELAND;MEXICO;PANAMA;ALMATY
    """


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()