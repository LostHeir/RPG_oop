from game_logic import GameLogic
from user_manager import check_user

game_over = False
current_enemy = None
combat_state = False
player = None
is_logged = False


if __name__ == '__main__':
    game = GameLogic(difficulty='easy')

    while not is_logged:
        game.print_logo()
        login = input('Login: ')
        password = input('Password: ')
        is_logged = check_user(login, password)

    while player is None:
        choice = game.choose_profession()
        print(choice)
        player = game.spawn_hero(choice)

    while not game_over:
        choice = 0
        if not current_enemy:
            choice = game.chose_action()
            if not choice:
                continue
            elif choice == 1:
                player.introduce()
            elif choice == 2:
                print(player.random_quote())
                input('Press any key to continue..')
            elif choice == 3:
                current_enemy = game.spawn_enemy()

        else:
            if not combat_state:
                print(f'{current_enemy.name} appears!\n')
                combat_state = True
            next_move = game.print_skills(skills=game.get_skills(player))
            if next_move:
                getattr(player, next_move)(enemy=current_enemy)
            else:
                continue
            if not next_move == 'run':
                current_enemy.attack_player(player=player)
                print(f'{player.name}: {player.hp}, {current_enemy.name}: {current_enemy.hp}\n')

            if player.hp <= 0:
                game_over = True
                game.game_over()
            elif current_enemy.hp <= 0:
                current_enemy = None
                combat_state = False
            elif next_move == 'run':
                current_enemy = None
                combat_state = False

