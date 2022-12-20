class Video:

    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()

v1 = Video()
v2 = Video()
v1.create('Python')
v2.create('Python ООП')
[YouTube.add_video(x) for x in [v1, v2]]
[YouTube.play(x) for x in range(len(YouTube.videos))]
