from ReadWriteMemory import ReadWriteMemory
from pymem import *
from pymem.process import *
from time import sleep
import pydirectinput as py
import keyboard


def main():
    pm = pymem.Pymem('Trove.exe')
    game_module = module_from_name(pm.process_handle, 'Trove.exe').lpBaseOfDll

    # o offset da base do endereço estático da corrente de ponteiro
    static_address = 0x0104CCC8
    # pointer_static_address = base_address + static_address  # "trove.exe"+010D450C
    pointer_static_address = game_module + static_address  # "trove.exe"+0104CCC8
    offsets = [0x00, 0x58, 0x1C, 0x0C, 0x04, 0x6BC]

    rwm = ReadWriteMemory()
    while (True):
        if(keyboard.is_pressed("'")):
            while not(keyboard.is_pressed("'")):
                peixes = 0
                f = 0
                while not(peixes == 5):
                    process = rwm.get_process_by_name('Trove.exe')
                    process.open()
                    my_pointer = process.get_pointer(
                        pointer_static_address, offsets=offsets)
                    pointer_value = process.read(my_pointer)
                    print(f'Valor: {pointer_value}')
                    if(peixes == 0 and f == 0):
                        py.press('f')
                    if pointer_value == 1:
                        sleep(0.5)
                        py.press('f')
                        print('Peixe fisgado!')
                        peixes += 1
                        print(f'Peixes: {peixes}')
                        sleep(3)
                        if(peixes == 5):
                            pass
                        else:
                            py.press('f')
                    if(f == 0):
                        f = f + 1
                    sleep(1.5)
                    

if __name__ == '__main__':
    main()
