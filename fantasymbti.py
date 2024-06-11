# Based on MBTI 16 personalities

print("""
      
Evil is about to attack. The world is in danger.\nYou are chosen to lead the war against evil to save the world!

""")

# 1
def gather_storm():
    print("\nChapter 1: The Gathering Storm")
    print("Before you embark on your journey, decide how you want to prepare yourself:")
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
    print("Your preparations complete, you set out on your journey. Along the way, you encounter a village under attack by goblins. The villagers desperately need help! What do you do?")
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
    print("After crossing the village, you entered the mysterious forest full of dark mystical flora and fauna. Then you found a group of lost traveler. What do you do?")
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
    print("In the middle of the forest, there is an ancient ruins known to hold a legendary powerful artifact. But it is guarded by a dangerous anchestral beast. What do you do?")
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
    print("You acquired the artifact and exit the forest. Before approaching the entrance of the evil lair, there is villager in a small village that knows an important secret about the evil force. But they are weary and cautious around stranger. What do you do? ")
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
    print("The time has come to fight the evil force! What tactics are you going to use?")
    print("1. Lead a direct assault on the enemy.")
    print("2. Use cunning tactics to outmaneuver the dark forces.")
    print("3. Inspire your allies with a rousing speech. Increasing their morale.")
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
    print("Evil has been defeated, all the people in the world rejoice!! The King thanks you and granted you any support you need for your next endeavors. What should you do next? ")
    print("1. Establish a new order, ensuring long-lasting peace and order.")
    print("2. Return to your studies, eager to learn from your experiences. Nobody knows when the evil will come back someday.")
    print("3. Travel the land, sharing your tales and inspiring others. Giving hope to all corners of the world")
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
    
    print("\n\nYears gone and your victorious tale have been heard by people all over the world. The legend known as...")
    print("The {}".format(role))

    print("\n\nYour personality type is: {}".format(personality))
    print("Your fantasy role is: {}".format(role))

if __name__ == "__main__":
    main()
