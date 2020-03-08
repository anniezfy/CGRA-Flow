"""
==========================================================================
Comp.py
==========================================================================
Functional unit for performing comparison.

Author : Cheng Tan
  Date : December 2, 2019

"""

from pymtl3 import *
from pymtl3.stdlib.ifcs import SendIfcRTL, RecvIfcRTL
from ...lib.opt_type    import *
from ..basic.Fu         import Fu

class Comp( Fu ):

  def construct( s, DataType, ConfigType, num_inports, num_outports,
                 data_mem_size ):

    super( Comp, s ).construct( DataType, ConfigType, num_inports, num_outports,
           data_mem_size )

    # data:      s.recv_in[0]
    # reference: s.recv_in[1]

    @s.update
    def comb_logic():
      predicate = s.recv_in[0].msg.predicate & s.recv_in[1].msg.predicate
      for j in range( num_outports ):
        s.send_out[j].en = s.recv_opt.en# and s.send_out[j].rdy and s.recv_in[0].en and s.recv_in[1].en
      if s.recv_opt.msg.ctrl == OPT_EQ:
        if s.recv_in[0].msg.payload == s.recv_in[1].msg.payload:
          s.send_out[0].msg = DataType( 1, predicate )
        else:
          s.send_out[0].msg = DataType( 0, predicate )
      elif s.recv_opt.msg.ctrl == OPT_LE:
        if s.recv_in[0].msg.payload < s.recv_in[1].msg.payload:
          s.send_out[0].msg = DataType( 1, predicate )
        else:
          s.send_out[0].msg = DataType( 0, predicate )
      else:
        for j in range( num_outports ):
          s.send_out[j].en = b1( 0 )
#      print("s.send_out: ", s.send_out[0].msg)

