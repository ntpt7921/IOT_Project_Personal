def connected(client):
    print("Ket noi thanh cong ...")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
