import argparse
from handlers import ethernet_handler

from reader import Reader
from writer import Writer


def get_output_filename():
    parser = argparse.ArgumentParser(description='Sniffer catches network packets passing through the personal '
                                                 'computer, the data is stored in the file specified when the program '
                                                 'starts in pcap format (the file can be opened in Wireshark). Also '
                                                 'parsed package headers are displayed in the console. '
                                                 'This program require superuser privileges.')

    parser.add_argument('-o', '--out', help='output pcap file')
    args = parser.parse_args()

    return args.out


if __name__ == "__main__":
    reader = Reader()
    try:
        with Writer(get_output_filename()) as writer:
            while True:
                package = reader.get_package()

                writer.write(package)

                ethernet_handler.handle_ethernet(package)

    except KeyboardInterrupt:
        print("\ndone")
