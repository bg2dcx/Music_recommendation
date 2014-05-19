import sys

f = open('kaggle_visible_evaluation_triplets.txt','r')
song_to_count = dict()
for line in f:
	_, song, _ = line.strip().split('\t')
	if song in song_to_count:
		song_to_count[song] += 1
	else:
		song_to_count[song] = 1

songs_ordered = sorted(song_to_count.keys(),
						key = lambda s: song_to_count[s],
						reverse  = True)

user_to_songs = dict()
for line in f:
	user,song,_ = line.strip().split('\t')
	if user in user_to_songs:
		user_to_songs[user].add(song)
	else:
		user_to_songs[user] = set([song])

f.close()







f2 = open('kaggle_users.txt','r')
canonical_users = map(lambda line:line.strip(),
					  f2.readlines())
f2.close()


f3 = open('kaggle_songs.txt','r')
song_to_index = dict(map (lambda line: 
							line.strip().split(' '),
							f3.readlines()))
f3.close()

f = open('submission.txt','w');
for user in canonical_users:
	print "user is "+user
	songs_to_recommend = []
	for song in songs_ordered:
		if len(songs_to_recommend) >=500:
			break
		print "song is  "+song	
		if not song in user_to_songs[user]:
			songs_to_recommend.append(song)
	indices = map(lambda s:song_to_index[s],
					songs_to_recommend)
	f.write(' '.join(indices)+'\n')
f.close()





