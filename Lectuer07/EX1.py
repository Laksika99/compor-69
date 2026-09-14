survey_results = [
    ["Python", "JavaScript", "C++"],
    ["python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

sets =[set(p) for p in survey_results]
all_common = set.intersection(*sets)
language_count = {}
for s in sets:
    for lang in s:
        language_count[lang] = language_count.get(lang, 0) + 1

        only_one = [lang for lang, count in language_count.items() if count == 1]

        unique_languages = set.union(*sets)

        exactly_two = [lang for lang, count in language_count.items() if count == 2]

        same_participants = []
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if sets[i] == sets[j]:
                    same_participants.append((i + 1, j + 1))

                    print("1. Languages chosen by all participants:", all_common)
                    print("2. Languages chosen by only one participant:", only_one)
                    print("3. Number of unique languages chosen by all participants:", len(unique_languages))
                    print("4. Languages chosen by exactly two participants:", exactly_two)
                    print("5. Pairs of participants with the same language preferences:", same_participants)