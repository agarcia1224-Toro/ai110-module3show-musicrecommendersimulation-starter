# VibeFinder 1.0 Model Card

## 1. Model Name

**VibeFinder 1.0**

## 2. Goal / Task

VibeFinder ranks songs that may fit a listener's stated genre, mood, energy, and valence preferences. It returns the five highest-scoring songs with short explanations.

## 3. Data Used

The catalog has 17 songs. Each row has genre, mood, energy, tempo, valence, danceability, and acousticness, plus song and artist names. The current scoring uses genre, mood, energy, and valence. The catalog is small and made for this classroom project, so many sounds and moods are missing.

## 4. Algorithm Summary

A matching genre adds 1 point, and a matching mood adds 1 point. Energy closeness adds up to 2 points, and valence closeness adds up to 1 point. Closer values earn more points. The system scores every song, sorts them, and returns the top five.

## 5. Observed Behavior / Biases

The chill lofi profile ranked “Library Rain” and “Midnight Coding” first. The intense rock profile ranked “Storm Runner” first. The conflicting lofi, sad, high-energy profile had no sad song to match, so high-energy rock rose to the top after energy received more weight. Exact labels and the small catalog limit what the system can recommend.

## 6. Evaluation Process

I compared High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Lofi / Sad / High Energy profiles. I also halved the genre weight and doubled the energy weight. The top results stayed similar for the first three profiles, but the conflicting profile changed from lofi songs leading to high-energy rock leading.

Pair comparisons:

- High-Energy Pop vs. Chill Lofi: pop and happy songs lead one list; chill lofi songs lead the other.
- High-Energy Pop vs. Deep Intense Rock: “Sunrise City” leads pop; “Storm Runner” leads rock.
- High-Energy Pop vs. the conflicting profile: pop and happy preferences work directly, while the missing sad label leaves the other profile relying on its numeric targets.
- Chill Lofi vs. Deep Intense Rock: low-energy chill songs lead one; high-energy intense songs lead the other.
- Chill Lofi vs. the conflicting profile: lofi leads when the target is calm, but high-energy rock rises when the target energy is high.
- Deep Intense Rock vs. the conflicting profile: both can favor intense rock, but only the deep rock profile also matches the rock genre.

### Captured Terminal Recommendations

#### High-Energy Pop

```
High-Energy Pop - Top recommendations:

1. Sunrise City - Neon Echo (Score: 4.83)
   Reasons: genre match (+1.0); mood match (+1.0); energy similarity (+1.84); valence similarity (+0.99)
2. Gym Hero - Max Pulse (Score: 3.86)
   Reasons: genre match (+1.0); energy similarity (+1.94); valence similarity (+0.92)
3. Rooftop Lights - Indigo Parade (Score: 3.68)
   Reasons: mood match (+1.0); energy similarity (+1.72); valence similarity (+0.96)
4. Desert Bloom - Sola Luna (Score: 2.87)
   Reasons: energy similarity (+1.90); valence similarity (+0.97)
5. Corner Cypher - Northbound (Score: 2.63)
   Reasons: energy similarity (+1.76); valence similarity (+0.87)
```

#### Chill Lofi

```
Chill Lofi - Top recommendations:

1. Library Rain - Paper Lanterns (Score: 5.00)
   Reasons: genre match (+1.0); mood match (+1.0); energy similarity (+2.00); valence similarity (+1.00)
2. Midnight Coding - LoRoom (Score: 4.82)
   Reasons: genre match (+1.0); mood match (+1.0); energy similarity (+1.86); valence similarity (+0.96)
3. Focus Flow - LoRoom (Score: 3.89)
   Reasons: genre match (+1.0); energy similarity (+1.90); valence similarity (+0.99)
4. Spacewalk Thoughts - Orbit Bloom (Score: 3.81)
   Reasons: mood match (+1.0); energy similarity (+1.86); valence similarity (+0.95)
5. Coffee Shop Stories - Slow Stereo (Score: 2.85)
   Reasons: energy similarity (+1.96); valence similarity (+0.89)
```

#### Deep Intense Rock

```
Deep Intense Rock - Top recommendations:

1. Storm Runner - Voltline (Score: 4.84)
   Reasons: genre match (+1.0); mood match (+1.0); energy similarity (+1.92); valence similarity (+0.92)
2. Iron Horizon - Black Anvil (Score: 3.94)
   Reasons: mood match (+1.0); energy similarity (+1.98); valence similarity (+0.96)
3. Gym Hero - Max Pulse (Score: 3.59)
   Reasons: mood match (+1.0); energy similarity (+1.96); valence similarity (+0.63)
4. Night Drive Loop - Neon Echo (Score: 2.51)
   Reasons: energy similarity (+1.60); valence similarity (+0.91)
5. Corner Cypher - Northbound (Score: 2.34)
   Reasons: energy similarity (+1.66); valence similarity (+0.68)
```

#### Conflicting Lofi / Sad / High Energy

```
Conflicting Lofi / Sad / High Energy - Top recommendations:

1. Iron Horizon - Black Anvil (Score: 2.62)
   Reasons: energy similarity (+1.88); valence similarity (+0.74)
2. Storm Runner - Voltline (Score: 2.60)
   Reasons: energy similarity (+1.98); valence similarity (+0.62)
3. Midnight Coding - LoRoom (Score: 2.58)
   Reasons: genre match (+1.0); energy similarity (+1.04); valence similarity (+0.54)
4. Focus Flow - LoRoom (Score: 2.51)
   Reasons: genre match (+1.0); energy similarity (+1.00); valence similarity (+0.51)
5. Library Rain - Paper Lanterns (Score: 2.40)
   Reasons: genre match (+1.0); energy similarity (+0.90); valence similarity (+0.50)
```

## 7. Intended Use and Non-Intended Use

This project is for learning how a simple recommendation score works. It is not a production music service. It should not be treated as a reliable measure of a person's taste or used to make decisions about people.

## 8. Ideas for Improvement

- Add more songs and more mood labels.
- Let users set feature weights or mark recommendations as good or bad.
- Use tempo, danceability, and acousticness, and add a rule to encourage variety.

## Personal Reflection

My biggest learning moment was seeing the conflicting profile change when I changed the weights. A simple formula can feel like a real recommendation because its ranked results reflect recognizable preferences. AI helped me implement the loader, scoring, and ranking, but I checked the CLI output and calculations because the starter import failed and the requested weight change could alter the results. I was surprised that one weight shift changed the edge case more than the ordinary profiles. Next, I would add more songs and let listeners adjust weights and give feedback.
