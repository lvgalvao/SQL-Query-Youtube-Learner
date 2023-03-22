import google.auth
from googleapiclient.discovery import build
from config import API_KEY

def search_youtube(query_string, max_results=3):
    # Set up authentication and create the YouTube API client
    credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Execute the search
    search_response = youtube.search().list(
        q=query_string,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    # Extract the results
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            videos.append({
                'title': search_result['snippet']['title'],
                'video_url': video_url,
            })

    # Convert the results to a dictionary and return
    return {'videos': videos}