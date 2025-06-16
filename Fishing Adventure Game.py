import random
import pandas as pd
import matplotlib.pyplot as plt

fishing_log = []

def choices(xp, money, level, rod):
    while xp >= 100:
        print('You\'ve leveled up to lvl ' + str(level + 1) + '!')
        level += int(xp / 100)
        xp %= 100
        print('Remaining xp to level up: ' + str(100 - xp) + ' xp')
        print('-------------------\n')

    print('What do you want to do?\n')
    print('1. Go fishing')
    print('2. Go to the store')
    print('3. Check your stats')
    print('4. Exit game\n')

    choice = input('> ')
    if choice == '1':
        xp, money, level = fishing(xp, money, level, rod)
        choices(xp, money, level, rod)
    elif choice == '2':
        money, rod = store(money, rod)
        choices(xp, money, level, rod)
    elif choice == '3':
        stats(xp, money, level, rod)
        choices(xp, money, level, rod)
    elif choice == '4':
        quit = input('Are you sure you want to quit? (yes/no) > ').lower()
        if quit == 'yes':
            save_and_visualize()
            print('Thanks for playing!')
        else:
            choices(xp, money, level, rod)
    else:
        print('Invalid choice. Try again.')
        choices(xp, money, level, rod)

def stats(xp, money, level, rod):
    print('-' * 36)
    print(' ' * 3 + 'YOUR STATS:')
    print(f'     XP: {xp}\n     Money: Rs.{money}\n     Level: {level}\n     Fishing rod: {rod}')
    print('-' * 36)

def fishing(xp, money, level, rod):
    fish_data = {
        1: ('Salmon', 5.0, 5.0),
        2: ('Trout', 4.0, 4.5),
        3: ('Bass', 3.5, 5.0),
        4: ('Catfish', 8.0, 7.0),
        5: ('Gold Fish', 10.0, 10.0),
        6: ('Nothing', 0.0, 0.0)
    }

    print('You start fishing...')
    print('.... ....... ...')

    fish = random.randint(1, 6)
    fish_name, fish_xp, fish_money = fish_data[fish]

    xp += fish_xp
    money += fish_money

    print(f'You caught a {fish_name}!   +{fish_xp} xp  +Rs.{fish_money}')
    if fish_name != 'Nothing':
        fishing_log.append({
            "Fish": fish_name,
            "XP Gained": fish_xp,
            "Money Gained": fish_money,
            "Rod Used": rod,
            "Level": level
        })

    if xp < 100:
        print('Remaining xp to level up: ' + str(100 - xp) + ' xp')
    print('-------------------\n')
    return xp, money, level

def store(money, rod):
    print('You go to the store.\n')
    options = {
        'BASIC Fishing Rod': [('AQUATIC Fishing Rod', 100), ('GOLD Fishing Rod', 500)],
        'AQUATIC Fishing Rod': [('GOLD Fishing Rod', 500)],
        'GOLD Fishing Rod': []
    }

    upgrades = options[rod]
    if not upgrades:
        print('No more upgrades available!\n')
        return money, rod

    for i, (item, cost) in enumerate(upgrades, start=1):
        print(f'{i}. {item} (Rs.{cost})')
    print(f'{len(upgrades) + 1}. Exit store\n')

    choice = input('> ')
    try:
        choice = int(choice)
        if 1 <= choice <= len(upgrades):
            item, cost = upgrades[choice - 1]
            if money >= cost:
                money -= cost
                rod = item
                print(f'You bought the {item}!\n')
            else:
                print('Not enough money!\n')
        else:
            print('Exiting store.\n')
    except:
        print('Invalid choice.\n')
    return money, rod

def save_and_visualize():
    if not fishing_log:
        print("No fishing data to save.")
        return
    df = pd.DataFrame(fishing_log)
    df.to_csv('fishing_log.csv', index=False)
    df.to_excel('fishing_log.xlsx', index=False)
    print('Game log saved as "fishing_log.csv" and "fishing_log.xlsx".')

    fish_counts = df['Fish'].value_counts()
    fish_counts.plot(kind='bar', color='orange')
    plt.title("Fish Caught Summary")
    plt.xlabel("Fish Type")
    plt.ylabel("Count")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Game starts
print('\n\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ')
print('          FISHING ADVENTURE')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n\n')

print('You\'ve just found a comfortable place for fishing.\n')
print('Level up and earn money by catching fish and visiting the store:\n')

print('-' * 18 + 'FISH:' + '-' * 18)
print('  1. SALMON      5.0 xp, Rs.5.0')
print('  2. TROUT       4.0 xp, Rs.4.5')
print('  3. BASS        3.5 xp, Rs.5.0')
print('  4. CATFISH     8.0 xp, Rs.7.0')
print('  5. GOLD FISH   10.0 xp, Rs.10.0')
print('-' * 36)

xp = 0
money = 0
level = 1
rod = 'BASIC Fishing Rod'

stats(xp, money, level, rod)
choices(xp, money, level, rod)