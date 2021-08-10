def can_segment_string(s, dictionary):
    for word in dictionary:
        if word in s:
            new_s = s.replace(word, "", 1)
            if new_s == "":
                return True
            else:
                dictionary.remove(word)
                return can_segment_string(new_s, dictionary)
    return False


can_segment_string("loveappplebear", ['love', 'apple', 'bear'])
