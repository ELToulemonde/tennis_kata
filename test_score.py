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
