import signal
import sys
import time

import gspread


def get_data():
    lab_temp = 21.0  # Placeholder until sensors arrive
    lab_hum = 65.5
    glove_box_temp = 19.2
    glove_box_hum = 33.2
    glove_box_pressure = 1000  # Probably in millibar/hPa, would be most logical

    return ['=NOW()', lab_temp, '=CONVERT(B2, "C", "F")', lab_hum, glove_box_temp, '=CONVERT(E2, "C", "F")', glove_box_hum, glove_box_pressure, '=(H2-1013.25) / 2.488']


def signal_handler(sig, frame):
    print('Exiting script...')
    sys.exit(0)


loop_frequency = 3  # Seconds between each upload
signal.signal(signal.SIGINT, signal_handler)
gc = gspread.service_account(filename='service_account.json')  # Held locally

# Data will be entered in this worksheet, and visualized in another one
data_sheet = gc.open("Test API Spreadsheet").worksheet("Raw Data")


while True:
    data_sheet.insert_row(get_data(), 2, value_input_option="USER_ENTERED")
    data_sheet.update('A2', data_sheet.get('A2'))

    time.sleep(loop_frequency - time.time() % loop_frequency)
