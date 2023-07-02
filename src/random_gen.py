import random
import numpy as np

class RandomGen(object):

    def __init__(self, random_nums, probabilities):
        if not np.isclose(sum(probabilities), 1):
            raise ValueError("Probabilities should add up to 1.")
        self._random_nums = random_nums
        self._probabilities = probabilities

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        return np.random.choice(self._random_nums, p=self._probabilities)
