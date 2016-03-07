#!/usr/bin/env python

from construct import Struct, UBInt32, String, Field
import yaml

class SMAPI_Parser(object):

    def __init__(self, config_path):
        self._configuration = self.load_configuration(config_path)
        self._smapi_request_struct = Struct("SMAPI_REQUEST",
            UBInt32("input_length"),
            UBInt32("function_name_length"),
            String("function_name", lambda ctx: ctx.function_name_length),
            UBInt32("authenticated_userid_length"),
            String("authenticated_userid", lambda ctx: ctx.authenticated_userid_length),
            UBInt32("password_length"),
            String("password", lambda ctx: ctx.password_length),
            UBInt32("target_identifier_length"),
            String("target_identifier", lambda ctx: ctx.target_identifier_length),
            Field("additional_parameters", lambda ctx: (ctx.input_length -
                                                        (ctx.function_name_length +
                                                         ctx.authenticated_userid_length +
                                                         ctx.password_length +
                                                         ctx.target_identifier_length + 4 * 4)))
        )
        self._smapi_response_1_struct = Struct("SMAPI_RESPONSE_1", UBInt32("request_id"))
        self._smapi_response_2_struct = Struct("SMAPI_RESPONSE_2",
            UBInt32("output_length"),
            UBInt32("request_id"),
            UBInt32("return_code"),
            UBInt32("reason_code"),
            Field("additional_parameters", lambda ctx: ctx.output_length - 16)
        )

    def load_configuration(self, path):
        with open(path, "r") as stream:
            return yaml.load(stream)

    def get_configuration(self):
        return self._configuration

    def parse(self, response):
        pass

    def build_request(self, container):
        return self._smapi_request_struct.build(container)
