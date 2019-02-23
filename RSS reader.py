###################################
# Ronfort Théo, TS1               #
# Projet ISN                      # 
# Onglet "News" 3P                #
# RSS reader                      #
###################################

###################################
# Importation locale des fontions
import feedparser

###################################
# Corps du programme

NewsFeed = feedparser.parse("https://nyaa.si/?page=rss&u=zangafan")
print ('Number of RSS posts :', len(NewsFeed.entries))

entry = NewsFeed.entries[6]

print ('Post Title :',entry.title)
print (entry.published)
print ("******")
print (entry.summary)
print ("------News Link--------")
print (entry.link)

