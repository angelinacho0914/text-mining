import string
import open_reddit


def process_information(sub):
    '''
    Read the top 50 reddit submissions from r/subreddit, and return the dictionary of word with word frequencies.
    '''
    h = dict()
    
    for item in open_reddit.open_reddit(sub, 50):
        for line in item:
            # Strip they're in string and split they're in lists
            line = line.strip(string.punctuation + string.whitespace)
            # Split them into individual words
            word = line.split()
            for i in word:
                i = i.strip(string.punctuation + string.whitespace) # We do not want punctuation and whitespace in our strings
                i = i.lower()

                h[i] = h.get(i, 0) + 1
    return h


def total_words(hist):
    '''
    Return the total number in frequencies of histogram.
    '''
    return sum(hist.values())


def different_words(hist):
    '''
    Return the number of different words in the histogram.
    '''
    return len(hist.keys())


def most_common_words(hist, num, unimportant_words):
    '''
    Retun a list of given number of most common words in the histogram by using the histogram and excluding the given list of unimportant words.
    '''
    lst = []
    for word, freq in hist.items():
        if word not in unimportant_words:
            lst.append((freq, word))
    lst.sort(reverse=True)
    return lst[0:num]


def main():
    histogram_mamamoo = process_information('mamamoo')    # Print a histogram of frequency of words in r/mamamoo
    histogram_redvelvet = process_information('red_velvet')    # Print a histogram of frequency of words in r/red_velvet
    histogram_straykids = process_information('straykids')    # Print a histogram of frequency of words in r/straykids
    histogram_twice = process_information('twice')    # Print a histogram of frequency of words in r/twice
    
    print(f'The total number of words in the top 50 post of r/mamamoo is: {total_words(histogram_mamamoo)}')
    print(f'The total number of words in the top 50 post of r/red_velvet is: {total_words(histogram_redvelvet)}')
    print(f'The total number of words in the top 50 post of r/twice is: {total_words(histogram_twice)}')
    print(f'The total number of words in the top 50 post of r/straykids is: {total_words(histogram_straykids)}')
    
    print(f'The number of different words is: {different_words(histogram_mamamoo)}')
    
    # I have a list of words that are not important, so those words will be ignored when I retrieve the most common words
    with open('data/unimportant_words.txt') as f:
        lines = f.readlines()
    unimportant_lst = ['']
    for item in lines:
        for w in item.split():
            unimportant_lst.append(w)
    print(f'The most common words for r/mamamoo are: {most_common_words(histogram_mamamoo, 10, unimportant_lst)}')
    print(f'The most common words for r/red_velvet are: {most_common_words(histogram_redvelvet, 10, unimportant_lst)}')
    print(f'The most common words for r/twice are: {most_common_words(histogram_twice, 10, unimportant_lst)}')
    print(f'The most common words for r/straykids are: {most_common_words(histogram_straykids, 10, unimportant_lst)}')


if __name__ == "__main__":
    main()