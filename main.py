# main.py

from shortest_path import shortest_path_group1
from trendPosts import Post, filter_posts, get_trending_posts, compute_trending_score #Katelyn's portion
from datetime import datetime, timedelta


def main():
    # Create a graph for testing (replace with your graph format)
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('C', 1), ('D', 7)],
        'C': [('A', 4), ('B', 1), ('D', 3)],
        'D': [('B', 7), ('C', 3)]
    }

    print("=== Group 1: Shortest Path ===")
    start_node = 'A'
    end_node = 'D'
    path, cost = shortest_path_group1(graph, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {path}, cost: {cost}")
    print()

    print("=== Group 2: Interesting Users ===")
    # TODO: Call Group 2’s function here
    # Example: result = group2_function(graph)
    user_A = User("user_A", age=22, gender="female", region="Oahu")
    user_B = User("user_B", age=19, gender="female", region="Oahu")
    user_C = User("user_C", age=31, gender="female", region="Maui")
    user_D = User("user_D", age=26, gender="male", region="Oahu")
    user_E = User("user_E", age=21, gender="female", region="Oahu")
    user_F = User("user_F", age=24, gender="female", region="Oahu")

    users = [user_A, user_B, user_C, user_D, user_E, user_F]

    # Posts
    user_A.authored_posts += ["Day at the beach", "Uni life", "GRWM", "OOTD", "Travel"]
    user_F.authored_posts += ["Skull Panda Unboxing", "Formula 1", "Mukbang", "Dubai Chocolate"]
    user_B.authored_posts += ["Bird watching"]

    # Views
    user_F.viewed_posts += ["Day at the beach", "Bird watching"]
    user_A.viewed_posts += ["Bird watching"]
    user_B.viewed_posts += ["Day at the Beach"]

    # Output
    interesting_users = get_interesting_users(users)
    print_interesting_users(interesting_users)
    print()

    print("=== Group 3: Trending Posts ===")
    now = datetime.now()

    # ex trend posts
    posts = [
        Post(1, "Dubai Chocolate!", {"age": 22, "gender": "female", "region": "Oahu"}, now - timedelta(hours=1), likes=50, comments=10),
        Post(2, "Worst experience ever.", {"age": 22, "gender": "male", "region": "Oahu"}, now - timedelta(hours=2), likes=30, comments=15),
        Post(3, "Matcha Latte", {"age": 25, "gender": "female", "region": "Maui"}, now - timedelta(hours=0.5), likes=20, comments=5),
        Post(4, "I hate Labubus", {"age": 20, "gender": "female", "region": "Oahu"}, now - timedelta(hours=0.25), likes=10, comments=2)
    ]

    include_keywords = ["Matcha", "Dubai", "Worst"]
    exclude_keywords = ["hate"]
    user_filters = {"gender": "female", "region": "Oahu"}

    filtered_posts = filter_posts(posts, include_keywords, exclude_keywords, user_filters)
    trending = get_trending_posts(filtered_posts, now)

    for p in trending:
        score = compute_trending_score(p, now)
        print(f"Post ID: {p.post_id} | Score: {score:.2f} | Content: \"{p.content}\"")
    print()


if __name__ == "__main__":
    main()
