from random import randint
from os import system

class LivingThing():
    MOVEMENTS = '8', '2', '4', '6'
    UP, DOWN, LEFT, RIGHT = MOVEMENTS
    ATTACK = 'a'
    printable = {'Goblin': 'G', 'Dragon': 'D'}

    def __init__ (self, name, health, magic_points, inventory, weapon, location, board, armor=None):
        self.name = name
        self.health = health
        self.magic_points = magic_points
        self.inventory = inventory
        self.weapon = weapon
        self.__location = location
        self.board = board
        self.armor = armor

    def move(self, direction):
        """
        move in specific direction
        """
        new_location = self.__location[:]
        if direction == LivingThing.UP:
            new_location[0] -= 1
        elif direction == LivingThing.DOWN:
            new_location [0] += 1
        elif direction == LivingThing.LEFT:
            new_location [1] -= 1
        elif direction == LivingThing.RIGHT:
            new_location [1] += 1
        if self.board.is_free(new_location):
            self.__location = new_location
            return True
        else:
            return False

    def get_location(self):
        """
        location getter
        """
        return self.__location

    def set_location(self, location):
        """
        location setter
        """
        self.__location = location

    def __str__(self):
        """
        returns printing string for board
        """

        if self.name in LivingThing.printable:
            return LivingThing.printable[self.name]
        else:
            return 'H'

    def __repr__(self):
        """
        returns object's representation
        """

        return 'A LivingThing in Location: ' + str(self.__location) + ' By the name: ' + self.name

    def attack(self, enemy):
        """
        attack a specific enemy. and return true if killed it!
        """
        damage = self.weapon.get_damage()
        print(self.name, 'attacks', enemy.name, 'for', damage, end='')
        if not enemy.take_damage(damage):
            print(' and kills it!', end='')
            self.inventory['gold'] += enemy.get_inventory()['gold']
            input(' (press any key to continue)')
            return True
        input(' (press any key to continue)')
        return False

    def get_inventory(self):
        """
        inventory getter
        """
        return self.inventory

    def get_health(self):
        """
        health getter
        """
        return self.health

    def take_damage(self, damage):
        """
        takes damage according to armor adjustment.
        returns true if still alive, or false if killed
        """
        damage_adjustment = 0
        if self.armor:
            damage_adjustment += self.armor.get_protection()
        self.health -= max((damage - damage_adjustment), 0)
        if self.health > 0:
            return True
        return False

    def random_move(self):
        """
        make a random play (either move or attack)
        """
        choice = randint(0,10)
        if choice in range(4):
            self.move(LivingThing.MOVEMENTS[choice])
        else:
            #attack everybody around us!
            self.board.attack_neighbors(self)

    def get_neighbors(self):
        """
        return all adjacent living creatures
        """
        neighbors = []
        if self is not self.board.get_hero() and self.near(self.board.get_hero()):
            neighbors.append(self.board.get_hero())
        for monster in self.board.get_monsters():
            if self is not monster and self.near(monster):
                neighbors.append(monster)
        return neighbors

    def near(self, living_thing):
        """
        returns whether another living thing is adjacent
        """
        self_row, self_column = self.__location
        other_row, other_column = living_thing.get_location()
        return abs(self_row-other_row) < 2 and abs(self_column-other_column) < 2



class GameBoard():
    def __init__(self, height=10, width=10):
        self.height = height
        self.width = width
        self.monsters = []
        self.hero = None
        self.trees = []
        self.game_over = False

    def is_free(self, location):
        if not 0 <= location[0] < self.height or not 0 <= location[1] < self.width:
            return False
        for monster in self.monsters:
            if location == monster.get_location():
                return False
        for tree in self.trees:
            if location == tree:
                return False
        if self.hero:
            if location == self.hero.get_location():
                return False
        return True

    def put_tree(self, location):
        if self.is_free(location):
            self.trees.append(location)
            return True
        return False

    def put_monster(self, monster):
        if self.is_free(monster.get_location()):
            self.monsters.append(monster)
            return True
        return False

    def put_hero(self, hero):
        if self.is_free(hero.get_location()):
            self.hero = hero
            return True
        return False

    def __str__(self):
        board_lists = [[' '] * self.width for rows in range(self.height)]
        for tree_row, tree_column in self.trees:
            board_lists[tree_row][tree_column] = '*'
        for monster in self.monsters:
            monster_row, monster_column = monster.get_location()
            board_lists[monster_row][monster_column] = str(monster)
        hero_row, hero_column = self.hero.get_location()
        board_lists[hero_row][hero_column] = str(self.hero)
        board_strings = ['#' * (self.width + 1)]
        for row in board_lists:
            board_strings.append(''.join(row))
        board_strings.append('#' * (self.width + 1))
        return_str = '#\n#'.join(board_strings)
        if self.hero:
            return_str += '\nHero Health: '
            return_str += str(self.hero.get_health())
        return return_str

    def __contains__(self, living_thing):
        return living_thing in self.heroes or living_thing in self.monsters

    def reset(self):
        self.__init__(10, 10)
        self.put_tree([1,1])
        self.put_tree([1,2])
        self.put_tree([1,3])
        self.put_tree([2,3])
        weapon = Weapon('sword', 6)
        armor = Armor('wooden shield', 1)
        hero = LivingThing('Mark', 50, 80, {'gold': 40, 'potion': 2, 'sword':1}, weapon, [4, 6], self, armor)
        self.put_hero(hero)
        weapon = Weapon('dagger', 2)
        monster = LivingThing('Goblin', 20, 0, {'gold': 12, 'dagger': 1}, weapon, [3, 3], self)
        self.put_monster(monster)
        weapon = Weapon('fire', 30)
        monster = LivingThing('Dragon', 300, 200, {'gold': 890, 'amulet': 1}, weapon , [1, 5], self)
        self.put_monster(monster)
        weapon = Weapon('dagger', 2)
        monster = LivingThing('Goblin', 18, 0, {'gold': 15, 'dagger': 1}, weapon, [4, 2], self)
        self.put_monster(monster)

    def play_turn(self, action):
        if action in (self.hero.UP, self.hero.DOWN, self.hero.LEFT, self.hero.RIGHT):
            self.hero.move(action)
        elif action == self.hero.ATTACK:
            self.attack_neighbors(self.hero)
        for monster in self.monsters:
            monster.random_move()
        return not self.game_over

    def attack_neighbors(self, attacker):
        for neighbor in attacker.get_neighbors():
            killed = attacker.attack(neighbor)
            if killed:
                self.__kill(neighbor)

    def __kill(self, living_thing):
        if living_thing is self.hero:
            self.game_over = True
            return True
        if living_thing  in self.monsters:
            self.monsters.remove(living_thing)
            return True
        return False

    def get_hero(self):
        return self.hero

    def get_monsters(self):
        return self.monsters


class Weapon():
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_damage(self):
        return self.__damage

    def __str__(self):
        return self.__name


class Armor():
    def __init__(self, name, protection):
        self.__name = name
        self.__protection = protection

    def get_protection(self):
        return self.__protection

    def __str__(self):
        return self.__name


class GameRunner():
    ABORT_GAME = 'q'
    GAME_OVER_MSG = 'Game over! Do you want to play again? (y)'
    PLAY_AGAIN = 'y'
    INPUT_MESSAGE = 'Please enter your move: To move, use the keys ' \
                    + ', '.join(LivingThing.MOVEMENTS) + '. To Attack, use ' \
                    + LivingThing.ATTACK + '.\nTo quit, enter ' \
                    + ABORT_GAME + '.\n'

    def __init__(self):
        self.board = GameBoard()
        self.board.reset()

    def run(self):
        while True:
            system('cls')
            print(self.board)
            action = self.get_action_from_usr()
            if action == GameRunner.ABORT_GAME:
                break
            alive = self.board.play_turn(action)
            if not alive:
                play_again = input(GameRunner.GAME_OVER_MSG)
                if play_again == GameRunner.PLAY_AGAIN:
                    self.board.reset()
                else:
                    break

    def get_action_from_usr(self):
        return input(GameRunner.INPUT_MESSAGE)


if __name__ == "__main__":
    game = GameRunner()
    game.run()














