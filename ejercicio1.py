text = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Split the text into sentences
sentences = text.split("#")

# Capitalize the first letter of each sentence
capitalized_sentences = [sentence.capitalize() for sentence in sentences]

# Join the sentences with line breaks
formatted_text = "\n\n".join(capitalized_sentences)

print(formatted_text)