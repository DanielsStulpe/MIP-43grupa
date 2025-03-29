"""
Datu struktūra spēles kokam
"""

import random
from typing import List
from copy import deepcopy

class Node:
    def __init__(self, length: int = 15, first_player_points: int = 100, second_player_points: int = 100, sequence: List[int] = None):
        """ Klases konstruktors """
        self.first_player_points: int = first_player_points
        self.second_player_points: int = second_player_points
        self.sequence: List[int] = sequence if sequence is not None else self.generate_sequence(length)
        self.length = length

    def generate_sequence(self, length: int) -> List[int]:
        """ Ģenerē nejaušu skaitļu virkni no 1 līdz 4 """
        return [random.randint(1, 4) for _ in range(length)]



def possible_moves(node: Node) -> List[int]:
    """ Izdod visus iespējamus gājienus """
    return list(set(node.sequence))
    

def get_player(node: Node) -> int:
    """ Nosaka spēlētāju """
    return ((node.length - len(node.sequence)) % 2) + 1
    

def is_terminal(node: Node) -> bool:
    """ Nosaka vai spēle ir pabeigta """
    return len(node.sequence) == 0
    

def get_heuristic_value(node: Node) -> int:
    """ Izdod heiristiskas funkcijas novērtējumu  """
    sequence = node.sequence[:]
    first_player_points = node.first_player_points
    second_player_points = node.second_player_points
    player = get_player(node)    # 1 = pirmais, 2 = otrais

    move_cost = {  
        1: -1,   # dod 1 punktu pretiniekam = noņem 1 punktu sev
        2: -4,   # noņem 4 punktus sev
        3: -3,   # dod 3 punktus pretiniekam = noņem 3 punktus sev
        4: -8    # noņem 8 punktus sev
    }

    while sequence:      # Katrā solī atbilstošais spēlētājs izvēlas mazāko iespējamo zaudējumu
        best_move = min(sequence, key=lambda x: move_cost[x])
        sequence.remove(best_move)

        if player == 1:     # Pirmais spēlētājs
            first_player_points += move_cost[best_move]
            player += 1
        else:               # Otrais spēlētājs
            second_player_points += move_cost[best_move]
            player -= 1

    return first_player_points - second_player_points
    

def get_winner(node: Node) -> int:
    """ Nosaka uzvarētāju """
    if node.first_player_points < node.second_player_points:
        return 1
    elif node.first_player_points > node.second_player_points:
        return 2
    else:
        return 0


def update_points(node: Node, player: int, move: int) -> Node:
    """ Atjaunina punktus, pamatojoties uz gājienu un spēlētāju """
    if player == 1:
        if move % 2 == 0:
            node.first_player_points -= (move * 2)
        else:
            node.second_player_points += move
    else:
        if move % 2 == 0:
            node.second_player_points -= (move * 2)
        else:
            node.first_player_points += move
    return node


def player_make_move(node: Node, place: int) -> Node:
    """ Apstrādā spēlētāja gājienu, noņemot elementu no virknes atkarībā no `place` """
    player = get_player(node)
    new_node = deepcopy(node)
    
    if 0 <= place < len(new_node.sequence):
        move = new_node.sequence.pop(place)
    else:
        raise ValueError("`Place` ir ārpus diapazona")
    
    new_node = update_points(new_node, player, move)
    
    return new_node


def ai_make_move(node: Node, move: int) -> tuple[Node, int]:
    """ Apstrādā AI gājienu, noņemot skaitli `move` no virknes """
    player = get_player(node)
    new_node = deepcopy(node)
    
    places = [index for index, value in enumerate(node.sequence) if value == move]
    if places:
        place = random.choice(places)
        new_node.sequence.pop(place)
    else:
        raise ValueError("Nav iespējams veikt gājienu")
    
    new_node = update_points(new_node, player, move)
    
    return new_node, place
