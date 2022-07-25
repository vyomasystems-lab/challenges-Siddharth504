# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
from array import *

#acting as an reference model similar to mux,whose o/p is selected on basis of sel signal
#a/c to design,for sel value 12,13,30 it should throw error
#for sel value 13 and 30 sepearate test is designed
#for sel value 12 ,it is defined in randomised test ,whenever sel value come 2 it will throw error
inp_arr =array('i',[0]*32)

for i in range(0,32):
    if i == 31 :
        inp_arr[i] = 0
    else:
        inp_arr[i] = (i % 3) + 1

# below input in 1,2,3 in circular loop fashion is assigned to input pins
@cocotb.test()
async def randomised_test_mux(dut):    
    dut.inp0.value = 1
    dut.inp1.value = 2
    dut.inp2.value = 3
    dut.inp3.value = 1
    dut.inp4.value = 2
    dut.inp5.value = 3
    dut.inp6.value = 1
    dut.inp7.value = 2
    dut.inp8.value = 3
    dut.inp9.value = 1
    dut.inp10.value = 2
    dut.inp11.value = 3
    dut.inp12.value = 1
    dut.inp13.value = 2
    dut.inp14.value = 3
    dut.inp15.value = 1
    dut.inp16.value = 2
    dut.inp17.value = 3
    dut.inp18.value = 1
    dut.inp19.value = 2
    dut.inp20.value = 3
    dut.inp21.value = 1
    dut.inp22.value = 2
    dut.inp23.value = 3
    dut.inp24.value = 1
    dut.inp25.value = 2
    dut.inp26.value = 3
    dut.inp27.value = 1
    dut.inp28.value = 2
    dut.inp29.value = 3
    dut.inp30.value = 1
    
    dut._log.info(f'inp1  = {0} inp1 = {1} inp2 = {2} inp3 = {3} inp4  = {0} inp5 = {1} inp6 = {2} inp7 = {3} inp8  = {0} inp9 = {1} inp10 = {2} inp11 = {3} inp12 = {0} inp13 = {1} inp14 = {2} inp15 = {3} inp16 = {0} inp17 = {1} inp18 = {2} inp19 = {3} inp20 = {0} inp21 = {1} inp22 = {2} inp23 = {3} inp24 = {0} inp25 = {1} inp26 = {2} inp27 = {3} inp28 = {0} inp29 = {1} inp30 = {2} inp31 = {3} ')

    for i in range(32):
        sel = random.randint(0, 31)
        dut.sel.value = sel

        await Timer(2, units='ns')

        dut._log.info(f' sel = {sel}  DUT={int(dut.out.value)}')
        expected_output = inp_arr[sel]
        assert dut.out.value == expected_output, "Randomised test failed with: Sel = {sel} expected_value = {exp} , DUT_output = {out}".format(
            sel = sel ,exp = expected_output, out=dut.out.value)


@cocotb.test()
async def test_mux_bug1(dut):

    dut.inp0.value = 1
    dut.inp1.value = 2
    dut.inp2.value = 3
    dut.inp3.value = 1
    dut.inp4.value = 2
    dut.inp5.value = 3
    dut.inp6.value = 1
    dut.inp7.value = 2
    dut.inp8.value = 3
    dut.inp9.value = 1
    dut.inp10.value = 2
    dut.inp11.value = 3
    dut.inp12.value = 1
    dut.inp13.value = 2
    dut.inp14.value = 3
    dut.inp15.value = 1
    dut.inp16.value = 2
    dut.inp17.value = 3
    dut.inp18.value = 1
    dut.inp19.value = 2
    dut.inp20.value = 3
    dut.inp21.value = 1
    dut.inp22.value = 2
    dut.inp23.value = 3
    dut.inp24.value = 1
    dut.inp25.value = 2
    dut.inp26.value = 3
    dut.inp27.value = 1
    dut.inp28.value = 2
    dut.inp29.value = 3
    dut.inp30.value = 1
    
    dut._log.info(f'inp0  = {1} inp1 = {2} inp2 = {3} inp3 = {1} inp4  = {2} inp5 = {3} inp6 = {1} inp7 = {2} inp8  = {3} inp9 = {1} inp10 = {2} inp11 = {3} inp12 = {1} inp13 = {2} inp14 = {3} inp15 = {1} inp16 = {2} inp17 = {3} inp18 = {1} inp19 = {2} inp20 = {3} inp21 = {1} inp22 = {2} inp23 = {3} inp24 = {1} inp25 = {2} inp26 = {3} inp27 = {1} inp28 = {2} inp29 = {3} inp30 = {1} inp31 = {0} ')

    sel = 13
    dut.sel.value = sel
    await Timer(2, units='ns')

    dut._log.info(f' sel = {sel}  DUT={int(dut.out.value)}')
    expected_output = inp_arr[sel]
    assert dut.out.value == expected_output, "test_bug1 failed with: Sel = {sel} expected_value = {exp} , DUT_output = {out}".format(
            sel = sel ,exp = expected_output, out=dut.out.value)

@cocotb.test()
async def test_mux_bug2(dut):

    dut.inp0.value = 1
    dut.inp1.value = 2
    dut.inp2.value = 3
    dut.inp3.value = 1
    dut.inp4.value = 2
    dut.inp5.value = 3
    dut.inp6.value = 1
    dut.inp7.value = 2
    dut.inp8.value = 3
    dut.inp9.value = 1
    dut.inp10.value = 2
    dut.inp11.value = 3
    dut.inp12.value = 1
    dut.inp13.value = 2
    dut.inp14.value = 3
    dut.inp15.value = 1
    dut.inp16.value = 2
    dut.inp17.value = 3
    dut.inp18.value = 1
    dut.inp19.value = 2
    dut.inp20.value = 3
    dut.inp21.value = 1
    dut.inp22.value = 2
    dut.inp23.value = 3
    dut.inp24.value = 1
    dut.inp25.value = 2
    dut.inp26.value = 3
    dut.inp27.value = 1
    dut.inp28.value = 2
    dut.inp29.value = 3
    dut.inp30.value = 1
    
    dut._log.info(f'inp1  = {0} inp1 = {1} inp2 = {2} inp3 = {3} inp4  = {0} inp5 = {1} inp6 = {2} inp7 = {3} inp8  = {0} inp9 = {1} inp10 = {2} inp11 = {3} inp12 = {0} inp13 = {1} inp14 = {2} inp15 = {3} inp16 = {0} inp17 = {1} inp18 = {2} inp19 = {3} inp20 = {0} inp21 = {1} inp22 = {2} inp23 = {3} inp24 = {0} inp25 = {1} inp26 = {2} inp27 = {3} inp28 = {0} inp29 = {1} inp30 = {2} inp31 = {3} ')

    sel = 30
    dut.sel.value = sel
    await Timer(2, units='ns')

    dut._log.info(f' sel = {sel}  DUT={int(dut.out.value)}')
    expected_output = inp_arr[sel]
    assert dut.out.value == expected_output, "test_bug2 failed with: Sel = {sel} expected_value = {exp} , DUT_output = {out}".format(
            sel = sel ,exp = expected_output, out=dut.out.value)
