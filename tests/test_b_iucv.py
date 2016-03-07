#!/usr/bin/python
import os
import b_iucv
import unittest


class TestIUCV(unittest.TestCase):
    def setUp(self):
        '''
        Setup the test suite.
        '''
        self.data = "00000021000000095353495f51756572790000000000000000000000086c696e7578313735"
        self.iucv = b_iucv.SMIUCV()


    def test_xxd_encode(self):
        '''
        Test if encoder is identical to the xxd
        '''
        data = "SSI_Query"
        from_system = os.popen("echo -n " + data + " | xxd -p").read().strip()
        from_py = self.iucv._s2hex(data)

        self.assertEqual(from_system, from_py)

        
    def test_xxd_decode(self):
        '''
        Test if decoder is identical to the xxd.
        '''
        from_system = os.popen("echo " + self.data + " | xxd -p -r").read().strip()
        from_py = self.iucv._hxdmp_to_str(self.data)

        self.assertEqual(from_system, from_py)


    def test_pipeline(self):
        '''
        Test correct smiucv piping.
        '''
        from_system = os.popen("echo {0} | smiucv".format(self.data)).read().strip()
        from_py = self.iucv._smiucv(self.data)
        self.assertEqual(from_system, from_py)


    def test_piped_decoded(self):
        '''
        Test if the pipelined data correctly decoded back.
        '''
        from_system = os.popen("echo {0} | smiucv | xxd -p".format(self.data)).read().strip()
        from_py = self.iucv._s2hex(self.iucv._smiucv(self.data))
        self.assertEqual(from_system, from_py)
        



if __name__ == "__main__":
    unittest.main()
