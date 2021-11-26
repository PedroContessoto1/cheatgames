from ReadWriteMemory import ReadWriteMemory
from pymem.process import *

pm = pymem.Pymem('IdleDragons.exe')

baseaddres = module_from_name(pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll

static_addres_offset = 0x003A1C68

pointer_static_addres = baseaddres + static_addres_offset

offsets = [0x150, 0xAA4, 0x34, 0xC8, 0x38, 0x98]

rwm = ReadWriteMemory()

process = rwm.get_process_by_name('IdleDragons.exe')
process.open()

my_pointer = process.get_pointer(pointer_static_addres, offsets=offsets)

pointer_value = process.read(my_pointer)

print(f"valor atual = {pointer_value}")

value_to_set = int(input("Qual valor quer por no click : "))

process.write(my_pointer, value_to_set)

