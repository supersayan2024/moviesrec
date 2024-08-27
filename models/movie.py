class Movie:
    def __init__(self, name: str, duration: int, description: str):
        self.name = name
        self.duration = duration
        self.description = description
        self.categories = []
        self.actors = []

    def add_category(self, category):
        self.categories.append(category)

    def add_actor(self, actor):
        self.actors.append(actor)

    def __str__(self):
        return f"{self.name} ({self.duration} mins)"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Duration: {self.duration} mins")
        print(f"Description: {self.description}")
        print(f"Categories: {', '.join([str(category) for category in self.categories])}")
        print(f"Actors: {', '.join([str(actor) for actor in self.actors])}")
fafa = Movie("undisputed", 2, "C'est un film de combat")

fafa.add_category("drama")
fafa.add_actor("alain")
fafa.display_info()