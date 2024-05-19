from netmiko import ConnectHandler
import ipaddress
import sys
from hosts_list import *
from pprint import pprint
import getpass

# Запись ввода с терминала
def user_input():
    global ip_input, username, password
    ip_input = input("Enter an IP to block (ip or ip/prefix or ip mask): ")
    username = input('username: ')
    password = getpass.getpass('password: ')

# Валидация на правильность ввода айпи/айпи+маски/айпи+префикса
def validate_network():
    global ip_check
    try:
        # Валидация айпи+префикса
        if '/' in ip_input:
            network = ipaddress.ip_network(ip_input, strict=False)
            print(f"'{ip_input}' is a valid IP network: {network}\n")
            ip_check = 'prefix'
        # Валидация айпи
        elif len(ip_input.split()) !=2:
            ip = ipaddress.ip_address(ip_input)
            print(f"'{ip_input}' is a valid IP address: {ip}\n")
            ip_check = 'host'
        else:
        # Валидация айпи+маски
            network_str, subnet_mask_str = ip_input.split()
            network = ipaddress.IPv4Network(f"{network_str}/{subnet_mask_str}", strict=False)
            print(f"'{ip_input}' is a valid IPv4 network: {network}\n")
            ip_check = 'mask'
    # Выход из программы в случае провала валидации
    except ValueError:
        print("Invalid input format. Please use 'IP_ADDRESS SUBNET_MASK'.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit()  
    # Преобразование адреса в текст и его возврат   
    return str(ip_input)

# Создание списка команд
def create_commands(ip_input):
        # Создание списка команд для единичного айпи
        if ip_check == 'host':
            commands = [ 
                'object-group network BLACK-LIST', 
                f'network-object host {ip_input}',
            ]
        # Создание списка команд для айпи+префикса
        elif ip_check == 'prefix':
            # Преобразование префикса в айпи+маска
            network = ipaddress.IPv4Network(ip_input, strict=False)
            network_address = str(network.network_address)
            subnet_mask = str(network.netmask)
            if subnet_mask == "255.255.255.255":
                ip_input = network_address
                commands = [ 
                'object-group network BLACK-LIST', 
                f'network-object host {ip_input}',]
            else:
                ip_input = network_address + " " + subnet_mask
                commands = [ 
                'object-group network BLACK-LIST', 
                f'network-object {ip_input}',]
        # Создание списка команд для айпи+маски
        else:
            commands = [ 
                'object-group network BLACK-LIST', 
                f'network-object {ip_input}',
            ]
        return commands  

# Преобразование айпи+маски всех входящих в подсеть с префиксом айпи адресов в range вида 'StartIP-EndIP'
def calculate_ip_range(ip_with_prefix):
            try:
                network = ipaddress.IPv4Network(ip_with_prefix, strict=False)
                first_ip = network.network_address + 1
                last_ip = network.broadcast_address - 1
                ip_range = f"{first_ip}-{last_ip}"
            except ValueError:
                return "Invalid input format"
            return ip_range

# Преобразование айпи+маски всех входящих в подсеть с маской айпи адресов в range вида 'StartIP-EndIP'
def generate_ip_range(ip_mask):
            try:
                ip, mask = ip_mask.split()
                network = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False)
                first_ip = network.network_address + 1
                last_ip = network.broadcast_address - 1
                ip_range = f"{first_ip}-{last_ip}"
                return ip_range
            except ValueError:
                return "Invalid input format. Please provide IP address and mask separated by a space."

# Ввод сгенерированной конфигурации в хосты
def configure(commands, ip):
    # Оформление терминала
    print ("============= FIREWALLS LIST =============")
    for list_host in host_configurations:
         print(list_host)
    print ("============= END OF FIREWALLS LIST =============\n")
    print ("============= START OF CONFIG =============")
    for command in commands:
        print (command)
    print ("============= END OF CONFIG =============\n")
    # Подтверждение ввода конфига
    agreement = input('Вводим эту конфигурацию? Введи Y или y, если да \n')
    if agreement=='Y' or agreement == 'y':
        try:
            # Ввод конфига
            for host in host_configurations:
                print(f"Connecting to {host}...")
                # Настройки хостов
                device = {
                    "device_type": "cisco_asa",  # Указывается тип устройства, этот подходит только для asa
                    "ip": host,
                    "username": username,
                    "password": password,
                }
                # Подключение к хосту
                ssh_client = ConnectHandler(**device)
                ssh_client.send_command('configure terminal', expect_string=r'#')
                output = ssh_client.send_config_set(commands)
                print(output)
                output2 = ssh_client.send_command(f'clear conn address {ip}\n')
                print ("clearing connections...")
                print(output2)
                # Закрытие сессии
                ssh_client.save_config()
                ssh_client.disconnect()
                print(f"\nFinished configuring {host}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print ("\nНа нет и суда нет!\n")
        sys.exit()
    

# Исполнение программы
def main():
    user_input() # Запись ввода с терминала
    ip_to_block = validate_network() # Забираем валидированный айпи/айпи+подсеть
    commands_to_push = create_commands(ip_to_block) # Создаём конфигурацию для пуша и вставляем валидированный айпи/айпи+подсеть
    # Выборка правильного синтаксиса для 'clear conn address XXXX' и далее ввод конфигурации
    if ip_check == 'host':
        configure(commands_to_push, ip_to_block)
    elif ip_check == 'prefix':
        configure(commands_to_push, calculate_ip_range(ip_to_block))
    elif ip_check == 'mask':
        configure(commands_to_push, generate_ip_range(ip_to_block))
    else:
        print ("ip_check from commands function did not work")
        sys.exit()

if __name__ == '__main__':
    main()
