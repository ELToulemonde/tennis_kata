from dataclasses import dataclass


@dataclass
class Players:
    player_1: int = 0
    player_2: int = 1


@dataclass
class Scores:
    score_0_0: tuple = (0, 0)
    score_15_0: tuple = (15, 0)
    score_0_15: tuple = (0, 15)
    score_15_15: tuple = (15, 15)


def get_score(scoring_player: int = None, score: tuple = None) -> tuple:
    if scoring_player == Players.player_1:
        if score == Scores.score_0_15:
            return Scores.score_15_15
        return Scores.score_15_0
    elif scoring_player == Players.player_2:
        if score == Scores.score_15_0:
            return Scores.score_15_15
        return Scores.score_0_15
    return Scores.score_0_0
