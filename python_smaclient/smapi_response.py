#!/usr/bin/env python

import uuid


class SMAPI_Response(object):
    '''
        Implentation of a ICUV Request
    '''

    def __init__(self, output_parameters):
        self._uuid = uuid.uuid1()
        self._date = None
        self._output_parameters = output_parameters

    def get_output_parameters(self):
        return self._output_parameters

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def __repr__(self):
        "<{} (name={}, input parameters={})>".format(
            self.__class__.__name__,
            self.name,
            self._output_parameters)
