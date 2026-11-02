"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.90, "valence": 0.85}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.35, "valence": 0.60}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.95, "valence": 0.40}),
        ("Conflicting Lofi / Sad / High Energy", {"genre": "lofi", "mood": "sad", "energy": 0.90, "valence": 0.10}),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{profile_name} - Top recommendations:\n")
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{rank}. {song['title']} - {song['artist']} (Score: {score:.2f})")
            print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
