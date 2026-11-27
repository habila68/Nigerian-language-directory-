# ===== NIGERIAN LANGUAGES DICTIONARY =====

dictionary = {
    # HAUSA
    "sannu": "Hello (Hausa)",
    "na gode": "Thank you (Hausa)",
    "ruwa": "Water (Hausa)",
    "abinci": "Food (Hausa)",
    "gida": "House (Hausa)",

    # YORUBA
    "bawo ni": "How are you? (Yoruba)",
    "e se": "Thank you (Yoruba)",
    "omi": "Water (Yoruba)",
    "ounje": "Food (Yoruba)",
    "ile": "House (Yoruba)",

    # IGBO
    "ndewo": "Hello (Igbo)",
    "daalu": "Thank you (Igbo)",
    "mmiri": "Water (Igbo)",
    "nri": "Food (Igbo)",
    "ulo": "House (Igbo)",

    # TIV
    "m sugh": "Thank you (Tiv)",
    "aondo": "God (Tiv)",
    "ter": "Father (Tiv)",
    "iye": "Mother (Tiv)",
    "mba": "No (Tiv)"
}

print("===== NIGERIAN LANGUAGES DICTIONARY =====")
print("Available languages: Tiv, Hausa, Yoruba and Igbo")

while True:
    word = input("\nWhat do you want to ask? ").lower().strip()

    if word in dictionary:
        print("English Meaning:", dictionary[word])
    else:
        print("Invalid! Word not found in the dictionary.")
        continue

    next_question = input("\nNext? (yes/no): ").lower().strip()

    if next_question == "yes":
        continue
    else:
        print("Thank you for using the dictionary!")
        break
