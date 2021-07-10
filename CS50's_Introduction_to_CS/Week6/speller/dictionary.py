# Words in dictionary
words = set()


def check(word):
    # Return true if word is in dictionary else false
    if word.lower() in words:
        return True
    else:
        return False


def load(dictionary):
    # Loading dictionary into memory
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip())
    file.close()
    return True


def size():
    # Returns number of words in dictionary
    return len(words)


def unload():
    # Unloads dictionary from memory
    # No need as memory is managed by python.
    return True
