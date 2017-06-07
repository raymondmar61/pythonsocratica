#a standard data structure is an array or a map.  In Python, it's called a dictionary.  Dictionaries key value pairs of data; an input mapped to an output.  In Python, inputs are keys and outputs are values.

#FriendFace post
#user_id = 209
#message = "D5 E5 C5 C4 G4"
#language = "English"
#datetime = "20230215T124231Z"
#location = (44.590533, -104.715556)

post = {"user_id":209, "message": "D5 E5 C5 C4 G4", "language": "English", "datetime": "20230215T124231Z", "location":(44.590533, -104.715556)}
print(post)
print(type(post))
print(post["message"])
post2 = {"message": "SS Cotopaxi", "language": "English"}
print(post2)
post2["user_id"] = 209
post2["datetime"] = "199771116T0931Z"
print(post2) #returned post2 dictionary with user_id and datetime added

#get() method for lists
print(post2.get("Location","If there is no location, print value wrote here."))
mess = post2.get("message","There is no message.")
print(mess)
print("\n")

post = {"user_id":209, "message": "D5 E5 C5 C4 G4", "language": "English", "datetime": "20230215T124231Z", "location":(44.590533, -104.715556)}
for eachkey in post.keys():
	value = post[eachkey]
	print(eachkey, "=", value)
for key, value in post.items(): #use items() method to get key and value.  Another way.
	print(key, "=", value)

#pop and popitem methods removes an individual dictionary  Clear method removes all data in a dictionary.