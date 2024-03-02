from homeplugav.core import HomePlugAV

def discover_devices():
    hpav = HomePlugAV(interface='your_network_interface_here')
    hpav.discover_devices()

if __name__ == "__main__":
    discover_devices()