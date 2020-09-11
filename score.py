from dataclasses import dataclass
from typing import NewType


@dataclass
class Players:
    player_1: int = 0
    player_2: int = 1


Score = NewType("Score", tuple)


@dataclass
class Scores:
    score_0_0: Score = (0, 0)
    score_15_0: Score = (15, 0)
    score_0_15: Score = (0, 15)
    score_15_15: Score = (15, 15)
    score_0_30: Score = (0, 30)


PLAYER_1_NEXT_SCORE = {Scores.score_0_0: Scores.score_15_0,
                       Scores.score_0_15: Scores.score_15_15}
PLAYER_2_NEXT_SCORE = {Scores.score_0_0: Scores.score_0_15,
                       Scores.score_15_0: Scores.score_15_15,
                       Scores.score_0_15: Scores.score_0_30}


def get_score(score: Score, scoring_player: int = None) -> Score:
    if scoring_player == Players.player_1:
        return PLAYER_1_NEXT_SCORE[score]
    elif scoring_player == Players.player_2:
        return PLAYER_2_NEXT_SCORE[score]
    return Scores.score_0_0
