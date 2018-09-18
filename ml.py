import pandas as pd
import pickle
import sys, os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main():
	if len(sys.argv) < 2:
		print("need <train> or <predict>")
		exit()

	# train or predict
	action = sys.argv[1]
	if action == "train":
		train()
	elif action == "predict":
		if len(sys.argv) < 3:
			print("must pass title to predict")
			exit()
		
		predict(sys.argv[2])


def train():
	# read in csv data (subreddit, title)
	df = pd.read_csv("./titles.csv")

	# samples are titles, targets are subreddits
	X = df.title
	y = df.subreddit

	# split into train and test sets
	X_train, X_test, y_train, y_test = train_test_split(X, y)
	
	# run tfidf on the titles
	print("running tfidf")
	tfidf = TfidfVectorizer()
	tfidf.fit(X_train)
	X_train = tfidf.transform(X_train)
	X_test = tfidf.transform(X_test)

	# train a random forest
	print("training model")
	rf = RandomForestClassifier()
	rf.fit(X_train, y_train)
	
	# predict
	predictions = rf.predict(X_test)
	
	# print metrics
	accuracy = accuracy_score(y_test, predictions)
	print("accuracy is: %.4f" % accuracy)
	print(classification_report(y_test, predictions))

	# save tfidf and model to file
	file_path = os.path.realpath(__file__)
	directory = os.path.dirname(file_path)
	try:
		os.mkdir("%s/pickles" %directory)
	except OSError:
		print("something went wrong")
		exit()

	file = open("./pickles/tfidf.p", "wb")
	pickle.dump(tfidf, file)
	file.close()
	file = open("./pickles/rf.p", "wb")
	pickle.dump(rf, file)
	file.close()


def predict(title):
	print("predicting %s" % title)
	try: 
		file = open("./pickles/tfidf.p", "rb")
		tfidf = pickle.load(file)
		file = open("./pickles/rf.p", "rb")
		rf = pickle.load(file)
	except FileNotFoundError:
		print("must train first")
		exit()

	X = tfidf.transform([title])
	y = rf.predict(X)

	print("that belongs in r/%s" % y[0])


if __name__ == "__main__":
	main()