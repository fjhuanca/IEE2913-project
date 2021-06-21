class DCRemover:
    def __init__(self, alpha=0, dcw=0):
        self._alpha = alpha
        self._dcw = dcw

    def step(self, x: float) -> float:
        olddcw = dcw
        dcw = x + alpha * dcw
        return dcw - olddcw
	

    def getDCW(self):
        return dcw


class  FilterBuLp1:

    def __init__(self):
        self.v = [0, 0]

    def step(x: float) -> float:
        self.v[0] = v[1]
        self.v[1] = (2.452372752527856026e-1 * x) + (0.50952544949442879485 * v[0])
        return v[0] + v[1]
		
