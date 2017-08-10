class Movie():
    '''Class Movie.
       To create instance of a Movie, just call Movie() and pass:
       1. title of movie
       2. trailer url on youtube
       3. poster image url
    '''
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        # constructor of Movie class
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url