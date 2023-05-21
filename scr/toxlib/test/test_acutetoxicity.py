import unittest
import acutetoxicity


class TestProbits(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.62, 4.57, 6.38])

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 1, 2, 4],
            survived=[4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.47, 4.33, 5.00, 6.53])

    def test_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 1, 2, 3, 5],
            survived=[5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.36, 4.16, 4.75, 5.25, 6.64])

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 1, 2, 3, 4, 6],
            survived=[6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.27, 4.03, 4.47, 5.00, 5.43, 6.73])

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 1, 2, 3, 4, 5, 7],
            survived=[7, 6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.20, 3.93, 4.43, 4.82, 5.18, 5.57, 6.80])

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.13, 3.85, 4.33, 4.68, 5.00, 5.32, 5.67, 6.87])

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.09, 3.78, 4.23, 4.57, 4.86, 5.14, 5.43, 5.77, 6.91])

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 , 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(), [3.04, 3.72, 4.16, 4.48, 4.75, 5.00, 5.25, 5.52, 5.84, 6.28, 6.96])


if __name__ == "__main__":
    unittest.main()
