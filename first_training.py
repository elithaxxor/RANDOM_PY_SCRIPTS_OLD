import pd, sys, traceback
from pandas \
import json, nltk


def topten():
    yield 1
    yield 2
    yield 3
    yield 4


def training(self):
    pass
    try:
        message = input('')
        data = json.loads(message)
        self.split()
        tokens = nltk.word_tokenize(message)
        print(tokens)
        tag = nltk.pos_tag(tokens)
        print(tag)
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(tag)
        print(result)
        result.draw()  # It will draw the pattern graphically which can be seen in Noun Phrase chunking
        print(f'[+] Please enter the message you would like to encrypt')
        message = input('')
        message = message.split() ## to conver cars to lower case

        ### serialize json
        results = []
        for chunk in pd.read_csv():
            results.append(sum(chunk['X']))
        total = sum(results)
        print(total)

        nltk.download()


        values = topten()
        print(values.__next__())
        print(values.__next__())

        for i in values:
            print(i)

        ###  LOADING THE DATA
        ## 1 TOKENIZ
        sentence = """At eight o'clock on Thursday morning
        ... Arthur didn't feel very good."""
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        print(tagged[0:6])


        # 2 display enetitites

        entities = nltk.chunk.ne_chunk(tagged)
        # entities
        ## count pos tags
        text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
        lower_case = text.lower()
        tokens = nltk.word_tokenize(lower_case)
        tags = nltk.pos_tag(tokens)
        counts = Counter(tag for word, tag in tags)
        print(counts)

        ### COUNTING POS TAGS

        text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
        lower_case = text.lower()
        tokens = nltk.word_tokenize(lower_case)
        tags = nltk.pos_tag(tokens)
        counts = Counter(tag for word, tag in tags)
        print(counts)

        #  from nltk.corpus import treebank
        t = treebank.parsed_sents('wsj_0001.mrg')[0]
        t.draw()

        ## produces graphicsal of dispalyed words s
        a = "Gase     visit the site guru99.com and much more."
        words = nltk.tokenize.word_tokenize(a)
        fd = nltk.FreqDist(words)
        fd.plot()
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        print(sys.exc_info()[2])
        pass




