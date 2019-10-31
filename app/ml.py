import re
from nltk.corpus import stopwords
import sqlite3

import os
import pyprind
import numpy as np
import requests
import json

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier

import pickle

dirname = os.path.dirname('../')

dir_name = os.path.dirname(__file__)


class MlHelper():
    def __init__(self):
        self.classefier()

    def get_video_id(self, url):
        self.video_id = url.split('=')[1]
        self.get_respons_jsone()

    def get_respons_jsone(self):

        url = 'https://www.googleapis.com/youtube/v3/commentThreads'
        key_api = 'AIzaSyC6mUfTewPh2ZPZHUFWbYu45J7dSI4PKOk'
        some_part = 'snippet'
        self.r = requests.get(url=url, params={'videoId': self.video_id,
                                                'key':key_api,
                                                'part':some_part,
                                                'maxResults':100,
                                                })
        # self.save_to_json_file()

    def save_to_json_file(self):
        with open(os.path.join(dir_name, 'respons.json'), 'w') as f:
            json.dump(self.r.json(), f, indent=2, ensure_ascii=False)

    def get_comments(self):
        # json_file_ = os.path.join(dir_name, 'respons.json')
        # data = json.load(open(json_file_))
        dict_comments = [i['snippet']['topLevelComment']['snippet']['textDisplay'] for i in self.r.json()['items']]
        return dict_comments


    def preprocessing(self, text):
        text = re.sub('<[^>]*>', '', text)
        emoticons = re.findall('(?::|;|=) (?:-)?(?:\)|\(|D|P)', text)
        self.text = re.sub('[\W]+', ' ', text.lower())+' '.join(emoticons).replace('-', '')
        pass
        # return self.text

    def tokenizer(self, text):
        self.stop_words()
        self.preprocessing(text=text)
        return [w for w in self.text.split() if w not in self.stop]

    def stop_words(self):
        # self.stop = stopwords.words('russian')
        self.stop = pickle.load(open(
                                    os.path.join(dir_name,
                                                 'movieclassifier/pkl_objects/stopwords.pkl'), 'rb'))


    def stream_docs(self):
        con = sqlite3.connect(os.path.join(dirname, 'db.sqlite3'))
        cursor = con.execute("""
                            SELECT *
                            FROM app_parsercomments
                            """)
        db = cursor.fetchall()
        con.close()
        for line in db:
            text, label = line[2], int(line[3])
            yield text, label


    def get_minibatch(self, size):
        docs, y = [], []
        a = self.stream_docs()
        try:
            for _ in range(size):
                text, label = next(a)
                self.preprocessing(text=text)
                docs.append(self.text)
                y.append(label)
        except StopIteration:
            return  None,  None
        return docs, y

    def classefier(self):
        self.vect = HashingVectorizer(decode_error='ignore',
                                 n_features=2**21,
                                 preprocessor=None,
                                 tokenizer=self.tokenizer)
        self.clf = SGDClassifier(loss='log', random_state=1, n_iter_no_change=1)

    def clf_score(self, minibatch = 10, cycle=10):
        pbar = pyprind.ProgBar(cycle)
        classes = np.array([0, 1])
        for _ in range(cycle):
            X_train, y_train = self.get_minibatch(size=minibatch)
            if not X_train:
                break
            X_train = self.vect.transform(X_train)
            self.clf.partial_fit(X_train, y_train, classes=classes)
            pbar.update()

    def pickle_dump_stop_clf(self):
        dest = os.path.join('movieclassifier', 'pkl_objects')
        if not os.path.exists(dest):
            os.makedirs(dest)
        pickle.dump(self.stop,
                    open(os.path.join(dest, 'stopwords.pkl'), 'wb'),
                    protocol=4)
        pickle.dump(self.clf,
                    open(os.path.join(dest, 'classifier.pkl'), 'wb'),
                    protocol=4)

        pass



def main():
    ml_helper = MlHelper()
    ml_helper.clf_score()
    # ml_helper.pickle_dump_stop_clf()




if __name__ == '__main__':
    main()



