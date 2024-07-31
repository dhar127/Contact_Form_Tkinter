
from googleapiclient.discovery import build

# Set up the YouTube Data API client
api_key = 'AIzaSyCoE-1aUD_oiUfuK4nvPJg_bJCeoYf79r8'
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for videos
search_response = youtube.search().list(
    q='java',
    type='video',
    maxResults=50,
    part='snippet'
).execute()

# Extract video data
video_data = []
for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        video_id = search_result['id']['videoId']
        title = search_result['snippet']['title']
        published_at = search_result['snippet']['publishedAt']
        video_data.append([video_id, title, published_at])

# Calculate and store video ratings based on the ratio of views and likes
video_ratings = []

for video in video_data:
    try:
        video_stats = youtube.videos().list(
            part="statistics",
            id=video[0]
        ).execute()

        view_count = int(video_stats['items'][0]['statistics']['viewCount'])
        like_count = int(video_stats['items'][0]['statistics']['likeCount'])

        # Calculate the ratio of views to likes, you can use any ratio logic you prefer
        ratio = view_count / (like_count + 1)  # Add 1 to prevent division by zero

        # Use a custom rating logic based on the ratio (you can adjust this as needed)
        rating = min(5, max(1, int(5 * ratio)))

        video_ratings.append(rating)
    except Exception as e:
        print(f"Error fetching video statistics: {e}")
        video_ratings.append(0)  # Assign a default rating of 0 in case of an error

# Combine video data with ratings
videos_with_ratings = [(video_data[i], video_ratings[i]) for i in range(len(video_data))]

# Sort the videos based on ratings in descending order
videos_with_ratings.sort(key=lambda x: x[1], reverse=True)

# Display the top 50 videos with the highest ratings
top_50_videos = videos_with_ratings[:50]

for i, (video, rating) in enumerate(top_50_videos, start=1):
    video_id, title, published_at = video
    print(f"Video {i}:")
    print(f"  Video ID: {video_id}")
    print(f"  Title: {title}")
    print(f"  Published At: {published_at}")
    print(f"  Rating: {rating}\n")
