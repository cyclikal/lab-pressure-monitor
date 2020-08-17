import signal
import sys
import time
import sensor_data
#from wifi_handler import WLAN_check
import gspread

'''
# Placeholder until sensors arrive, sensor_data
def get_data():
    lab_temp = random.uniform(20.0, 24.0)
    lab_hum = random.uniform(40.0, 55.0)
    glove_box_temp = random.uniform(20.0, 23.0)
    glove_box_hum = random.uniform(15.0, 30.0)
    # Probably in millibar/hPa, would be most logical
    glove_box_pressure = random.uniform(1013.25, 1025.0)

    return ['=TEXT(NOW(),"yyyy/mm/dd")', '=TEXT(NOW(),"hh:mm:ss")', lab_temp, '=CONVERT(C2, "C", "F")', lab_hum, glove_box_temp, '=CONVERT(F2, "C", "F")', glove_box_hum, glove_box_pressure, '=(I2-1013.25) / 2.488']
'''

def signal_handler(sig, frame):
    data_sheet.update('A2', data_sheet.get(
        'A2'), value_input_option="USER_ENTERED")
    data_sheet.update('B2', data_sheet.get(
        'B2'), value_input_option="USER_ENTERED")
    print('Exiting script...')
    sys.exit(0)


start_time = time.time()
loop_frequency = 30  # Seconds between each upload
signal.signal(signal.SIGINT, signal_handler)
gc = gspread.service_account(filename='service_account.json')  # Held locally

# Data will be entered in this worksheet, and visualized in another one
data_sheet = gc.open("Lab Monitor Data").worksheet("Raw Data")

sensor_data.connect()

while True:    
    try:
        data_sheet.insert_row(sensor_data.get_data(), 2, value_input_option="USER_ENTERED")
    except:
        print("Sensor error! Likely not connected, either electrically or i2c.")
    else:
        data_sheet.update('A2', data_sheet.get(
            'A2'), value_input_option="USER_ENTERED")
        data_sheet.update('B2', data_sheet.get(
            'B2'), value_input_option="USER_ENTERED")
        print(time.time() - start_time)
        start_time = time.time()

        time.sleep(loop_frequency - time.time() % loop_frequency)
