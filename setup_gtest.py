#!/home/jwhite/.cache/pypoetry/virtualenvs/gtest-setup-LfEI3PIb-py3.8/bin/python3
import sys

from gtest_setup import GTestSetup
import argparse
import time
import datetime
import signal
import clipboard


def signal_handler(sig, frame):
    print_empty()
    end_time = time.time()
    end_text = generate_google_sheets_time(end_time)
    handle_google_sheets_commmand("End", end_text)
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


def handle_google_sheets_commmand(label, command):
    print_google_sheets_command(label, command)
    clipboard.copy(command)


def generate_google_sheets_time(seconds):
    return "=from_unix_epoch(" + str(seconds) + ")"


def print_google_sheets_command(label, command):
    print(label + ":\t\t" + command)


def print_empty():
    print(100 * " ", end='\r')


def print_elapsed(time_elapsed):
    print_empty()
    b = "Elapsed:\t" + str(datetime.timedelta(seconds=round(time_elapsed)))
    print(b, end='\r')


def run_stopwatch(interval_in_seconds):
    start_time = time.time()
    start_text = generate_google_sheets_time(start_time)
    handle_google_sheets_commmand("Start", start_text)
    while True:
        print_elapsed(time.time() - start_time)
        time.sleep(interval_in_seconds)


def main():
    description = "Sets up a folder for a leetcode problem w/ GTests"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("project", help="project name (no spaces)")
    parser.add_argument("-p", "--path", help="full path to project")
    parser.add_argument("-i", "--interval", help="refresh rate in seconds", default=5)
    args = parser.parse_args()

    GTestSetup(project=args.project, path=args.path).Setup()
    run_stopwatch(int(args.interval))


if __name__ == '__main__':
    main()
