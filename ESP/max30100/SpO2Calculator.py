from defs import *
import math

class SpO2Calculator:

    def __init__(self):
        self._spO2LUT = spO2LUT
        self._irACValueSqSum = 0.0
        self._redACValueSqSum = 0.0
        self._beats_DetectedNum = 0
        self._samplesRedcorded = 0
        self._spO2 = 0

    def update(irACValue: float, redACValue: float, beatDetected: bool) -> None:
        self._irACValueSqSum += irACValue ** 2
        self._redACValueSqSum += irACValue ** 2
        self._samplesRedcorded += 1

        if beatDetected:
            self._beats_DetectedNum += 1
            if self._beats_DetectedNum == CALCULATE_EVERY_N_BEATS:
                acSqRatio = 100.0 * math.log(self._redACValueSqSum / self._samplesRedcorded) /\
                            math.log(self._irACValueSqSum / self._samplesRedcorded)
                index = 0
            if acSqRatio > 66:
                index = acSqRatio - 66
            elif acSqRatio > 50:
                index = acSqRatio - 50  

            self.reset()
            self._spO2 = self._spO2LUT[index]

        
    def reset() -> None:
        self._samplesRecorded = 0
        self._redACValueSqSum = 0
        self._irACValueSqSum = 0
        self._beatsDetectedNum = 0
        self._spO2 = 0

    def getSpO2() -> float:
        return self._spO2
    
