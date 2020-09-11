from dataclasses import dataclass
from typing import NewType


@dataclass
class Players:
    player_1: int = 0
    player_2: int = 1


Score = NewType("Score", tuple)


@dataclass
class SingleScores:
    zero: int = 0
    quinze: int = 15
    trente: int = 30
    quarante: int = 40


@dataclass
class Scores:
    score_0_0: Score = (SingleScores.zero, SingleScores.zero)
    score_15_0: Score = (SingleScores.quinze, SingleScores.zero)
    score_0_15: Score = (SingleScores.zero, SingleScores.quinze)
    score_15_15: Score = (SingleScores.quinze, SingleScores.quinze)
    score_0_30: Score = (SingleScores.zero, SingleScores.trente)
    score_30_0: Score = (SingleScores.trente, SingleScores.zero)
    score_15_30: Score = (SingleScores.quinze, SingleScores.trente)
    score_30_15: Score = (SingleScores.trente, SingleScores.quinze)
    score_30_30: Score = (SingleScores.trente, SingleScores.trente)
    score_40_30: Score = (SingleScores.quarante, SingleScores.trente)
    score_30_40: Score = (SingleScores.trente, SingleScores.quarante)
    score_40_40: Score = (SingleScores.quarante, SingleScores.quarante)
    score_40_0: Score = (SingleScores.quarante, SingleScores.zero)
    score_0_40: Score = (SingleScores.zero, SingleScores.quarante)
    score_15_40: Score = (SingleScores.quinze, SingleScores.quarante)
    score_40_15: Score = (SingleScores.quarante, SingleScores.quinze)

NEXT_SCORE = {
    SingleScores.zero: SingleScores.quinze,
    SingleScores.quinze: SingleScores.trente,
    SingleScores.trente: SingleScores.quarante,
}


PLAYER_1_NEXT_SCORE = {Scores.score_0_0: Scores.score_15_0,
                       Scores.score_0_15: Scores.score_15_15,
                       Scores.score_15_0: Scores.score_30_0,
                       Scores.score_15_15: Scores.score_30_15,
                       Scores.score_15_30: Scores.score_30_30,
                       Scores.score_0_40: Scores.score_15_40,
                       Scores.score_15_40: Scores.score_30_40,
                       Scores.score_30_40: Scores.score_40_40,
                       Scores.score_30_30: Scores.score_40_30,
                       Scores.score_30_15: Scores.score_40_15,
                       Scores.score_30_0: Scores.score_40_0
                       }

PLAYER_2_NEXT_SCORE = {Scores.score_0_0: Scores.score_0_15,
                       Scores.score_15_0: Scores.score_15_15,
                       Scores.score_0_15: Scores.score_0_30,
                       Scores.score_15_15: Scores.score_15_30,
                       Scores.score_15_30: Scores.score_15_40,
                       Scores.score_30_15: Scores.score_30_30,
                       Scores.score_30_30: Scores.score_30_40,
                       Scores.score_40_0: Scores.score_40_15,
                       Scores.score_40_15: Scores.score_40_30,
                       Scores.score_40_30: Scores.score_40_40,
                       Scores.score_0_30: Scores.score_0_40
                       }


def get_score(score: Score, scoring_player: int = None) -> Score:
    if scoring_player == Players.player_1:
        return PLAYER_1_NEXT_SCORE[score]
    elif scoring_player == Players.player_2:
        return PLAYER_2_NEXT_SCORE[score]
    return Scores.score_0_0
