import wallaroo
import wallaroo.experimental
import json

def application_setup(args):
    global ARGS = args
    ingress = wallaroo.experimental.SourceConnectorConfig(
        "ingress",
        encoder=encode_ingress,
        decoder=decode_ingress,
        port=7100)
    egress = wallaroo.experimental.SinkConnectorConfig(
        "egress",
        encoder=encode_egress,
        decoder=decode_egress,
        port=7200)
    pipeline = (wallaroo.source("simply passing", ingress)
                .to(upperize)
                .to_sink(egress))
    return wallaroo.build_application("simply passing data", pipeline)


class Msg(object):
    def __init__(self, msg):
        self.msg = msg


@wallaroo.computation(name="upperize")
def upperize(msg):
    return Msg(ARGS[0] + msg.msg.upper())


@wallaroo.experimental.stream_message_encoder
def encode_ingress(data):
    return data


@wallaroo.experimental.stream_message_decoder
def decode_ingress(data):
    return Msg(data)


@wallaroo.experimental.stream_message_encoder
def encode_egress(data):
    return data.msg


@wallaroo.experimental.stream_message_decoder
def decode_egress(data):
    return data
