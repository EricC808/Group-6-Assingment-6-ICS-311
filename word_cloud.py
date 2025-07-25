from typing import List, Dict

# Define a structure for each post
class Post:
    def __init__(self, content: str, user: Dict):
        self.content = content
        self.user = user  # e.g., {'age': 20, 'gender': 'female', 'region': 'Oahu'}

# Function to filter posts based on keywords and optional user attributes
def filter_posts(posts: List[Post], keywords: List[str], attribute_filters: Dict = {}) -> List[Post]:
    filtered = []

    for post in posts:
        # Check if the content contains any of the keywords
        if any(keyword.lower() in post.content.lower() for keyword in keywords):
            match = True

            # Check for user attribute filters (e.g., gender="female")
            for attr, value in attribute_filters.items():
                if post.user.get(attr) != value:
                    match = False
                    break

            if match:
                filtered.append(post)

    return filtered

# Function to generate a word frequency dictionary from a list of posts
def generate_word_cloud_data(posts: List[Post]) -> Dict[str, int]:
    word_freq = {}

    for post in posts:
        # Basic tokenization: split by whitespace
        words = post.content.lower().split()

        for word in words:
            # Clean punctuation (optional, basic version)
            word = word.strip(".,!?\"'()[]{}")

            if word:
                word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_posts = [
        Post("This is a great day!", {"age": 20, "gender": "female", "region": "Oahu"}),
        Post("Totally awesome concert last night.", {"age": 22, "gender": "female", "region": "Maui"}),
        Post("This sucks...", {"age": 21, "gender": "male", "region": "Oahu"})
    ]

    keywords = ["great", "awesome", "sucks"]
    filters = {"gender": "female"}

    # Filter posts
    relevant = filter_posts(sample_posts, keywords, filters)

    # Generate word cloud data
    word_cloud = generate_word_cloud_data(relevant)

    # Display results
    print(word_cloud)
