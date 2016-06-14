VALID_GENRES = ("Romance", "Action", "?")

class movie:
    def __init__(self, title, kisses, kicks, genre):
        self.title = title
        self.kisses = kisses
        self.kicks = kicks
        if genre not in VALID_GENRES:
            raise ValueError("Invalid genre! ('" + genre + "')")
        else:
            self.genre = genre

    def __repr__(self):
        return "[Movie] : title='{}'; #kisses={}; #kicks={}, genre='{}'".format(self.title, self.kisses, self.kicks, self.genre)
