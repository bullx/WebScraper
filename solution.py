from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict, Counter


class Solution(object):
    link = ""
    weight = 5

    def __init__(self, path):
        self.link = path
        self.diction = defaultdict(int)

    # prints the top n values depending on value supplied
    def printValues(self, val):
        frequent = Counter(self.diction)
        frequent.most_common()
        print("Top " + str(val) + " elements found are ")
        for k, v in frequent.most_common(val):
            print(k)

    # Process the data
    def process(self):

        # Use of beautifulsoup library for parsing the html page
        r = requests.get(self.link)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")

        # Find information for all headers and paragraphs
        for out in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"]):

            stop_words = set(stopwords.words('english'))

            # convert text to lower case
            sentence = out.text.lower()

            # remove special characters and tokenize the words
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(sentence)

            cleanedWords = []

            # remove stop words
            for w in tokens:
                if w not in stop_words:
                    cleanedWords.append(w)

            counter = 1;

            # assign a weight to the counter if it is not a paragraph by considering only headings
            if out.name != "p":
                counter = counter * 5

            # increment the counter value in dictionary if the words are founds or add new words to the dictionary
            for words in cleanedWords:

                if words in self.diction:
                    self.diction[words] += counter
                else:
                    self.diction[words] = 1


def main():
    link1 = "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"
    link2 = "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"
    link3 = "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"
    sol = Solution(link3)
    sol.process()
    sol.printValues(5)


if __name__ == '__main__':
    main()
