import unittest

import pandas as pd

class PandaTest(unittest.TestCase):

    def test_read_csv_and_data_frame(self):
        df = pd.read_csv('stub/test_panda.csv')
        self.assertEqual(df.size, 4);
        self.assertEqual(df.at[0, 'name'], 'sang')
        self.assertEqual(df.loc[1].at['name'], 'kim')
        self.assertEqual(df.iat[0, 1], 36)

    def test_data_frame_merge(self):
        df1 = pd.read_csv('stub/test_panda.csv')
        df2 = pd.read_csv('stub/test_panda_join.csv')

        merged = pd.merge(df1, df2)
        self.assertEqual(merged.at[0, 'name'], 'sang')
        self.assertEqual(merged.at[0, 'age'], 36)
        self.assertEqual(merged.at[0, 'gender'], 'male')
        self.assertEqual(merged.at[1, 'name'], 'kim')
        self.assertEqual(merged.at[1, 'age'], 35)
        self.assertEqual(merged.at[1, 'gender'], 'female')

if __name__ == '__main__':
    unittest.main()

