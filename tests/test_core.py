# import unittest
#
#
# class LgtmTest(unittest.TestCase):
#     def test_lgtm(self):
#         from lgtm.core import lgtm
#         self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))  # add assertion here

def test_lgtm():
    from lgtm.core import lgtm
    assert (lgtm('./python.jpeg', 'LGTM')) is None  # add assertion here
