
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s2) == 0:
        return len(s1)

    previous_row = list(range(len(s2) + 1))

    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def spell_check(word, word_list, max_distance):
    suggestions = []
    for w in word_list:
        distance = levenshtein_distance(word, w)
        if distance <= max_distance:
            suggestions.append((w, distance))
    suggestions.sort(key=lambda x: x[1])
    return suggestions

if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "pear", "peach"]
    word = input("type your wrong word: ")
    #word = "aple"
    max_distance = 1
    suggestions = spell_check(word, word_list, max_distance)
    print("Suggestions for", word, ":", [s[0] for s in suggestions])
