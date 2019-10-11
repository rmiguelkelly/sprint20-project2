import struct

class Header:
    seqNum = 0
    ackNum = 0 
    connId = 0
    isAck = False
    isSyn = False
    isFin = False

    def encode(self):
        flags = 0
        if self.isAck:
            flags = flags | (1 << 2)
        if self.isSyn:
            flags = flags | (1 << 1)
        if self.isFin:
            flags = flags | (1)
        return struct.pack("!IIHH",
                           self.seqNum, self.ackNum,
                           self.connId, flags)

    def decode(self, packet):
        (self.seqNum, self.ackNum, self.connId, flags) = struct.unpack("!IIHH", packet)
        self.isAck = flags & (1 << 2)
        self.isSyn = flags & (1 << 1)
        self.isFin = flags & (1)
