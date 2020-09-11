from unittest import TestCase

from score import get_score


class Test(TestCase):
    def test_get_score_start_with_0_0(self):
        # Given
        expected_score: tuple = (0, 0)

        # When
        score: tuple = get_score()

        # Then
        self.assertEqual(score, expected_score)

    def test_get_score_when_player_1_score_once(self):
        # Given
        expected_score: tuple = (15, 0)
        scoring_player = 0

        # When
        score: tuple = get_score(scoring_player)

        # Then
        self.assertEqual(score, expected_score)
