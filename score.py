def get_score(scoring_player: int = None) -> tuple:
    if scoring_player == 0:
        return 15, 0
    elif scoring_player == 1:
        return 0, 15
    return 0, 0
