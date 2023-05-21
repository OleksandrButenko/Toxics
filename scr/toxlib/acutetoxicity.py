import dataclasses


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
