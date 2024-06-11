# Based on MBTI 16 personalities


# 1
def gather_storm():
    print("\nChapter 1: The Gathering Storm")
    print("1. Study ancient texts for clues about the enemy.")
    print("2. Train rigorously with weapons and spells.")
    print("3. Gather allies and form strategic alliances.")
    print("4. Meditate and seek visions of the future.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'N': 2, 'T': 2}
        elif choice == 2:
            return {'S': 2, 'J': 2}
        elif choice == 3:
            return {'E': 2, 'J': 2}
        elif choice == 4:
            return {'I': 2, 'N': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))
        
# 2
def journey_begins():
    print("\nChapter 2: The Journey Begins")
    print("1. Defend the villagers and drive off the goblins.")
    print("2. Create a diversion to allow the villagers to escape.")
    print("3. Negotiate with the goblin leader for a peaceful resolution.")
    print("4. Use magic to protect the village and its people.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'S': 2, 'J': 2}
        elif choice == 2:
            return {'N': 2, 'P': 2}
        elif choice == 3:
            return {'F': 2, 'E': 2}
        elif choice == 4:
            return {'N': 2, 'F': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))
            
# 3
def mysterious_forest():
    print("\nChapter 3: The Mysterious Forest")
    print("1. Guide the travelers to safety using your knowledge of the forest.")
    print("2. Set up camp and protect the travelers for the night.")
    print("3. Share stories and songs to lift the travelers' spirits.")
    print("4. Investigate the forest's secrets while ensuring the travelers are safe.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'S': 2, 'I': 2}
        elif choice == 2:
            return {'S': 2, 'J': 2}
        elif choice == 3:
            return {'E': 2, 'F': 2}
        elif choice == 4:
            return {'N': 2, 'T': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))

# 4
def ancient_ruins():
    print("\nChapter 4: The Ancient Ruins")
    print("1. Confront the beast head-on in a battle of strength.")
    print("2. Find a way to outsmart the beast and bypass it.")
    print("3. Attempt to communicate and understand the beast.")
    print("4. Search for hidden passages or clues to avoid the beast altogether.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'S': 2, 'T': 2}
        elif choice == 2:
            return {'N': 2, 'P': 2}
        elif choice == 3:
            return {'F': 2, 'N': 2}
        elif choice == 4:
            return {'T': 2, 'I': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))

# 5
def hidden_village():
    print("\nChapter 5: The Hidden Village")
    print("1. Earn their trust by helping with their tasks and protecting them.")
    print("2. Impress them with your skills and knowledge.")
    print("3. Charm them with stories and magic, gaining their favor.")
    print("4. Analyze their situation and offer strategic advice.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'F': 2, 'S': 2}
        elif choice == 2:
            return {'T': 2, 'J': 2}
        elif choice == 3:
            return {'E': 2, 'F': 2}
        elif choice == 4:
            return {'N': 2, 'T': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))

# 6
def final_battle():
    print("\nChapter 6: The Final Battle")
    print("1. Lead a direct assault on the enemy.")
    print("2. Use cunning tactics to outmaneuver the dark forces.")
    print("3. Inspire your allies with a rousing speech.")
    print("4. Utilize ancient magic to turn the tide of battle.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'J': 2, 'T': 2}
        elif choice == 2:
            return {'N': 2, 'P': 2}
        elif choice == 3:
            return {'E': 2, 'F': 2}
        elif choice == 4:
            return {'N': 2, 'T': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))

# 7
def aftermath():
    print("\nChapter 7: The Aftermath")
    print("1. Establish a new order, ensuring long-lasting peace and order.")
    print("2. Return to your studies, eager to learn from your experiences.")
    print("3. Travel the land, sharing your tales and inspiring others.")
    print("4. Continue to explore, seeking new adventures and mysteries.")
    choice = int(input("Choose an action (1-4): "))
    while True:
        if choice == 1:
            return {'J': 2, 'S': 2}
        elif choice == 2:
            return {'N': 2, 'I': 2}
        elif choice == 3:
            return {'E': 2, 'F': 2}
        elif choice == 4:
            return {'P': 2, 'N': 2}
        else:
            choice = int(input("Invalid choice.\nChoose an action (1-4): "))

def determine_personality(points):
    personality = ""
    personality += "I" if points.get('I', 0) > points.get('E', 0) else "E"
    personality += "N" if points.get('N', 0) > points.get('S', 0) else "S"
    personality += "T" if points.get('T', 0) > points.get('F', 0) else "F"
    personality += "J" if points.get('J', 0) > points.get('P', 0) else "P"
    return personality

def determine_role(personality):
    roles = {
        'INTJ': "Mastermind Sorcerer",
        'INTP': "Arcane Scholar",
        'ENTJ': "War General",
        'ENTP': "Charismatic Trickster",
        'INFJ': "Visionary Seer",
        'INFP': "Enchanted Bard",
        'ENFJ': "Noble Paladin",
        'ENFP': "Wandering Druid",
        'ISTJ': "Stalwart Knight",
        'ISFJ': "Guardian Healer",
        'ESTJ': "City Governor",
        'ESFJ': "Benevolent Matron/Patron",
        'ISTP': "Skilled Ranger",
        'ISFP': "Free-spirited Artisan",
        'ESTP': "Daring Mercenary",
        'ESFP': "Joyful Performer",
    }
    return roles.get(personality, "Unknown Role")

def main():
    points = {}
    
    chapters = [
        gather_storm,
        journey_begins,
        mysterious_forest,
        ancient_ruins,
        hidden_village,
        final_battle,
        aftermath
    ]
    
    for chapter in chapters:
        chapter_points = chapter()
        for trait, point in chapter_points.items():
            points[trait] = points.get(trait, 0) + point
    
    personality = determine_personality(points)
    role = determine_role(personality)
    
    print(f"\nYour personality type is: {personality}")
    print(f"Your fantasy role is: {role}")

if __name__ == "__main__":
    main()
