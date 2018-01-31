# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import asr_service_pb2 as asr__service__pb2


class ASRStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Recognize = channel.stream_stream(
        '/sarmata.ASR/Recognize',
        request_serializer=asr__service__pb2.RecognizeRequest.SerializeToString,
        response_deserializer=asr__service__pb2.RecognizeResponse.FromString,
        )
    self.DefineGrammar = channel.unary_unary(
        '/sarmata.ASR/DefineGrammar',
        request_serializer=asr__service__pb2.DefineGrammarRequest.SerializeToString,
        response_deserializer=asr__service__pb2.DefineGrammarResponse.FromString,
        )


class ASRServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Recognize(self, request_iterator, context):
    """recognizes speech in stream using given grammar
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DefineGrammar(self, request, context):
    """defines user-persistent grammar
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ASRServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Recognize': grpc.stream_stream_rpc_method_handler(
          servicer.Recognize,
          request_deserializer=asr__service__pb2.RecognizeRequest.FromString,
          response_serializer=asr__service__pb2.RecognizeResponse.SerializeToString,
      ),
      'DefineGrammar': grpc.unary_unary_rpc_method_handler(
          servicer.DefineGrammar,
          request_deserializer=asr__service__pb2.DefineGrammarRequest.FromString,
          response_serializer=asr__service__pb2.DefineGrammarResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sarmata.ASR', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
