import serial.tools.list_ports as serial_port_list
import tomli

with open("../config.toml", "rb") as config_file:
    config = tomli.load(config_file)
uart_cfg = config['UART']

combined_pattern = '|'.join(uart_cfg['device_name_regex'])

def getSerialPortList(*, pattern = combined_pattern):
    return [port for port in serial_port_list.grep(pattern)]

print("List of port matching pattern:")
print(getSerialPortList())
