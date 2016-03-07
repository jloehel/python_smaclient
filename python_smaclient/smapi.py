#!/usr/bin/env python

from smapi_request import SMAPI_Request as Request
from smapi_parser import SMAPI_Parser

def send(function_name, target, smhost, smport, smuser, smpass, additional_parameters):
    request = Request(str.encode(function_name),
             target_identifier = str.encode(target),
             authenticated_userid= str.encode(smuser),
             password=str.encode(smpass),
             additional_parameters=str.encode(additional_parameters))
    if smhost == "IUCV":
        parser = SMAPI_Parser("config.yaml")
        raw_command = parser.build_request(request.get_container())
        print(raw_command)
        return "response"
    else:
        pass
