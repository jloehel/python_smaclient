#!/usr/bin/env python

import uuid

class SMAPI_Call(object):

  def __init__(self, name, request, response1, response2):
    self._uuid = uuid.uuid1()
    self._name = name
    self._request = request
    self._response1 = response1
    self._response2 = response2
