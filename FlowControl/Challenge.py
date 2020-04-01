prompt = "Please enter an IP address. An IP address consists of 4 numbers," \
         "separated from each other with a full stop: "

ipAddress = input(prompt)

segment = 1
segment_length = 0

if ipAddress[-1] != '.':
    ipAddress += '.'

if ipAddress != '':
    for character in ipAddress:
        if character == '.':
            print("Segment {} contains {} characters".format(segment, segment_length))
            segment += 1
            segment_length = 0
        else:
            segment_length += 1

    # Unless the final character in the string was a . then we haven't printed the last_segment
    if character != '.':
        print("Segment {} contains {} characters".format(segment, segment_length))
else:
    print('Please enter a valid ipAddress')
