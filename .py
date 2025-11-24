pip install nltk


import nltk
nltk.download('wordnet')



from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = set()

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace("_", " "))
    
    return sorted(synonyms)


def synonym_finder():
    print("📚 SYNONYM FINDER")

    while True:
        word = input("\nEnter a word (or EXIT to stop): ")

        if word.lower() == "exit":
            print("👋 Exiting Synonym Finder.")
            break

        synonyms = get_synonyms(word)

        if synonyms:
            print("\n✨ Synonyms found:")
            for s in synonyms:
                print("-", s)
        else:
            print("❌ No synonyms found!")


# Run the program
synonym_finder()
