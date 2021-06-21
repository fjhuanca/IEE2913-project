from defs import *


class BeatDetector:
    def __init__(self, threshold=BEATDETECTOR_MIN_THRESHOLD,
                beatPeriod = 0,
                lastMaxValue = 0,
                tsLastBeat = 0):
        self._threshold = threshold
        self._beatPeriod = beatPeriod
        self._lastMaxValue = lastMaxValue
        self._tsLastBeat = tsLastBeat
        self._state = state

    def addSample(self, sample: float, tmillis: int) -> bool:
        return self._checkForBeat(sample, tmillis)

    def getRate(self) -> float:
        if self.beatPeriod != 0:
            return 1 / self.beatPeriod * 1000 * 60
        else:
            return 0

    def getCurrentThreshold(self) -> float:
        return self._threshold

    def _checkForBeat(self, value: float, tmillis: int) -> bool:
        beatDetected = False
        if self._state == BEATDETECTOR_STATE_INIT:
            if tmillis > BEATDETECTOR_INIT_HOLDOFF:
                self._state = BEATDETECTOR_STATE_WAITING

        elif self._state == BEATDETECTOR_STATE_WAITING:
            if sample > self._threshold:
                self._threshold = min(sample, BEATDETECTOR_MAX_THRESHOLD)
                self._state = BEATDETECTOR_STATE_FOLLOWING_SLOPE
            
            if tmillis - self._tsLastBeat > BEATDETECTOR_INVALID_READOUT_DELAY:
                self._beatPeriod = 0
                self._lastMaxValue = 0

            self._decreaseThreshold()
        
        elif self._state == BEATDETECTOR_STATE_FOLLOWING_SLOPE:
            if sample < self._threshold:
                self._state = BEATDETECTOR_STATE_MAYBE_DETECTED
            else:
                self._threshold = min(sample, BEATDETECTOR_MAX_THRESHOLD)

        elif self._state == BEATDETECTOR_STATE_MAYBE_DETECTED:
            if sample + BEATDETECTOR_STEP_RESILIENCY < self._threshold:
                beatDetected = True
                self._lastMaxValue = sample
                self._state = BEATDETECTOR_STATE_MASKING
                delta = tmillis -self._tsLastBeat
                if delta:
                    self._beatPeriod = BEATDETECTOR_BPFILTER_ALPHA * delta +\
                                       (1 - BEATDETECTOR_BPFILTER_ALPHA) * self._beatPeriod

                self._tsLastBeat = tmillis
            else:
                self._state = BEATDETECTOR_STATE_FOLLOWING_SLOPE

        elif self._state == BEATDETECTOR_STATE_MASKING:
            if tmillis - self._tsLastBeat > BEATDETECTOR_MASKING_HOLDOFF:
                state = BEATDETECTOR_STATE_WAITING
            self._decreaseThreshold()

        return beatDetected
    
    def _decreaseThreshold(self) -> None:
        if self._lastMaxValue > 0 and self._beatPeriod > 0:
            self._threshold -= self._lastMaxValue * (1 - BEATDETECTOR_THRESHOLD_FALLOFF_TARGET) / \
                               (self._beatPeriod / BEATDETECTOR_SAMPLES_PERIOD)
        else:
            self._threshold *= BEATDETECTOR_THRESHOLD_DECAY_FACTOR
        
        if (self._threshold) < BEATDETECTOR_MIN_THRESHOLD:
            self._threshold = BEATDETECTOR_MIN_THRESHOLD
        return None

