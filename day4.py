# Create object
insta = InstagramAccount("bhuvana_official", "insta123")

# Add private reels
insta.add_private_reel("Vacation Reel")
insta.add_private_reel("Birthday Reel")

# Add archived reels
insta.add_archived_reel("Old Memories")
insta.add_archived_reel("College Days")

print("\n--- Private Reels as Follower ---")
insta.display_private_reels(True)

print("\n--- Private Reels as Non-Follower ---")
insta.display_private_reels(False)

print("\n--- Archived Reels (Correct Password) ---")
insta.display_archived_reels("insta123")

print("\n--- Archived Reels (Wrong Password) ---")
insta.display_archived_reels("wrongpass")

print("\n--- Update Password ---")
insta.set_password("insta123", "newpass123")

print("\n--- Archived Reels After Password Update ---")
insta.display_archived_reels("newpass123")