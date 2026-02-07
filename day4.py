class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password          # private variable
        self.private_reels = []
        self.archived_reels = []

    # Add private reel
    def add_private_reel(self, reel):
        self.private_reels.append(reel)

    # Add archived reel
    def add_archived_reel(self, reel):
        self.archived_reels.append(reel)

    # Display private reels (only for followers)
    def display_private_reels(self, is_follower):
        if is_follower:
            for reel in self.private_reels:
                print(reel)
        else:
            print("Follow to see private reels.")

    # Display archived reels (password protected)
    def display_archived_reels(self, password):
        if password == self.__password:
            for reel in self.archived_reels:
                print(reel)
        else:
            print("Incorrect password! Cannot access archived reels.")

    # Update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Old password is incorrect.")
