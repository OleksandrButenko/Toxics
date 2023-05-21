import dataclasses
import numpy as np
from numpy._typing import NDArray


@dataclasses.dataclass
class Expirement:
    dosage: list[float]
    fallen: list[int]
    survived: list[int]


class Probits(object):
    __slots__: list[str] = ["_expirement", "__probit_mapping"]

    def __init__(self, expirement: Expirement) -> None:
        self._expirement: Expirement = expirement
        self.__probit_mapping: dict[int, dict[int, float]] = {
            3: {0: 3.62, 1: 4.57, 2: 5.43, 3: 6.38},
            4: {0: 3.47, 1: 4.33, 2: 5.00, 3: 5.57, 4: 6.53},
            5: {0: 3.36, 1: 4.16, 2: 4.75, 3: 5.25, 4: 5.84, 5: 6.64},
            6: {0: 3.27, 1: 4.03, 2: 4.47, 3: 5.00, 4: 5.43, 5: 5.97, 6: 6.73},
            7: {0: 3.20, 1: 3.93, 2: 4.43, 3: 4.82, 4: 5.18, 5: 5.57, 6: 6.07, 7: 6.80},
            8: {0: 3.13, 1: 3.85, 2: 4.33, 3: 4.68, 4: 5.00, 5: 5.32, 6: 5.67, 7: 6.15, 8: 6.87},
            9: {0: 3.09, 1: 3.78, 2: 4.23, 3: 4.57, 4: 4.86, 5: 5.14, 6: 5.43, 7: 5.77, 8: 6.22, 9: 6.91},
            10: {0: 3.04, 1: 3.72, 2: 4.16, 3: 4.48, 4: 4.75, 5: 5.00, 6: 5.25, 7: 5.52, 8: 5.84, 9: 6.28, 10: 6.96}
        }

    def calculate(self) -> list[float]:
        probits: list[float] = []
        for i in range(len(self._expirement.fallen)):
            fallen_survivors: int = self._expirement.fallen[i] + self._expirement.survived[i]
            probits.append(self.__probit_mapping[fallen_survivors][self._expirement.fallen[i]])
        return probits


class LetalDosage(object):
    __slots__: list[str] = ["_expirement", "_probits", "_percent_mortality"]

    def __init__(self, expirement: Expirement) -> None:
        self._expirement: Expirement = expirement
        self._probits: list[float] = Probits(expirement).calculate()

    def calculate_percent_mortality(self) -> list[float]:
        mortality: list[float] = []

        for i in range(len(self._expirement.fallen)):
            percent: float = self._expirement.fallen[i] / (self._expirement.fallen[i] + self._expirement.survived[i])
            convert_percent: float = round(percent * 100, 2)
            mortality.append(convert_percent)

        return list(mortality)

    def calculate_ld0(self) -> (float | None):
        survived: int = 0
        next_animal: int = 1

        for i in range(len(self._expirement.fallen)):
            if self._expirement.fallen[i] == survived and self._expirement.fallen[i + next_animal] != survived:
                return self._expirement.dosage[i]
        else:
            return None

    def calculate_ld16(self) -> float:
        LD16_PROBIT: int = 4
        ld16: NDArray[np.float64] = np.interp(LD16_PROBIT, self._probits, self._expirement.dosage)
        return float(round(ld16.item(), 2))

    def calculate_ld50(self) -> float:
        ld50: float = 0.0
        percent_mortality: list[float] = self.calculate_percent_mortality()

        for i in range(len(self._expirement.dosage) - 1):
            sum_dosage: float = self._expirement.dosage[i + 1] + self._expirement.dosage[i]
            diff_modality: float = abs(percent_mortality[i + 1] - percent_mortality[i])
            ld50 += sum_dosage * diff_modality / 200

        return float(round(ld50, 2))

    def calculate_ld84(self) -> float:
        LD84_PROBIT: int = 6
        ld84: NDArray[np.float64] = np.interp(LD84_PROBIT, self._probits, self._expirement.dosage)
        return float(round(ld84.item(), 2))

    def calculate_ld100(self) -> (float | None):
        all_animals_dead: float = 100.0
        percent_mortality: list[float] = self.calculate_percent_mortality()

        if max(percent_mortality) == all_animals_dead:
            return float(max(self._expirement.dosage))
        else:
            return None

    def calculate_sld50(self) -> float:
        coutn_animals: list[int] = []

        for i in range(len(self._expirement.fallen) - 1):
            current_fallen: int = self._expirement.fallen[i]
            next_fallen: int = self._expirement.fallen[i + 1]
            current_survived: int = self._expirement.survived[i]

            if current_fallen == 0 and next_fallen != 0:
                coutn_animals.append(current_fallen + current_survived)
            elif current_fallen != 0:
                coutn_animals.append(current_fallen + current_survived)

        total_count_animals: int = sum(coutn_animals)
        defference: float = float(self.calculate_ld84() - float(self.calculate_ld16()))
        sld50: float = defference / total_count_animals

        return float(round(sld50, 2))
