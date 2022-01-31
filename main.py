from game_logic import GameLogic
from my_utilities import clear

game_over = False
current_enemy = None
combat_state = False


if __name__ == '__main__':
    game = GameLogic(difficulty='easy')
    player = game.create_character(choice='none', name='LostHeir')
    choice = 0

    while not game_over:
        if not current_enemy:
            clear()
            print('What would You like to do adventurer?\n'
                  '1 - I shall introduce myself.\n'
                  '2 - I will talk to someone.\n'
                  '3 - The whole city must be purged! (Spawns enemy..)')
            try:
                choice = int(input('--> '))
            except ValueError:
                input('You really need to pick one of those options..\n'
                      'Press any key to go back..')

            if choice == 1:
                player.introduce()
            elif choice == 2:
                print(player.random_quote())
                input('Press any key to continue..')
            elif choice == 3:
                current_enemy = game.spawn_enemy()
            else:
                input('You really need to pick one of those options..\n'
                      'Press any key to go back..')

        else:
            if not combat_state:
                print(f'{current_enemy.name} appears!\n')
                combat_state = True
            next_move = game.print_skills(skills=game.get_skills(player))
            if next_move:
                getattr(player, next_move)(enemy=current_enemy)
            else:
                continue
            current_enemy.attack_player(player=player)
            print(f'{player.name}: {player.hp}, {current_enemy.name}: {current_enemy.hp}')
            input()

            if player.hp <= 0:
                game_over = True
            elif current_enemy.hp <= 0:
                current_enemy = None
                combat_state = False

