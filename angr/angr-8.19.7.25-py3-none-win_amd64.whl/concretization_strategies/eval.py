from . import SimConcretizationStrategy

class SimConcretizationStrategyEval(SimConcretizationStrategy):
    """
    Concretization strategy that resolves an address into some
    limited number of solutions. Always handles the concretization,
    but only returns a maximum of limit number of solutions.
    Therefore, should only be used as the fallback strategy.
    """

    def __init__(self, limit, **kwargs):
        super(SimConcretizationStrategyEval, self).__init__(**kwargs)
        self._limit = limit

    def _concretize(self, memory, addr):
        addrs = self._eval(memory, addr, self._limit)
        return addrs
