from unittest import TestCase

from score import get_score, Player


class Test(TestCase):
    def test_get_score_start_with_0_0(self):
        # Given
        expected_score: tuple = (0, 0)

        # When
        score: tuple = get_score()

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_1_score_once(self):
        # Given
        expected_score: tuple = (15, 0)
        scoring_player: int = Player.player_1

        # When
        score: tuple = get_score(scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_2_score_once(self):
        # Given
        expected_score: tuple = (0, 15)
        scoring_player: int = Player.player_2

        # When
        score: tuple = get_score(scoring_player)

        # Then
        self.assertEqual(expected_score, score)

    def test_get_score_when_player_1_lead_by_15_0_player_2_scores(self):
        # Given
        expected_score: tuple = (15, 15)
        scoring_player: int = Player.player_2
        current_score: tuple = (15, 0)

        # When
        score: tuple = get_score(scoring_player, current_score)

        # Then
        self.assertEqual(expected_score, score)

