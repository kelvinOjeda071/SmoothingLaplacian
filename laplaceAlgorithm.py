# Movie message
movie="A PERFECT WORLD "
movie+="MY PERFECT WOMAN "
movie+="PRETTY WOMAN"

#Song Message
song= "A PERFECT DAY "
song+="ELECTRIC STORM "
song+="ANOTHER RAINY DAY"

# Split the words in the set of message
movie_word=movie.split(" ")
song_word=song.split(" ")
# print(s for s in song_word)


def individual_probability(set_of_probability , word_probability: str):
    return set_of_probability.count(word_probability.upper())/len(set_of_probability)


# print(individual_probability(movie_word, "perfect"))
def global_probability(set_of_1, set_of_2, phrase_probability: str):
    # Split the phrase in upper letters
    set_of_words=phrase_probability.upper().split(" ")

    # In set of movie
    result1=words_in_set(set_of_words, set_of_1, set_of_2)
    # In set of song
    result2=words_in_set(set_of_words, set_of_2, set_of_1)
    # Final probability
    return result1/(result1+result2)

def laplace_smoothing(set_of_1, set_of_2, phrase_probability: str, number_of_classes: int):
    # Split the phrase in upper letters
    set_of_words = phrase_probability.upper().split(" ")

    # In set of movie
    result1 = words_in_set(set_of_words, set_of_1, set_of_2)

    # In set of song
    result2 = words_in_set(set_of_words, set_of_2, set_of_1)

    # Final probability
    return (result1 + 1) / ((result1 + result2)+(1*number_of_classes))



def set_of_probability(set_of_1, set_of_2):
    return len(set_of_1)/(len(set_of_1)+len(set_of_2))


def words_in_set(set_of_words, set_global_part1, set_of_global_part2):
    result=1
    for i in set_of_words:
        result *= set_global_part1.count(i)/len(set_global_part1)
    result=result * set_of_probability(set_global_part1, set_of_global_part2)
    return result

word1 = "perfect"
print("Single probability")
print(f"P({word1.upper()}|Movie )=> {individual_probability(movie_word, word1)}")

print(f"P({word1.upper()}|Song )=> {individual_probability(song_word, word1)}")

word2 = "Storm"
# print("Single probability")
print(f"P({word2.upper()}|Movie) => {individual_probability(movie_word, word2)}")
print(f"P({word2.upper()}|Song) => {individual_probability(song_word, word2):.4f}")

phraseToSearch= word1+" "+word2
print("Global probability")
print("Without laplace smoothing")
print(f"P(Movie|{phraseToSearch.upper()}) => {global_probability( movie_word, song_word,phraseToSearch)}")
print("With laplace smoothing")
print(f"P(Movie|{phraseToSearch.upper()}) => {laplace_smoothing(movie_word, song_word,phraseToSearch, 2):.6f}")