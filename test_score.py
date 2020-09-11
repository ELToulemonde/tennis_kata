from unittest import TestCase

from score import get_score, Players, Scores, Score


class Test(TestCase):
    def test_get_score_start_with_0_0(self):
        # Given
        expected_score: Score = Scores.score_0_0

        # When
        score: Score = get_score(score=Scores.score_0_0)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_1_score_once(self):
        # Given
        expected_score: Score = Scores.score_15_0
        scoring_player: int = Players.player_1

        # When
        score: Score = get_score(Scores.score_0_0, scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_2_score_once(self):
        # Given
        expected_score: Score = Scores.score_0_15
        scoring_player: int = Players.player_2
        current_score: Score = Scores.score_0_0

        # When
        score: Score = get_score(score=current_score, scoring_player=scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_1_lead_by_15_0_player_2_scores(self):
        # Given
        expected_score: Score = Scores.score_15_15
        scoring_player: int = Players.player_2
        current_score: Score = Scores.score_15_0

        # When
        score: Score = get_score(current_score, scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_2_lead_by_0_15_player_1_scores(self):
        # Given
        expected_score: Score = Scores.score_15_15
        scoring_player: int = Players.player_1
        current_score: Score = Scores.score_0_15

        # When
        score: Score = get_score(current_score, scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_2_score_and_score_is_0_15(self):
        # Given
        expected_score: Score = Scores.score_0_30
        scoring_player: int = Players.player_2
        current_score: Score = Scores.score_0_15

        # When
        score: Score = get_score(current_score, scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_1_score_and_score_is_15_0(self):
        # Given
        expected_score: Score = Scores.score_30_0
        scoring_player: int = Players.player_1
        current_score: Score = Scores.score_15_0

        # When
        score: Score = get_score(current_score, scoring_player)

        # Then
        self.assertEqual(expected_score, score)
