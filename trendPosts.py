from typing import List, Dict
from datetime import datetime, timedelta

# Data class for a post
class Post:
    def __init__(self, post_id: int, content: str, user: Dict, timestamp: datetime, likes: int, comments: int):
        self.post_id = post_id
        self.content = content
        self.user = user  # e.g., {'age': 25, 'gender': 'female', 'region': 'Oahu'}
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments

# Filter posts keyword and user attributes
def filter_posts(posts: List[Post], include_keywords: List[str], exclude_keywords: List[str], user_filters: Dict) -> List[Post]:
    filtered = []
    for post in posts:
        text = post.content.lower()

        if include_keywords and not any(kw.lower() in text for kw in include_keywords):
            continue
        if exclude_keywords and any(kw.lower() in text for kw in exclude_keywords):
            continue

        if any(post.user.get(attr) != val for attr, val in user_filters.items()):
            continue

        filtered.append(post)
    return filtered

# Trending score calc
def compute_trending_score(post: Post, current_time: datetime) -> float:
    age_in_hours = max((current_time - post.timestamp).total_seconds() / 3600, 1)
    score = (post.likes + 2 * post.comments) / age_in_hours
    return score

# Find top trending posts
def get_trending_posts(posts: List[Post], current_time: datetime, top_n: int = 5) -> List[Post]:
    scored_posts = [(post, compute_trending_score(post, current_time)) for post in posts]
    scored_posts.sort(key=lambda x: x[1], reverse=True)
    return [post for post, _ in scored_posts[:top_n]]

# Testing data
if __name__ == "__main__":
    now = datetime.now()
    posts = [
        Post(1, "Dubai Chocolate!", {"age": 22, "gender": "female", "region": "Oahu"}, now - timedelta(hours=1), likes=50, comments=10),
        Post(2, "I hate.", {"age": 22, "gender": "male", "region": "Oahu"}, now - timedelta(hours=2), likes=30, comments=15),
        Post(3, "Matcha Latte", {"age": 25, "gender": "female", "region": "Maui"}, now - timedelta(hours=0.5), likes=20, comments=5),
        Post(4, "Things to do in Japan", {"age": 20, "gender": "female", "region": "Japan"}, now - timedelta(hours=0.25), likes=10, comments=2)
    ]

    include_keywords = ["Dubai", "Matcha", "Japan"]
    exclude_keywords = ["hate"]
    user_filters = {"gender": "female", "region": "Oahu"}

    # Apply filters
    filtered_posts = filter_posts(posts, include_keywords, exclude_keywords, user_filters)

    # Get trending
    trending = get_trending_posts(filtered_posts, now)

    print("Top Trending Posts:")
    for p in trending:
        print(f"Post ID: {p.post_id} | Score: {compute_trending_score(p, now):.2f} | Content: {p.content}")
