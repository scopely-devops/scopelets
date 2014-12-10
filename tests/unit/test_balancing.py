# Copyright (c) 2014 Scopely, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import unittest
from scopelets.balancelib import fill


class TestBalancing(unittest.TestCase):

    def test_even_balance(self):
        by_az = [3, 3, 3]
        self.assertEqual(fill(by_az, 3), [1, 1, 1])

    def test_even_balance_uneven_instances(self):
        by_az = [3, 3, 3]
        self.assertEqual(fill(by_az, 5), [2, 2, 1])

    def test_even_balance_uneven_instances_less(self):
        by_az = [3, 3, 3]
        self.assertEqual(fill(by_az, 2), [1, 1, 0])

    def test_uneven_balance1(self):
        by_az = [3, 2, 1]
        self.assertEqual(fill(by_az, 2), [0, 0, 2])

    def test_uneven_balance2(self):
        by_az = [3, 2, 1]
        self.assertEqual(fill(by_az, 3), [0, 1, 2])

    def test_uneven_balance3(self):
        by_az = [3, 2, 1]
        self.assertEqual(fill(by_az, 5), [1, 2, 2])


if __name__ == "__main__":
    unittest.main()
