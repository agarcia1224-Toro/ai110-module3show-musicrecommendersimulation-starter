from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song rows from CSV and convert numeric columns to numbers."""
    numeric_converters = {
        "id": int,
        "tempo_bpm": int,
        "energy": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            for field, converter in numeric_converters.items():
                row[field] = converter(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song with match points and similarity rewards, returning reasons."""
    score = 0.0
    reasons = []

    if song["genre"].casefold() == user_prefs["genre"].casefold():
        score += 1.0
        reasons.append("genre match (+1.0)")
    if song["mood"].casefold() == user_prefs["mood"].casefold():
        score += 1.0
        reasons.append("mood match (+1.0)")

    if "energy" in user_prefs:
        energy_points = 2.0 * max(0.0, 1.0 - abs(song["energy"] - float(user_prefs["energy"])))
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")
    if "valence" in user_prefs:
        valence_points = max(0.0, 1.0 - abs(song["valence"] - float(user_prefs["valence"])))
        score += valence_points
        reasons.append(f"valence similarity (+{valence_points:.2f})")

    if not reasons:
        reasons.append("no matching preferences")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank by score, and return the top k with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))
    return sorted(scored_songs, key=lambda recommendation: recommendation[1], reverse=True)[:max(0, k)]
