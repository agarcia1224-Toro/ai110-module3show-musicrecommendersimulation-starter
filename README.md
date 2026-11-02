# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music recommenders can combine song descriptions with listening history, skips, saves, and patterns from similar listeners. This simulation uses a small content-based approach: it compares a listener's stated preferences with each song's tags and numeric audio features. It does not learn from listening behavior, so its recommendations reflect only the profile and the features in this small catalog.

**Features used in the simulation**

- `Song`: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `valence`. The CSV also has `tempo_bpm`, `danceability`, and `acousticness`, available for future scoring improvements.
- `UserProfile` (dictionary): `favorite_genre`, `favorite_mood`, `target_energy`, and `target_valence`. For example: `{"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.90, "target_valence": 0.50}`. The numeric targets use the same 0–1 scale as the song data.

**Algorithm recipe**

For each song, add 2 points for a genre match and 1 point for a mood match. Add up to 1 point each for energy and valence similarity, calculated as `1 − |song value − target value|`. This rewards closeness rather than treating a higher value as automatically better. Score every song in the CSV independently, sort by score from highest to lowest, and return the top K songs. Scoring measures how well one candidate fits; ranking compares candidates and orders the list. With the example rock/intense profile, both intense rock songs can score well, while their energy and valence still help distinguish them from one another.

**Data flow:** User preferences → loop over CSV songs and calculate each score → sort scores → return top K recommendations.

**Potential bias:** Genre receives twice the weight of mood, so the system may favor a genre match over a song with a stronger mood and audio-feature fit. Exact tag matching can also miss songs that feel similar but use different labels.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

For the default pop/happy profile (target energy 0.8 and valence 0.8):

```
Loaded songs: 17

Top recommendations:

1. Sunrise City - Neon Echo (Score: 4.94)
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+0.98); valence similarity (+0.96)

2. Gym Hero - Max Pulse (Score: 3.84)
   Reasons: genre match (+2.0); energy similarity (+0.87); valence similarity (+0.97)

3. Rooftop Lights - Indigo Parade (Score: 2.95)
   Reasons: mood match (+1.0); energy similarity (+0.96); valence similarity (+0.99)

4. Velvet Groove - The Pocket (Score: 1.91)
   Reasons: energy similarity (+0.92); valence similarity (+0.99)

5. Corner Cypher - Northbound (Score: 1.90)
   Reasons: energy similarity (+0.98); valence similarity (+0.92)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



