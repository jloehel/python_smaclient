#!/usr/bin/env python

import uuid
from construct import Container


class SMAPI_Request(object):
    '''
        Implentation of a ICUV Request
    '''

    def __init__(self, function_name, target_identifier,
                 authenticated_userid=b"", password=b"", additional_parameters=b""):
        self._function_name = function_name
        self._function_name_length = len(function_name)
        self._authenticated_userid = authenticated_userid
        self._authenticated_userid_length = len(authenticated_userid)
        self._password = password
        self._password_length = len(password)
        self._target_identifier = target_identifier
        self._target_identifier_length = len(target_identifier)
        self._additional_parameters = additional_parameters
        self._additional_parameters_length = len(additional_parameters)
        self._input_length = (self._function_name_length + 4 +
                              self._authenticated_userid_length + 4 +
                              self._password_length + 4 +
                              self._target_identifier_length + 4 +
                              self._additional_parameters_length)

    def get_container(self):
        return Container(input_length = self._input_length,
                         function_name_length = self._function_name_length,
                         function_name = self._function_name,
                         authenticated_userid_length = self._authenticated_userid_length,
                         authenticated_userid = self._authenticated_userid,
                         password_length = self._password_length,
                         password = self._password,
                         target_identifier_length = self._target_identifier_length,
                         target_identifier = self._target_identifier,
                         additional_parameters = self._additional_parameters)

    def __repr__(self):
        "<{} (container={})>".format(
            self.__class__.__name__,
            self.get_container())
