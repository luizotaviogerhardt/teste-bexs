import unittest
import sys
sys.path.append('app/Transformers')
sys.path.append('tests/fixture')
import RouteCsvTransformer

class RouteCsvTransformerTest(unittest.TestCase):
    def test_should_transform_csv(self):

        # Arrange

        testFilename = 'tests/fixture/input.csv'

        # Act

        dict = RouteCsvTransformer.transform(testFilename)

        # Assert

        expected = [
            {
                "cost": "10",
                "destination": "BRC",
                "origin": "GRU"
            },
            {
                "cost": "5",
                "destination": "SCL",
                "origin": "BRC"
            },
            {
                "cost": "75",
                "destination": "CDG",
                "origin": "GRU"
            }
        ]

        self.assertEqual(dict, expected)


if __name__ == '__main__':
    unittest.main()
