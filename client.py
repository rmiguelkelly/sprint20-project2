#!/usr/bin/env python3

import sys
import confundo

# Example how to use the provided confundo.Header class
pkt = confundo.Header()
pkt.seqNum = 42
pkt.ackNum = 0
pkt.isAck = False
pkt.isSyn = True
pkt.isFin = False

encodedHeader = pkt.encode()
payload = b"sample-buffer"
fullPacket = encodedHeader + payload

print(encodedHeader)
print(fullPacket)

if __name__ == '__main__':
    sys.stderr.write("client is not implemented yet\n")
