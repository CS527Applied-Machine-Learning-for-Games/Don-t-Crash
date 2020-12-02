from rl_model import RlModel
import numpy as np
import time
import sys
import json
import PIL
import PIL.ImageFilter
import datetime
import airsim

MODEL_FILENAME = 'sample_model.json'
weights_path = 'model_weights.h5'
#model = RlModel(None, False)
model = RlModel(weights_path, True)
with open(MODEL_FILENAME, 'r') as f:
    checkpoint_data = json.loads(f.read())
    model.from_packet(checkpoint_data['model'])

def get_image(car_client):
    image_response = car_client.simGetImages([ImageRequest("0", AirSimImageType.Scene, False, False)])[0]
    image1d = np.fromstring(image_response.image_data_uint8, dtype=np.uint8)
    image_rgba = image1d.reshape(108,256,4)
    image_resized = image_rgba[49:108,0:255,0:3].astype(float)
    return image_resized


def append_to_ring_buffer(item, buffer, buffer_size):
    if (len(buffer) >= buffer_size):
        buffer = buffer[1:]
    buffer.append(item)
    return buffer

def isDone(car_state, car_controls, reward):
    done = 0
    if reward < -1:
        done = 1
        pass
    if car_controls.brake == 0:
        if car_state.speed <= 5:
            pass
    return done

print('Connecting to AirSim...')
car_client = airsim.CarClient()
car_client.confirmConnection()
car_client.enableApiControl(True)
car_controls = airsim.CarControls()
print('Connected!')

state_buffer = []
state_buffer_len = 4

print('Running car for a few seconds...')
car_controls.steering = 0
car_controls.throttle = 1
car_controls.brake = 0
car_client.setCarControls(car_controls)
stop_run_time =datetime.datetime.now() + datetime.timedelta(seconds=2)
while(datetime.datetime.now() < stop_run_time):
    time.sleep(0.01)
    state_buffer = append_to_ring_buffer(get_image(car_client), state_buffer, state_buffer_len)

print('Running model')
while(True):
    state_buffer = append_to_ring_buffer(get_image(car_client), state_buffer, state_buffer_len)
    next_state, dummy = model.predict_state(state_buffer)
    next_control_signal = model.state_to_control_signals(next_state, car_client.getCarState())

    car_controls.steering = next_control_signal[0]
    car_controls.throttle = next_control_signal[1]
    car_controls.brake = next_control_signal[2]

    car_state = car_client.getCarState()
    collision_info = car_client.simGetCollisionInfo()
    if (collision_info.has_collided and car_state.speed < 2):
        car_client.reset()

    print('State = {0}, steering = {1}, throttle = {2}, brake = {3}'.format(next_state, car_controls.steering, car_controls.throttle, car_controls.brake))

    car_client.setCarControls(car_controls)

    time.sleep(0.1)


