from dataclasses import dataclass


@dataclass
class Player:
    player_1: int = 0
    player_2: int = 1


def get_score(scoring_player: int = None, score: tuple = None) -> tuple:
    if scoring_player == Player.player_1:
        return 15, 0
    elif scoring_player == Player.player_2:
        if score == (15, 0):
            return 15, 15
        return 0, 15
    return 0, 0
