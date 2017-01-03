# Copyright (c) 2016, MD2K Center of Excellence
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import datetime
import unittest

from cerebralcortex.kernel.datatypes.datapoint import DataPoint


class TestDataPoint(unittest.TestCase):
    def test_DataPoint_None(self):
        dp = DataPoint()
        self.assertIsNone(dp.get_sample())
        self.assertIsNone(dp.get_datastream_id())
        self.assertIsNone(dp.get_timestamp())
        self.assertRaises(ValueError, dp.get_timestamp_epoch)

    def test_DataPoint(self):
        ts = datetime.datetime.now()
        dp = DataPoint(id=134, datastream=4, timestamp=ts, sample={'Foo': 123})
        self.assertDictEqual(dp.get_sample(), {'Foo': 123})
        self.assertEqual(dp.get_datastream_id(), 4)
        self.assertEqual(dp.get_timestamp(), ts)
        self.assertEqual(dp.get_timestamp_epoch(), ts.timestamp() * 1e6)


if __name__ == '__main__':
    unittest.main()
