#interesting_users.py

class User: 
    def __init__(self, user_id, age, gender, region):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.region = region
        self.authored_posts = []
        self.viewed_posts = []

    def is_interesting(self):
        return self.gender == "female" and self.region == "Oahu" and len(self.authored_posts) >= 4
    
    def total_activity(self):
        return len(self.authored_posts) + len(self.viewed_posts)
    
def get_interesting_users(users):
    return sorted(
        [u for u in users if u.is_interesting()],
        key=lambda u: u.total_activity(),
        reverse=True
    )

def print_interesting_users(users):
    for user in users:
        print(f"User ID: {user.user_id}")
        print(f"  Age: {user.age}")
        print(f"  Gender: {user.gender}")
        print(f"  Region: {user.region}")
        print(f"  Authored Posts: {len(user.authored_posts)}")
        print(f"  Viewed Posts: {len(user.viewed_posts)}")
        print(f"  Total Activity: {user.total_activity()}")
        print()
