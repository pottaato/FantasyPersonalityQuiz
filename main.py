# DRAFT: 2024/6/6

def determine_archetype(answers):
    # Each answer is a letter 'A', 'B', 'C', or 'D' corresponding to the questions 1 through 7.
    q1, q2, q3, q4, q5, q6, q7 = answers

    # Initialize counters for each archetype
    archetypes = {
        "Brave Knight": 0,
        "Cunning Thief": 0,
        "Wise Sage": 0,
        "Mysterious Sorcerer": 0,
        "Joyful Bard": 0,
        "Fierce Warrior": 0,
        "Noble Prince/Princess": 0,
        "Shadowy Assassin": 0,
        "Devoted Healer": 0,
        "Silent Ranger": 0,
        "Fearless Explorer": 0,
        "Enigmatic Seer": 0,
        "Gentle Giant": 0,
        "Faithful Squire": 0,
        "Benevolent Queen/King": 0,
        "Enchanting Enchanter/Enchantress": 0,
        "Stoic Blacksmith": 0,
        "Visionary Alchemist": 0,
        "Gentle Herbalist": 0,
        "Reclusive Hermit": 0,
        "Valiant Paladin": 0,
        "Curious Scholar": 0,
        "Mystic Druid": 0,
    }

    # Scenario 1: The Call to Adventure
    if q1 == 'A':
        archetypes["Joyful Bard"] += 1
        archetypes["Noble Prince/Princess"] += 1
    elif q1 == 'B':
        archetypes["Cunning Thief"] += 1
        archetypes["Shadowy Assassin"] += 1
    elif q1 == 'C':
        archetypes["Wise Sage"] += 1
        archetypes["Devoted Healer"] += 1
    elif q1 == 'D':
        archetypes["Silent Ranger"] += 1
        archetypes["Reclusive Hermit"] += 1

    # Scenario 2: The Mysterious Cave
    if q2 == 'A':
        archetypes["Fearless Explorer"] += 1
        archetypes["Brave Knight"] += 1
    elif q2 == 'B':
        archetypes["Mysterious Sorcerer"] += 1
        archetypes["Fierce Warrior"] += 1
    elif q2 == 'C':
        archetypes["Cunning Thief"] += 1
        archetypes["Shadowy Assassin"] += 1
    elif q2 == 'D':
        archetypes["Visionary Alchemist"] += 1
        archetypes["Curious Scholar"] += 1

    # Scenario 3: The Enchanted Garden
    if q3 == 'A':
        archetypes["Gentle Herbalist"] += 1
        archetypes["Devoted Healer"] += 1
    elif q3 == 'B':
        archetypes["Wise Sage"] += 1
        archetypes["Curious Scholar"] += 1
    elif q3 == 'C':
        archetypes["Mystic Druid"] += 1
        archetypes["Enigmatic Seer"] += 1
    elif q3 == 'D':
        archetypes["Valiant Paladin"] += 1
        archetypes["Brave Knight"] += 1

    # Scenario 4: The Ruined Castle
    if q4 == 'A':
        archetypes["Reclusive Hermit"] += 1
        archetypes["Wise Sage"] += 1
    elif q4 == 'B':
        archetypes["Mysterious Sorcerer"] += 1
        archetypes["Cunning Thief"] += 1
    elif q4 == 'C':
        archetypes["Stoic Blacksmith"] += 1
        archetypes["Benevolent Queen/King"] += 1
    elif q4 == 'D':
        archetypes["Joyful Bard"] += 1
        archetypes["Enchanting Enchanter/Enchantress"] += 1

    # Scenario 5: The Sacred Spring
    if q5 == 'A':
        archetypes["Brave Knight"] += 1
        archetypes["Valiant Paladin"] += 1
    elif q5 == 'B':
        archetypes["Cunning Thief"] += 1
        archetypes["Shadowy Assassin"] += 1
    elif q5 == 'C':
        archetypes["Wise Sage"] += 1
        archetypes["Visionary Alchemist"] += 1
    elif q5 == 'D':
        archetypes["Joyful Bard"] += 1
        archetypes["Enchanting Enchanter/Enchantress"] += 1

    # Scenario 6: The Bandit Ambush
    if q6 == 'A':
        archetypes["Fierce Warrior"] += 1
        archetypes["Brave Knight"] += 1
    elif q6 == 'B':
        archetypes["Cunning Thief"] += 1
        archetypes["Shadowy Assassin"] += 1
    elif q6 == 'C':
        archetypes["Noble Prince/Princess"] += 1
        archetypes["Benevolent Queen/King"] += 1
    elif q6 == 'D':
        archetypes["Joyful Bard"] += 1
        archetypes["Mischievous Trickster"] += 1

    # Scenario 7: The Final Revelation
    if q7 == 'A':
        archetypes["Brave Knight"] += 1
        archetypes["Fierce Warrior"] += 1
    elif q7 == 'B':
        archetypes["Wise Sage"] += 1
        archetypes["Visionary Alchemist"] += 1
    elif q7 == 'C':
        archetypes["Devoted Healer"] += 1
        archetypes["Gentle Herbalist"] += 1
    elif q7 == 'D':
        archetypes["Joyful Bard"] += 1
        archetypes["Enchanting Enchanter/Enchantress"] += 1

    # Determine the highest scoring archetype
    final_archetype = max(archetypes, key=archetypes.get)
    return final_archetype


# Example of determining the archetype based on user answers
user_answers = ['A', 'B', 'C', 'D', 'A', 'B', 'C']  # Example answers
print(f"Your archetype is: {determine_archetype(user_answers)}")
