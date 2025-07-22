# Existing usernames in the system
existing_usernames = {'amit', 'neha', 'ravi'}

# New signup attempt
new_username = input("Enter desired username: ").strip().lower()

# Check if the username already exists
if new_username in existing_usernames:
    print("Username already taken. Try another.")
else:
    existing_usernames.add(new_username)  # Add to set (hashed)
    print("Username created successfully.")
