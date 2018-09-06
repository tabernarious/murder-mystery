import re

def sentence_count(text):
    # Count the number of sentences by looking for sentence-ending punctuation with a trailing space
    #  to cover situations where multiple punctuation marks are used (e.g. !! or ?! or ...).

    # Strip leading and trailing whitespace, just in case the string was not already clean.
    text_stripped = text.strip()

    # We start with a value of one to include the final sentence which should not have space after it.
    sentence_count = 1
    for punctuation in [".", "?", "!"]:
        sentence_count += text_stripped.count(punctuation + " ")
    return sentence_count

def get_average_sentence_length_by_characters(text):
    # Strip leading and trailing whitespace.
    text_stripped = text.strip()
    # Divide the total text length by the number of sentences.
    return len(text_stripped) / sentence_count(text_stripped)

def get_average_sentence_length(text):
    # Strip leading and trailing whitespace, just in case the string was not already clean.
    text_stripped = text.strip()

    # Count total words in text
    word_count = len(text_stripped.split(" "))

    # Divide the total word count by the number of sentences.
    return word_count / sentence_count(text_stripped)

def prepare_text(text):
    # Requires module re
    # Strip all punctuation from the text
    clean_text = re.sub('[^a-zA-Z0-9_ ]', '', text)
    
    # Set all characters to lowercase
    clean_text = clean_text.lower()
    
    # Return the entire text as a list of words in order
    return clean_text.split()

def build_frequency_table(corpus):
    frequency_table = {}
    
    # Check each element of corpus for existence in frequency_table. Add or increment the element's value.
    for element in corpus:
        if element in frequency_table.keys():
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1
    
    return frequency_table

def build_frequency_table(corpus):
    frequency_table = {}
    
    # Check each element of corpus for existence in frequency_table. Add or increment the element's value.
    for element in corpus:
        if element in frequency_table.keys():
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1
    
    return frequency_table

def ngram_creator(text_list):
    # Create a blank list to hold our list of ngrams
    ngram_list = []
    
    # Iterate through the text_list to get text_list[i] and text_list[i+1], and append the pair as an element in ngram_list, but end one index short since the last word in text_list will not have following word.
    for i in range(len(text_list) - 1):
        ngram_list.append("{element} {next_element}".format(element=text_list[i], next_element=text_list[i+1]))
        
    return ngram_list

def frequency_comparison(table1, table2):
    # The number of appearances of all unique ngrams across both table1 and table2
    appearances = 0

    # The number of appearances of mutual ngrams bewtween table1 and table2
    mutual_appearances = 0

    # Iterate through table1's keys, check if the key exists in table2.
    #   For mutual keys add the smaller value to mutual_appearances, and add the larger value to appearances.
    #   For non-mutual keys, add the table1 value to appearances.
    # Then iterate through table2's keys, check if the key exists in table1.
    #   Ignore mutual keys (these have already been accounted for)
    #   For non-mutual keys, add the table2 value to appearances.
    for ngram in table1.keys():
        if ngram in table2.keys():
            if table1[ngram] < table2[ngram]:
                mutual_appearances += table1[ngram]
                appearances += table2[ngram]
            else:
                mutual_appearances += table2[ngram]
                appearances += table1[ngram]
        else:
            appearances += table1[ngram]
    for ngram in table2.keys():
        if ngram not in table1.keys():
            appearances += table2[ngram]

    # Return the frequency comparison
    return mutual_appearances / appearances

def percent_difference(sample1, sample2):
    # Calculate and return: (v1 - v2) / ((v1 + v2)/2)
    return abs(sample1.average_sentence_length - sample2.average_sentence_length) / ((sample1.average_sentence_length + sample2.average_sentence_length)/2)

def percent_difference_characters(sample1, sample2):
    # Calculate and return: (v1 - v2) / ((v1 + v2)/2)
    return abs(sample1.average_sentence_length_by_characters - sample2.average_sentence_length_by_characters) / ((sample1.average_sentence_length_by_characters + sample2.average_sentence_length_by_characters)/2)

def find_text_similarity(sample1, sample2):
    sentence_length_difference = percent_difference(sample1, sample2)
    sentence_length_similarity = abs(1 - sentence_length_difference)
    word_count_similarity = frequency_comparison(sample1.word_count_frequency, sample2.word_count_frequency)
    ngram_similarity = frequency_comparison(sample1.ngram_frequency, sample2.ngram_frequency)

    return (sentence_length_similarity + word_count_similarity + ngram_similarity) / 3

class TextSample:
    def __init__(self, text, author):
        self.raw_text = text
        self.prepared_text = prepare_text(text)
        self.average_sentence_length = get_average_sentence_length(text)
        self.average_sentence_length_by_characters = get_average_sentence_length_by_characters(text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram_frequency = build_frequency_table(ngram_creator(self.prepared_text))
        self.author = author
    def __repr__(self):
        return "Author: {author}\nAverage Sentence Length: {average_sentence_length}\n".format(author=self.author, average_sentence_length=self.average_sentence_length)


murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."

myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."

lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"

gregg_t_fishy_intro = "A most good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young, an adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might find yourself asking? Why, I happen to always be fishing for compliments of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television, I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life, every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay To Remember, it certainly seems like a grand time to explore life and love."


murderer_sample = TextSample(murder_note, "Murder Note")
lily_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
myrtle_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T Fishy")


#print(sentence_count(myrtle_beech_intro))

#print(get_average_sentence_length(murder_note))
#print(get_average_sentence_length(myrtle_beech_intro))
#print(get_average_sentence_length(lily_trebuchet_intro))
#print(get_average_sentence_length(gregg_t_fishy_intro))

#print(murderer_sample)
#print(lily_sample)
#print(myrtle_sample)
#print(gregg_sample)

#print(prepare_text(murder_note))
#print(murderer_sample.prepared_text)

#print(build_frequency_table(murderer_sample.prepared_text))
#print(build_frequency_table(lily_sample.prepared_text))
#print(build_frequency_table(myrtle_sample.prepared_text))
#print(build_frequency_table(gregg_sample.prepared_text))
#print(murderer_sample.word_count_frequency)

#print(ngram_creator(['what', 'in', 'the', 'world', 'is', 'going', 'on']))
#print(ngram_creator(murderer_sample.prepared_text))

#print(build_frequency_table(ngram_creator(murderer_sample.prepared_text)))

#print(murderer_sample.ngram_frequency)
#print(lily_sample.ngram_frequency)
#print(myrtle_sample.ngram_frequency)
#print(gregg_sample.ngram_frequency)

print()
print("Text Similarity to Murder Note:")
print("{author}: {similarity}".format(author="Murder Note", similarity=find_text_similarity(murderer_sample, murderer_sample)))
print("{author}: {similarity}".format(author=lily_sample.author, similarity=find_text_similarity(murderer_sample, lily_sample)))
print("{author}: {similarity}".format(author=myrtle_sample.author, similarity=find_text_similarity(murderer_sample, myrtle_sample)))
print("{author}: {similarity}".format(author=gregg_sample.author, similarity=find_text_similarity(murderer_sample, gregg_sample)))

print()
print("ngram Frequency Comparison:")
print(frequency_comparison(murderer_sample.ngram_frequency, murderer_sample.ngram_frequency))
print(frequency_comparison(murderer_sample.ngram_frequency, lily_sample.ngram_frequency))
print(frequency_comparison(murderer_sample.ngram_frequency, myrtle_sample.ngram_frequency))
print(frequency_comparison(murderer_sample.ngram_frequency, gregg_sample.ngram_frequency))

print()
print("Word Count Frequency Comparison:")
print(frequency_comparison(murderer_sample.word_count_frequency, murderer_sample.word_count_frequency))
print(frequency_comparison(murderer_sample.word_count_frequency, lily_sample.word_count_frequency))
print(frequency_comparison(murderer_sample.word_count_frequency, myrtle_sample.word_count_frequency))
print(frequency_comparison(murderer_sample.word_count_frequency, gregg_sample.word_count_frequency))

print()
print("Average Sentence Length (words) Percent Similarity:")
print(abs(1 - percent_difference(murderer_sample, murderer_sample)))
print(abs(1 - percent_difference(murderer_sample, lily_sample)))
print(abs(1 - percent_difference(murderer_sample, myrtle_sample)))
print(abs(1 - percent_difference(murderer_sample, gregg_sample)))

print()
print("Average Sentence Length (characters) Percent Similarity:")
print(abs(1 - percent_difference_characters(murderer_sample, murderer_sample)))
print(abs(1 - percent_difference_characters(murderer_sample, lily_sample)))
print(abs(1 - percent_difference_characters(murderer_sample, myrtle_sample)))
print(abs(1 - percent_difference_characters(murderer_sample, gregg_sample)))

print()
print("Gregg T Fishy appears to have killed Jay Stacksby, though Myrtle Beech's text similarity is a bit high to declare this as \"obvious\". If ngram frequency or word count frequency were weighted higher than average sentence length (I have no reason to believe this should be the case linguistically) the tables could quickly turn towards Myrtle. Myrtle beat out Gregg in two of three categories, but Gregg blew Myrtle out of the water for average sentence length similarity.")
