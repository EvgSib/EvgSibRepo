


def ip_examination(ip_mask):
    ip_address, mask = ip_mask.split('/')
    octets = ip_address.split(".")
    correct_ip, correct_mask = [True,True]

    if len(octets) != 4:
        correct_ip = False
    elif not 8 < int(mask) < 32:
        correct_mask = False
    else:
        for octet in octets:
            # тут второе условие int(octet) in range(256)
            # проверяется только в том случае, если первое условие истина
            # Если встретился хоть один октет с нарушением,
            # дальше можно не смотреть
                if not (octet.isdigit() and int(octet) in range(256)):
                    correct_ip = False
                    break

    if not correct_ip:
        raise ValueError(f"Неправильнo задан IP-адрес {ip_address}")
    elif not correct_mask:
        raise ValueError(f"Неправильнo задана маска {mask}")
    else:
        return print("Данные указаны верно", ip_address, mask)

if __name__ == "__main__":
    print(ip_examination('10.1.1.111/24'))