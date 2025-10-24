# Function 1: more_than_20

def more_than_20(file):
 
    long_words = []
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) > 20:
                long_words.append(word)
    return long_words


# Function 2: has_no_e

def has_no_e(word):
 
    return 'e' not in word



# Function 3: uses_only

def uses_only(word, letters):
 
    for char in word:
        if char not in letters:
            return False
    return True



# Function 4: all_uses_only

def all_uses_only(file, letters):
 
    valid_words = []
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            if uses_only(word, letters):
                valid_words.append(word)
    return valid_words