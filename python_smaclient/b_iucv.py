#!/usr/bin/python

import os
import sys
import subprocess


class SMIUCV(object):
    '''
    Implementation for the client via the IUCV socket communication.
    '''

    def _smiucv(self, request):
        '''
        Send a request to the IUCV socket.
        '''
        return subprocess.Popen(['/root/bin/smiucv'],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.STDOUT).communicate(input=request)[0]


    def _hxint8(self, val):
        '''
        Convert value to hex representation of 8 byte int
        '''
        return self._hxint(val).zfill(16)


    def _hxint4(self, val):
        '''
        Convert value to hex representation of 4 byte int
        '''
        return self._hxint(val).zfill(8)


    def _hxint(self, val):
        '''
        Convert value to hex representation of 1 byte int
        '''
        return hex(val).split("x")[-1]


    def _s2hex(self, val):
        '''
        String to hexadecimal. (xxd -p)
        '''
        return ''.join([hex(ord(smb)).split('x')[-1].zfill(2) for smb in val])


    def _str_len_hex(self, val):
        '''
        Prepend string lenth hexadecimal.
        '''
        return self._hxint4(len(val)) + self._s2hex(val)


    def _str_asciiz(self, val):
        '''
        Convert string to hex representation with ASCIIZ appended
        '''
        return self._s2hex(val) + "00"


    def _hxdmp_to_str(self, val):
        '''
        Convert hex dump to the string (xxd -p -r)
        '''
        return ''.join([chr(int("0x" + val[idx:idx + 2], 0)) for idx in range(0, len(val), 2)])


    def _hxdmp_str_array(self, val):
        '''
        Convert array of strings to hex representation.
        '''
        hx_repr = ''.join([self._str_len_hex(elem) for elem in val])
        return self._hxint4(int(len(hx_repr) / 2)) + hx_repr


    def __call__(self, function, user=None, password=None, target=None, switch=None):
        '''
        Send request to the SMAPI server
        '''
        request = list()
        size = 0
        for elem in [function, user or "", password or "", target, switch]:
            if elem is not None:
                elem = self._str_len_hex(elem)
                size += len(elem)
                request.append(elem)
        request.insert(0, self._hxint4(int(size / 2)))
        return self._s2hex(self._hxdmp_to_str(''.join(request)))


if __name__ == '__main__':
    smiucv = SMIUCV()
    print(smiucv("SSI_Query", user="", password="", target="linux175"))
