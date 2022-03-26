import open_reddit
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment():
    '''
    Prints out the average negativity, positivity, neutrality, and compound index of top 50 posts on r/mamamoo, rounded to 3 decimal place.
    '''
    neg_score = []  # Creating lists to store the all the score of each element
    pos_score = []
    neu_score = []
    comp_score = []
    for item in open_reddit.open_reddit('mamamoo', 50):
        for line in item:
            line = line.strip(string.punctuation + string.whitespace)
            score = SentimentIntensityAnalyzer().polarity_scores(line)  # Getting the Sentiment Analysis of each post
            # The compound index = +1 means it's most extreme positive while -1 means it's most extreme negative
            # Neg means negative, neu means neutral, pos means positive score of the text
            if score['neg'] > 0.0 or score['neu'] > 0 or score['pos'] > 0 and score['compound'] > 0:
                neg_score.append(score['neg'])
                pos_score.append(score['pos'])
                neu_score.append(score['neu'])
                comp_score.append(score['compound'])

    return f'Average Negativity: {round(average_lst(neg_score), 3)}, Average Neutrality: {round(average_lst(neu_score), 3)}, Average Positivity: {round(average_lst(pos_score), 3)}, Average Compound index: {round(average_lst(comp_score), 3)}'


def average_lst(lst):
    '''
    Calculate the average of the given list of numbers and returns the average.
    '''
    avg = sum(lst) / len(lst)
    return avg
                 
    
def main():
    print(f'Result of sentiment analysis: {sentiment()}')

if __name__ == '__main__':
    main()
