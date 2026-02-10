class Project:
    def __init__(self, title, creator_name, location, comments):
        self.title = title
        self.creator_name = creator_name
        self.location = location
        self.comments = comments  # list of strings

    # Display creator name
    def display_creator(self):
        print(f"Creator Name: {self.creator_name}")

    # Display location
    def display_location(self):
        print(f"Location: {self.location}")

    # Display comments
    def display_comments(self):
        print("Comments:")
        for idx, comment in enumerate(self.comments, start=1):
            print(f"{idx}. {comment}")

    # Display all details
    def display_details(self):
        print(f"Project Title: {self.title}")
        self.display_creator()
        self.display_location()
        self.display_comments()


# Example usage
comments_list = [
    "Well structured code",
    "Easy to understand",
    "Needs more test cases"
]

project = Project(
    title="Assessment Task",
    creator_name="John Doe",
    location="New York",
    comments=comments_list
)

project.display_details()
