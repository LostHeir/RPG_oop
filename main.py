from game_logic import GameLogic
from my_utilities import clear

game_over = False
current_enemy = None


if __name__ == '__main__':
    game = GameLogic(difficulty='easy')
    player = game.create_character(choice='none', name='LostHeir')

    while not game_over:
        if not current_enemy:
            clear()
            print('What would You like to do adventurer?\n'
                  '1 - I shall introduce myself.\n'
                  '2 - I will talk to someone.\n'
                  '3 - The whole city must be purged! (Spawns enemy..)')
            choice = int(input('--> '))
            if choice == 1:
                player.introduce()
            elif choice == 2:
                print(player.random_quote())
                input('Press any key to continue..')
            elif choice == 3:
                current_enemy = game.spawn_enemy()
            else:
                print('You really need to pick one of those options..')

        else:
            player.attack_enemy(current_enemy)
            current_enemy.attack_player(player=player)
            print(f'{player.name}: {player.hp}, {current_enemy.name}: {current_enemy.hp}')
            input()
            if player.hp <= 0:
                game_over = True
            elif current_enemy.hp <= 0:
                current_enemy = None

