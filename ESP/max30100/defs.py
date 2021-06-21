BEATDETECTOR_INIT_HOLDOFF                = 2000   # in ms, how long to wait before counting
BEATDETECTOR_MASKING_HOLDOFF             = 200    # in ms, non-retriggerable window after beat detection
BEATDETECTOR_BPFILTER_ALPHA              = 0.6    # EMA factor for the beat period value
BEATDETECTOR_MIN_THRESHOLD               = 20     # minimum threshold (filtered) value
BEATDETECTOR_MAX_THRESHOLD               = 800    # maximum threshold (filtered) value
BEATDETECTOR_STEP_RESILIENCY             = 30     # maximum negative jump that triggers the beat edge
BEATDETECTOR_THRESHOLD_FALLOFF_TARGET    = 0.3    # thr chasing factor of the max value when beat
BEATDETECTOR_THRESHOLD_DECAY_FACTOR      = 0.99   # thr chasing factor when no beat
BEATDETECTOR_INVALID_READOUT_DELAY       = 2000   # in ms, no-beat time to cause a reset
BEATDETECTOR_SAMPLES_PERIOD              = 10     # in ms, 1/Fs


BEATDETECTOR_STATE_INIT                  = 0
BEATDETECTOR_STATE_WAITING               = 1
BEATDETECTOR_STATE_FOLLOWING_SLOPE       = 2
BEATDETECTOR_STATE_MAYBE_DETECTED        = 3
BEATDETECTOR_STATE_MAS                   = 4

CALCULATE_EVERY_N_BEATS                  = 3
# SAMPLING_FREQUENCY                  = 100
# CURRENT_ADJUSTMENT_PERIOD_MS        = 500
# DEFAULT_IR_LED_CURRENT              = MAX30100_LED_CURR_50MA
# RED_LED_CURRENT_START               = MAX30100_LED_CURR_27_1MA
# DC_REMOVER_ALPHA                    = 0.95


PULSEOXIMETER_STATE_INIT      = 0
PULSEOXIMETER_STATE_IDLE      = 1
PULSEOXIMETER_STATE_DETECTING = 2

spO2LUT[43] = [100,100,100,100,99,99,99,99,99,99,98,98,98,98,
               98,97,97,97,97,97,97,96,96,96,96,96,96,95,95,
               95,95,95,95,94,94,94,94,94,93,93,93,93,93]