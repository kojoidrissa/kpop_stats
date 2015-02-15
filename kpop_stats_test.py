import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:5]:
    view_count = int(video['yt$statistics']['viewCount']) #converts viewCount into an int
    print(video['title']['$t'], "with", '{:,}'.format(view_count), "views") #second 1/2 formats the int with thousands separators

'''This prints the dictionary for the first 'entry' in the 'feed' key
I need to figure out of processing these dicts with Python's JSON
module will make them easier to read, for a human (me).
Running the variable through the print function compresses it;
Just typing the variable name at the prompt produces something 
easier to read
'''
google_test = data['feed']['entry'][0]

# #This is the code I used to create the youTube_data.txt file
# '''print()
# print("NEW CODE STARTS HERE!!!")
# print('''This is showing me the results from the "data = response.json"; the type and length of each
#     element in "data['feed']['entry']" ''')
# #this shows me the various data catagories stored in each YouTube Entry listing
# f = open("youTube_data.txt", "a")

# for i in data['feed']['entry']:
#     # for key in i:
#     #     print (key, )
#     # print (i['yt$statistics']['viewCount'])
#     f.write(str(type(i)) + " " + str(len(i)) + " " + i['title']['$t'] + "\n" + str(i) + "\n" + "\n")
#     print (len(i), i['title']['$t'])
# #Looks like I'm after ['title']['$t'] and ['yt$statistics']
# '''
# f.close()

# for i in data['feed']['entry']:
#     print (type(i), len(i))
#     # print (i['yt$statistics']['viewCount'])
#     print (i['title']['$t'])
# #Looks like I'm after ['title']['$t'] and ['yt$statistics']