from fuzzywuzzy import fuzz

import open_reddit
import sentiment_analysis
import string


def compare_subreddit(sub1, sub2):
    '''
    Compares the similarity (simple ratio, partial ratio, and token sort ratio) of r/mamamoo and other k-pop groups and returns the ratio of each.
    '''
    mamamoo_lst = add_to_list(sub1)
    other_kpop_group = add_to_list(sub2)

    simple_ratio = []
    partial_ratio = []
    token_sort_ratio = []

    for i in range(len(mamamoo_lst)):
        simple_ratio.append(fuzz.ratio(mamamoo_lst[i], other_kpop_group[i]))
        partial_ratio.append(fuzz.partial_ratio(mamamoo_lst[i], other_kpop_group[i]))
        token_sort_ratio.append(fuzz.token_sort_ratio(mamamoo_lst[i], other_kpop_group[i]))
    
    return f'On average, \nThe simple ratio is: {sentiment_analysis.average_lst(simple_ratio)}\n The partial ratio is: {sentiment_analysis.average_lst(partial_ratio)}\n The tokern sort ratio is: {sentiment_analysis.average_lst(token_sort_ratio)}'


def add_to_list(sub):
    '''
    Return a list of top 50 post from a given subreddit.
    '''
    lst = []
    for item in open_reddit.open_reddit(sub, 50):
        for line in item:
            line = line.strip(string.punctuation + string.whitespace)
            lst.append(line)
    return lst


def main():
    # Comparing Mamamoo subreddit to three other k-pop subreddit
    print(compare_subreddit('mamamoo', 'red_velvet'))
    print(compare_subreddit('mamamoo', 'twice'))
    print(compare_subreddit('mamamoo', 'straykids'))

if __name__ == '__main__':
    main()