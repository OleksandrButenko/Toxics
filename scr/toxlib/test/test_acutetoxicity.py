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
        self.assertEqual(probits.calculate(),
                         [3.20, 3.93, 4.43, 4.82, 5.18, 5.57, 6.80])

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(),
                         [3.13, 3.85, 4.33, 4.68, 5.00, 5.32, 5.67, 6.87])

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(),
                         [3.09, 3.78, 4.23, 4.57, 4.86, 5.14, 5.43, 5.77, 6.91])

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 , 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        probits: acutetoxicity.Probits = acutetoxicity.Probits(expirement)
        self.assertEqual(probits.calculate(),
                         [3.04, 3.72, 4.16, 4.48, 4.75, 5.00, 5.25, 5.52, 5.84, 6.28, 6.96])


class TestLetalDosogeCalculatePercentMortality(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_percent_mortality_for_three_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(), [0.0, 33.33, 100.0])

    def test_calculate_percent_mortality_for_four_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 1, 2, 4],
            survived=[4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 25.0, 50.0, 100.0])

    def test_calculate_percent_mortality_for_five_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 1, 2, 3, 5],
            survived=[5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 20.0, 40.0, 60.0, 100.0])

    def test_calculate_percent_mortality_for_six_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 1, 2, 3, 4, 6],
            survived=[6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 16.67, 33.33, 50.0, 66.67, 100.0])

    def test_calculate_percent_mortality_for_seven_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 1, 2, 3, 4, 5, 7],
            survived=[7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 14.29, 28.57, 42.86, 57.14, 71.43, 100.0])

    def test_calculate_percent_mortality_for_eight_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 100.0])

    def test_calculate_percent_mortality_for_nine_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6 , 0.7, 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 11.11, 22.22, 33.33, 44.44, 55.56, 66.67, 77.78, 100.0])

    def test_calculate_percent_mortality_for_ten_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6 , 0.7, 0.8, 0.9, 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_percent_mortality(),
                         [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100.0])


class TestLetalDosogeCalculateLD0(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_percent_mortality_for_three_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 0, 3],
            survived=[3, 3, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.2)

    def test_calculate_percent_mortality_for_four_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 0, 0, 4],
            survived=[4, 4, 4, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.3)

    def test_calculate_percent_mortality_for_five_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 0, 0, 0, 5],
            survived=[5, 5, 5, 5, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.4)

    def test_calculate_percent_mortality_for_six_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 0, 0, 0, 0, 6],
            survived=[6, 6, 6, 6, 6, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.5)

    def test_calculate_percent_mortality_for_seven_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 0, 0, 0, 0, 0, 7],
            survived=[7, 7, 7, 7, 7, 7, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.6)

    def test_calculate_percent_mortality_for_eight_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8],
            fallen=[0, 0, 0, 0, 0, 0, 0, 8],
            survived=[8, 8, 8, 8, 8, 8, 8, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.7)

    def test_calculate_percent_mortality_for_nine_animal_in_group(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9],
            fallen=[0, 0, 0, 0, 0, 0, 0, 0, 9],
            survived=[9, 9, 9, 9, 9, 9, 9, 9, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld0(), 0.8)


class TestLetalDosogeCalculateLD16(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.14)

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 1, 2, 4],
            survived=[4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.16)

    def test_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 1, 2, 3, 5],
            survived=[5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.18)

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 1, 2, 3, 4, 6],
            survived=[6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.20)

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 1, 2, 3, 4, 5, 7],
            survived=[7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.21)

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.23)

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.25)

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9, 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld16(), 0.26)


class TestLetalDosogeCalculateLD84(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.28)

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 1, 2, 4],
            survived=[4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.37)

    def test_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 1, 2, 3, 5],
            survived=[5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.45)

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 1, 2, 3, 4, 6],
            survived=[6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.54)

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 1, 2, 3, 4, 5, 7],
            survived=[7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.63)

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.73)

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.82)

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9, 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld84(), 0.91)


class LetalDosageCalculateLD100(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.3)

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4],
            fallen=[0, 1, 2, 4],
            survived=[4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.4)

    def test_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5],
            fallen=[0, 1, 2, 3, 5],
            survived=[5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.5)

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            fallen=[0, 1, 2, 3, 4, 6],
            survived=[6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.6)

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
            fallen=[0, 1, 2, 3, 4, 5, 7],
            survived=[7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.7)

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8],
            fallen=[0, 1, 2, 3, 4, 5, 6, 8],
            survived=[8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.8)

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 9],
            survived=[9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 0.9)

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 , 0.8, 0.9, 1.0],
            fallen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
            survived=[10, 9, 8, 7, 6, 5, 4, 3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld100(), 1.0)


class TestLetalDosogeCalculateLD50(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        exiprement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(exiprement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 1137.52)

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        exiprement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100],
            fallen=[0, 1, 3, 4],
            survived=[4, 3, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(exiprement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 1312.50)

    def text_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625],
            fallen=[0, 1, 3, 4, 5],
            survived=[5, 4, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 1575.00)

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        exiprement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625, 3150],
            fallen=[0, 1, 3, 4, 5, 6],
            survived=[6, 5, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(exiprement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 1749.98)

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625, 3150, 3675],
            fallen=[0, 1, 3, 4, 5, 6, 7],
            survived=[7, 6, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 1987.49)

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625, 3150, 3675, 4200],
            fallen=[0, 1, 3, 4, 5, 6, 7, 8],
            survived=[8, 7, 5, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 2231.25)

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625, 3150, 3675, 4200, 4725],
            fallen=[0, 1, 3, 4, 5, 6, 7, 8, 9],
            survived=[9, 8, 6, 5, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 2479.16)

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[525, 1050, 1575, 2100, 2625, 3150, 3675, 4200, 4725, 5250],
            fallen=[0, 0, 0, 0, 1, 3, 4, 5, 7, 10],
            survived=[10, 10, 10, 10, 9, 7, 6, 5, 3, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_ld50(), 3937.50)


class TestLetalDosogeCalculateSLD50(unittest.TestCase):
    __slots__: list[str] = []

    def test_calculate_for_three_animals_in_gpoup(self) -> None:
        exiprement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625],
            fallen=[0, 1, 3],
            survived=[3, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(exiprement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 121.63)

    def test_calculate_for_four_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150],
            fallen=[0, 1, 3, 4],
            survived=[4, 3, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 80.13)

    def test_calculate_for_five_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675],
            fallen=[0, 1, 3, 4, 5],
            survived=[5, 4, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 63.00)

    def test_calculate_for_six_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675, 4200],
            fallen=[0, 1, 3, 4, 5, 6],
            survived=[6, 5, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 53.88)

    def test_calculate_for_seven_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675, 4200, 4725],
            fallen=[0, 1, 3, 4, 5, 6, 7],
            survived=[7, 6, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 47.27)

    def test_calculate_for_eight_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675, 4200, 4725, 5250],
            fallen=[0, 1, 3, 4, 5, 6, 7, 8],
            survived=[8, 7, 5, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 42.25)

    def test_calculate_for_nine_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675, 4200, 4725, 5250, 5775],
            fallen=[0, 1, 3, 4, 5, 6, 7, 8, 9],
            survived=[9, 8, 6, 5, 4, 3, 2, 1, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 38.15)

    def test_calculate_for_ten_animals_in_gpoup(self) -> None:
        expirement: acutetoxicity.Expirement = acutetoxicity.Expirement(
            dosage=[1575, 2100, 2625, 3150, 3675, 4200, 4725, 5250, 5775, 6300],
            fallen=[0, 0, 0, 0, 1, 2, 3, 5, 8, 10],
            survived=[10, 10, 10, 10, 9, 8, 7, 5, 2, 0]
        )
        letal_dosoge: acutetoxicity.LetalDosage = acutetoxicity.LetalDosage(expirement)
        self.assertEqual(letal_dosoge.calculate_sld50(), 30.68)


if __name__ == "__main__":
    unittest.main()
