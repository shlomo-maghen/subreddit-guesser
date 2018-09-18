import os, praw, csv

def main():
	"""
	Use praw to write a csv containing titles from top 100 subreddits
	"""
	# open csv for writing
	csv_file = open("./titles.csv", 'w+')
	csv_writer = csv.writer(csv_file)

	# write headers
	csv_writer.writerow(["subreddit", "title"])

	# initialize praw
	praw = initialize_praw()

	# get a list of subreddit names to get titles from
	subreddit_names = get_subreddit_names()
	
	# get top 1000 posts of all times for each sub (takes a while)
	for subreddit_name in subreddit_names:
		subreddit = praw.subreddit(subreddit_name)
		submissions = subreddit.top('all', limit=1000)

		print("writing %s" % (subreddit_name))
		for submission in submissions:
			csv_writer.writerow([subreddit_name, submission.title])

	csv_file.close()


def get_subreddit_names():
	"""
	The top subreddits according to http://redditmetrics.com/top
	"""
	return [
		"announcements",
		"funny",
		"AskReddit",
		"todayilearned",
		"science",
		"worldnews",
		"pics",
		"IAmA",
		"gaming",
		"videos",
		"movies",
		"aww",
		"Music",
		"blog",
		"gifs",
		"news",
		"explainlikeimfive",
		"askscience",
		"EarthPorn",
		"books",
		"television",
		"mildlyinteresting",
		"LifeProTips",
		"Showerthoughts",
		"space",
		"DIY",
		"Jokes",
		"gadgets",
		"nottheonion",
		"sports",
		"tifu",
		"food",
		"photoshopbattles",
		"Documentaries",
		"Futurology",
		"history",
		"InternetIsBeautiful",
		"dataisbeautiful",
		"UpliftingNews",
		"listentothis",
		"GetMotivated",
		"personalfinance",
		"OldSchoolCool",
		"philosophy",
		"Art",
		"nosleep",
		"WritingPrompts",
		"creepy",
		"TwoXChromosomes",
		"Fitness",
		"technology",
		"WTF",
		"bestof",
		"AdviceAnimals",
		"politics",
		"atheism",
		"interestingasfuck",
		"europe",
		"woahdude",
		"BlackPeopleTwitter",
		"oddlysatisfying",
		"gonewild",
		"leagueoflegends",
		"pcmasterrace",
		"reactiongifs",
		"gameofthrones",
		"wholesomememes",
		"Unexpected",
		"Overwatch",
		"facepalm",
		"trees",
		"Android",
		"lifehacks",
		"me_irl",
		"relationships",
		"Games",
		"nba",
		"programming",
		"tattoos",
		"NatureIsFuckingLit",
		"Whatcouldgowrong",
		"CrappyDesign",
		"dankmemes",
		"nsfw",
		"cringepics",
		"4chan",
		"soccer",
		"comics",
		"sex",
		"pokemon",
		"malefashionadvice",
		"NSFW_GIF",
		"StarWars",
		"Frugal",
		"HistoryPorn",
		"AnimalsBeingJerks",
		"RealGirls",
		"travel",
		"buildapc",
		"OutOfTheLoop",
	]


def initialize_praw():
	"""
	Initialize and return a praw object
	"""
	return praw.Reddit(
		client_id=os.environ["REDDIT_CLIENT"],
		client_secret=os.environ["REDDIT_SECRET"],
		username=os.environ["REDDIT_USER"],
		password=os.environ["REDDIT_PASS"],
		user_agent='Subreddit-Guesser python script'
	)


if __name__ == "__main__":
	main()