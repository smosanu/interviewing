## Author: Sergiu Mosanu, 3/29/2023

# 1. Write a class for least recently used (LRU) cache with input as capacity and implement the general methods needed (put and get)

# LRU cache, fully associative, write-allocate (write back not implemented)
class LRUFACache:
    def __init__(self, capacity: int):
        # my cache uses a fixed sized array for the data (wanted to keep it basic)
        # plus stores the tag, and valid/dirty bits
        # it is fully associative, i.e. we only have tag and offset bits
        self.capacity = capacity # capacity as in "number of blocks"
        self.data = [0] * capacity
        self.tag = [0] * capacity
        self.valid = [False] * capacity
        self.dirty = [False] * capacity
        self.order = [0] * capacity # to keep track of order
        for i in range(capacity):
            self.order[i] = i
        self.blockSize = 2 # two Bytes per block (self.data is 2 bytes)
        # blockSize = 2 also means that offset is 1 bit and remaining address is tag

    def put(self, address, value):
        addr_tag = address >> 1
        offset = address % 2
        # if tag is in cache and valid
        for i in range(self.capacity):
            if self.tag[i] == addr_tag and self.valid[i]:
                self.data[i] += value << offset*8
                self._updateOrder(i)
                return
        # if tag not in cache or not valid
        # find LRU (order == 0) and use that location
        for i in range(self.capacity):
            if self.order[i] == 0:
                if self.dirty[i]:
                    self.data[i] = 0 # reset value
                    self._write_back()
                    self._allocate()
                self.data[i] += value << offset*8
                self.valid[i] = True
                self.dirty[i] = True
                self.tag[i] = addr_tag
                self._updateOrder(i)
                return

    def get(self, address):
        addr_tag = address >> 1
        offset = address % 2
        # find if tag is in cache and valid
        for i in range(self.capacity):
            if self.tag[i] == addr_tag and self.valid[i]:
                self._updateOrder(i)
                return (self.data[i] >> offset*8) & 0xFF
        self._allocate()
    
    def _write_back(self):
        print("write back")
    def _allocate(self):
        print("allocate")

    def _updateOrder(self, newest):
        for i in range(self.capacity):
            # only the order values higher than the one being updated need to be decremented
            if self.order[i] > self.order[newest]:
                self.order[i] -= 1
        self.order[newest] = self.capacity - 1

    def debugData(self):
        return self.data
    def debugTag(self):
        return self.tag
    def debugValid(self):
        return self.valid
    def debugDirty(self):
        return self.dirty
    def debugOrder(self):
        return self.order

mycache = LRUFACache(3) # init a cache
mycache.put(5,5) # put value 5 at address 5 = b101
mycache.put(4,4) # put value 4 at address 4 = b100 (dirty, hit)
print("get value at address 5:", mycache.get(5))
print("get value at address 4:", mycache.get(4))
mycache.put(6,6)
mycache.put(2,2)
print("debug oder values:", mycache.debugOrder())
print("put a 4th value, replacing the LRU block")
mycache.put(8,8) # will replace last accessed
print("debug data values:", mycache.debugData())
print("get value at address 5 (replaced):", mycache.get(5))
print("get value at address 4 (replaced):", mycache.get(4))
print("get value at address 6:", mycache.get(6))
print("get value at address 8:", mycache.get(8))


print("debug data values:", mycache.debugData())
print("debug tag values:", mycache.debugTag())
print("debug valid values:", mycache.debugValid())
print("debug dirty values:", mycache.debugDirty())
print("debug order values:", mycache.debugOrder())

#2. Describe in English or block diagram (if the platform allows) how the LRU cache is implemented in hardware.
# I implemented a fully associative cache
# the inputs and outputs for put and get (write and read) are the address and the value (wires)
# the address is split into tag and offset (in my case there are 2 bytes per block, so 1 bit offset)
# the cache data, tag data, valid and dirty bits, and the LRU data bits are all implemented in SRAM and registers
# to determine a hit, the address tag has to be compared with each tag in the cache and also check for the valid bit to be True
# the circuit of a hit read/write can be implemented with multple tag comparators in parallel ANDed with the value of the valid bit
# since only one tag hit will happen at any time, the results of the above ANDs can be XORed
# similarly, the results of the ANDs can be concatenated to control a MUX/DeMUX to control from which block to read or to which block to write
# during a miss, data will be fetched from main memory into the cache into the row that was least recently used, which in my implementation has a "order" value of 0
# this is quite expensive in hardware, because we have to keep track of the order of all tags and update that order at each read and write
# in my implementation, I decrement the oder value by 1 when it is used, and set the currenly used value to capacity (highest) {there is an additional condition, to avoid decrementing below 0}
# an ORreduce can be used to find the block with oder 0 and a MUX can be used to write to that block tag and data values