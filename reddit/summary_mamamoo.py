import string
import open_reddit


def process_information():
    '''
    Read the top 50 reddit submissions from r/mamamoo, and return the word frequencies
    '''
    h = dict()
    
    for item in open_reddit.open_reddit('mamamoo', 50):
        for line in item:
            # Strip they're in string and split they're in lists
            line = line.strip(string.punctuation + string.whitespace)
            # Split them into individual words
            word = line.split()
            for i in word:
                i = i.strip(string.punctuation + string.whitespace)
                i = i.lower()

                h[i] = h.get(i, 0) + 1
    return h


def total_words(hist):
    '''
    Return the total number in frequencies of histogram
    '''
    return sum(hist.values())


def different_words(hist):
    '''
    Return the number of different words in the histogram
    '''
    return len(hist.keys())


def most_common_words(hist, num, unimportant_words):
    '''
    Retun a list of given number of most common words in the histogram
    '''
    lst = []
    for word, freq in hist.items():
        if word not in unimportant_words:
            lst.append((freq, word))
    lst.sort(reverse=True)
    return lst[0:num]


def main():
    histogram_mamamoo = process_information()    # Print a histogram of frequency of words in r/mamamoo
    
    print(f'The total number of words in the top 50 post of r/mamamoo is: {total_words(histogram_mamamoo)}')
    
    print(f'The number of different words is: {different_words(histogram_mamamoo)}')
    
    with open('data/unimportant_words.txt') as f:
        lines = f.readlines()
    unimportant_lst = ['']
    for item in lines:
        for w in item.split():
            unimportant_lst.append(w)
    print(f'The most common words are: {most_common_words(histogram_mamamoo, 10, unimportant_lst)}')


if __name__ == "__main__":
    main()