from ReadWriteMemory import ReadWriteMemory
from pymem.process import *

pm = pymem.Pymem('adventure-capitalist.exe')

baseaddres = module_from_name(pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll

static_addres_offset = 0x0039B56C

pointer_static_addres = baseaddres + static_addres_offset

offsets = [0x63C, 0x14, 0x6C, 0x28, 0x1C, 0x298, 0x108]

rwm = ReadWriteMemory()

process = rwm.get_process_by_name('adventure-capitalist.exe')
process.open()

my_pointer = process.get_pointer(pointer_static_addres, offsets=offsets)

pointer_value = pm.read_double(my_pointer)

print(f"valor atual = {pointer_value}")

value_to_set = float(input("Qual valor quer por no limão : "))

pm.write_double(my_pointer, value_to_set)


