import max30100
from defs import *
from filters import DCRemover, FilterBuLp1
from SpO2Calculator import Spo2calculator

class PulseOximeter:
    def __init__(self,
                 i2c=None,
                 mode=MODE_HR,
                 sample_rate=100,
                 led_current_red=11.0,
                 led_current_ir=11.0,
                 pulse_width=1600,
                 max_buffer_len=10000
                 ):
        self._tsLastCurrentAdjustment = 0
        self._spo2_calculator = Spo2calculator()
        self._hrm = max30100.MAX30100(i2c=i2c, mode=mode, sample_rate=sample_rate,
                 led_current_red=led_current_red, led_current_ir=led_current_ir,
                 pulse_width=pulse_width, max_buffer_len=max_buffer_len)
        self._hrm.enable_spo2()
        self._irDCRemover = DCRemover(DC_REMOVER_ALPHA)
        self.redDCRemover = DCRemover(DC_REMOVER_ALPHA)
        self._state = PULSEOXIMETER_STATE_IDLE
        return True

    def update(self):
        self._hrm.read_sensor()
        self.checkSample()
        self.checkCurrentBias()

    def getHeartRate(self):
        pass

    def getSpO2(self):
        return self.spo2_calculator.getSpO2()
        