# start with some programing languade to be included
high_level_programing = ['java', 'python','go', 'klotin']
programing_languages = []
# simulate copying each language until none are left
# move each language to programming after copying
while high_level_programing:
    all_langagues = high_level_programing.pop()
    # simulate creating all languages from high level programming
    print(all_langagues.title() + " is a high level programming language")
    programing_languages.append(all_langagues)
# Display all programing languages
print("\nThe following are object orientend programing langugues")
for programing_language in programing_languages:
    print(programing_language.title())

def programing(high_level_programming, programming_languages ):

    while high_level_programming:
        all_langagues = high_level_programming.pop()
        print(all_langagues + "is a high level language")
        programming_languages.append(all_langagues)
    def show_programming_languages(programming_languages):
        print("\nThe following are object oriented programming languages")
        for programing_language in programming_languages:
            print(programing_language)
    high_level_programming = ['java', 'klotin', 'python', 'go']
    programming_languages = []
    programing(high_level_programming, programming_languages)
    show_programming_languages(programming_languages)

