import argparse
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
   


def main():
    parser_formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(
            description = 'Packet Analysis Study Quiz (TODO: better description)',
            formatter_class=parser_formatter)

    parser.add_argument('--filename', required=True, action='store',
            dest='filename', help='pcap file used to quiz')

    parser.add_argument('--number', required=False, action='store',
            dest='number', type=int, default=True, help='Displays Header Reference for question')
  

    args = parser.parse_args()

    print(args.filename, args.number)
    
    output=fibonacci(args.number)
    print(output)

    f = open(args.filename, "w")
    f.write(str(output))
    f.close()

if __name__ == '__main__':
    main()