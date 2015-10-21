import unittest
import imAlgo as jkl

""" Generate unit tests first. """

class TestCalMethods(unittest.TestCase):

    def test_getForce(self):
        self.assertEqual(0, jkl.getForce())

    def test_getAcceleration(self):
        self.assertEqual(0, jkl.getAcceleration())

    """ Creates """
    def test_computeForce(self):
        jkl.setMass()
        for i in range(100):
            self.assertEqual(i*0, jkl.computeForce())

if __name__ == "__main__":
    unittest.main()
    