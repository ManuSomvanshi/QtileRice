import pydbus

bus = pydbus.SystemBus()

adapter = bus.get('org.bluez', '/org/bluez/hci0')
mngr = bus.get('org.bluez', '/')

def list_connected_devices():
    mngd_objs = mngr.GetManagedObjects()
    dev_path = ""
    for path in mngd_objs:
        con_state = mngd_objs[path].get('org.bluez.Device1', {}).get('Connected', False)
        if con_state:
            addr = mngd_objs[path].get('org.bluez.Device1', {}).get('Address')
            dev = f'{addr}'
            dev_path = '/dev_' + '_'.join(dev.split(':'))
            return dev_path
        else:
            dev_path = "/dev_74_45_CE_B4_54_E3"
    return dev_path

#print(list_connected_devices())
