import json

file = open('0000.dat',"r")

for line in file.readlines():
	obj = json.loads(line)
	print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t".format(obj['video_id'],obj['title'],obj['description'],obj['upload_time'],obj['length'],obj['view_counter'],obj['mylist_counter'],obj['comment_counter'],str(obj['tags'])))

