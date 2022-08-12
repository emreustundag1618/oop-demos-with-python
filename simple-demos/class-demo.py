class Comment:
    
    def __init__(self, username, text, likes = 0, dislikes = 0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        
comm1 = Comment("Emre Üstündağ","That's really nice")
comm2 = Comment("Emily Croft","You're awesome, I liked it!", 5, 7)

comments = [comm1, comm2]

for comm in comments:
    print("Username: " + comm.username)
    print("Comment text: " + comm.text)
    print("Likes: " + str(comm.likes))
    print("Dislike: " + str(comm.dislikes))
    print("************")