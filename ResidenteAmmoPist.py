from ReadWriteMemory import ReadWriteMemory
from pymem.process import *

pm = pymem.Pymem('Resident Evil Village Crisis.exe')

baseaddres = module_from_name(pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll

static_addres_offset = 0x0039FC60

pointer_static_addres = baseaddres + static_addres_offset

offsets = [0x2C, 0xED8, 0x1C, 0xC, 0x5C, 0x18, 0xD0]

rwm = ReadWriteMemory()

process = rwm.get_process_by_name('Resident Evil Village Crisis.exe')
process.open()

my_pointer = process.get_pointer(pointer_static_addres, offsets=offsets)

pointer_value = process.read(my_pointer)

print(f"valor atual = {pointer_value}")

value_to_set = int(input("Qual numero de balas da pistola voce quer ficar : "))

process.write(my_pointer, value_to_set)


