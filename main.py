import pyshark



capture = pyshark.LiveCapture(display_filter='eth.addr[0:3]==1C:82:59')


for packet in capture.sniff_continuously(packet_count=20):
   try:
        print(packet[1].src)
   except:
       pass
