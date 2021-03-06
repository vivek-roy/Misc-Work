
FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def hexdump(src, length=16, prefix=''):
    """
        Print hexdump of string
    """
    n = 0
    left = length / 2 
    right = length - left
    result= []
    while src:
        s,src = src[:length],src[length:]
        l,r = s[:left],s[left:]
        hexa = "%-*s" % (left*3,' '.join(["%02x"%ord(x) for x in l]))
        hexb = "%-*s" % (right*3,' '.join(["%02x"%ord(x) for x in r]))
        lf = l.translate(FILTER)
        rf = r.translate(FILTER)
        result.append("%s%04x  %s %s %s %s" % (prefix, n, hexa, hexb, lf, rf))
        n += length
    return "\n".join(result)

def get_bits(data,offset,bits=1):
    """
        Get specified bits from integer
    """
    mask = ((1 << bits) - 1) << offset
    return (data & mask) >> offset 

def set_bits(data,value,offset,bits=1):
    """
        Set specified bits in integer
    """
    mask = ((1 << bits) - 1) << offset
    clear = 0xffff ^ mask
    data = (data & clear) | ((value << offset) & mask)
    return data

def binary(n,count=16,reverse=False):
    """
        Display n in binary (only difference from built-in `bin` is
        that this function returns a fixed width string and can
        optionally be reversed
    """
    bits = [str((n >> y) & 1) for y in range(count-1, -1, -1)]
    if reverse:
        bits.reverse()
    return "".join(bits)

