import time

class Packet:
    # Packet class for simulating a packet to be transmitted.
    def __init__(self, id, size):  # Fixed the constructor
        # Initialize class variables.
        self.id = id
        self.size = size

    def getSize(self):
        return self.size

    def getId(self):
        return self.id

class LeakyBucket:
    def __init__(self, leakRate, size):  # Fixed the constructor
        self.leakRate = leakRate
        self.bufferSizeLimit = size
        self.buffer = []
        self.currBufferSize = 0

    def addPacket(self, newPacket):
        if self.currBufferSize + newPacket.getSize() > self.bufferSizeLimit:
            # If the packet cannot fit in the buffer, then reject the packet.
            print("Bucket is full. Packet rejected.")
            return
        # Add packet to the buffer.
        self.buffer.append(newPacket)
        # Update current Buffer Size.
        self.currBufferSize += newPacket.getSize()
        # Print out the appropriate message.
        print("Packet with id = " + str(newPacket.getId()) +  " added to bucket.")

    def transmit(self):
        # Function to transmit packets. Called at each clock tick.
        if len(self.buffer) == 0:
            # Check if there is a packet in the buffer.
            print("No packets in the bucket.")
            return False  # Return False when no packets are left

        # Initialize n to the leak rate.
        n = self.leakRate
        while len(self.buffer) > 0:
            topPacket = self.buffer[0]
            topPacketSize = topPacket.getSize()
            # Check if the packet can be transmitted or not.
            if topPacketSize > n:
                break
            # Reduce n by the packet size that will be transmitted.
            n = n - topPacketSize
            # Update the current buffer size.
            self.currBufferSize -= topPacketSize
            # Remove packet from buffer.
            self.buffer.pop(0)
            print("Packet with id = " + str(topPacket.getId()) + " transmitted.")
        return True  # Return True if packets remain

if __name__ == '__main__':
    bucket = LeakyBucket(1000, 10000)
    bucket.addPacket(Packet(1, 200))
    bucket.addPacket(Packet(2, 500))
    bucket.addPacket(Packet(3, 400))
    bucket.addPacket(Packet(4, 500))
    bucket.addPacket(Packet(5, 200))
    
    while True:
        has_packets = bucket.transmit()
        if not has_packets:
            break  # Exit the loop if no packets are left
        print("Waiting for next tick.")
        time.sleep(1)

