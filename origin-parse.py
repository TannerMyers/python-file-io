#! /usr/bin/env python3

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening origin-output.txt')
    with open('origin-output.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                out_stream.write('{0}\n'.format(word))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('origin-output.txt is closed?', out_stream.closed)