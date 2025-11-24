import random
import webbrowser

# Mood → list of song titles (you can extend these)
mood_songs = {
    "happy": [
        "Happy - Pharrell Williams",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Can't Stop the Feeling! - Justin Timberlake",
    ],
    "sad": [
        "Someone Like You - Adele",
        "All of Me - John Legend (slow version)",
        "Tears in Heaven - Eric Clapton",
    ],
    "energetic": [
        "Eye of the Tiger - Survivor",
        "Can't Hold Us - Macklemore & Ryan Lewis",
        "Stronger - Kanye West",
    ],
    "chill romantic": [
        "Perfect - Ed Sheeran",
        "Shape of You (Acoustic) - Ed Sheeran",
        "Sunflower - Rex Orange County",
    ],
}

def get_youtube_url(song_title: str) -> str:
    """Build a YouTube search URL for the given song."""
    query = song_title.replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}"

def main():
    mood = input("How are you feeling today? (happy / sad / energetic / chill romantic): ").strip().lower()

    if mood not in mood_songs:
        print("Oops, I don't recognize that mood. Try one of the listed options.")
        return

    song = random.choice(mood_songs[mood])
    print(f"\nHow about listening to: '{song}'?")

    url = get_youtube_url(song)
    webbrowser.open(url)

if __name__ == "__main__":
    main()