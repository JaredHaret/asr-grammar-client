# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import sarmata_asr_pb2 as sarmata__asr__pb2


class ASRStub(object):
  """Service that implements Techmo ASR API.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Recognize = channel.stream_stream(
        '/techmo.sarmata.ASR/Recognize',
        request_serializer=sarmata__asr__pb2.RecognizeRequest.SerializeToString,
        response_deserializer=sarmata__asr__pb2.RecognizeResponse.FromString,
        )
    self.DefineGrammar = channel.unary_unary(
        '/techmo.sarmata.ASR/DefineGrammar',
        request_serializer=sarmata__asr__pb2.DefineGrammarRequest.SerializeToString,
        response_deserializer=sarmata__asr__pb2.DefineGrammarResponse.FromString,
        )


class ASRServicer(object):
  """Service that implements Techmo ASR API.
  """

  def Recognize(self, request_iterator, context):
    """Performs bidirectional streaming speech recognition using given grammar.
    Receive results while sending audio.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DefineGrammar(self, request, context):
    """Defines grammar that will be stored for future use in recognitions
    requested by `Recognize`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ASRServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Recognize': grpc.stream_stream_rpc_method_handler(
          servicer.Recognize,
          request_deserializer=sarmata__asr__pb2.RecognizeRequest.FromString,
          response_serializer=sarmata__asr__pb2.RecognizeResponse.SerializeToString,
      ),
      'DefineGrammar': grpc.unary_unary_rpc_method_handler(
          servicer.DefineGrammar,
          request_deserializer=sarmata__asr__pb2.DefineGrammarRequest.FromString,
          response_serializer=sarmata__asr__pb2.DefineGrammarResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'techmo.sarmata.ASR', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))