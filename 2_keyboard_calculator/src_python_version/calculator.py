import time
import sys
import os
from helper import *


# ------------------------------- MAIN FUNCTION ------------------------------ #
def main ():
    keys_tracker = Keys_Tracker()
    print(f'Started, keypresses will be tracked every {interval} seconds for {session} seconds.')
    print('')
    print('------------INTERVAL STATS----------')
    while (time.time() - keys_tracker.start_time) < keys_tracker.session:
        print(f'Keypresses in {interval} seconds: ', keys_tracker.count_keypresses(keypresses))
        print(f'Top 3 keypresses: ', keys_tracker.top_n_keypresses(keypresses, n))
        print(f'Current session speed:', keys_tracker.calculate_average_speed(keypress_speed), 'characters per minute')
        keys_tracker.store_total_keypresses(keypresses)
        keypresses.clear()
        print('------------------------------------')
    #session info
    print('')
    print('------------SESSION STATS----------')
    print(f'Total keypresses: ', sum(keypresses_total))
    print(f'Top 3 keypresses: ', keys_tracker.top_n_keypresses(keypress_total_dict, n))
    print(f'Final session speed:', keys_tracker.calculate_average_speed(keypress_speed), 'characters per minute')
    print('')

if __name__ == '__main__':
    main()