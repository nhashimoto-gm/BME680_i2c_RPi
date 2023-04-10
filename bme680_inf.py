#!/usr/bin/env python

import bme680

sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

# These oversampling settings can be tweaked to change the balance between accuracy and noise in the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

from influxdb import InfluxDBClient

if sensor.get_sensor_data():
    output = '{0:.2f} C, {1:.2f} hPa, {2:.3f} %RH'.format(sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)
    # wp_json_body = '[{"measurement": "bme680_measure","fields":{"temperature":',sensor.data.temperature,'}{"pressure":',sensor.data.pressure,'}{"humidity":',sensor.data.humidity,'}}]'

    wp_body = [{"measurement": "bme680_measure","fields":{"temperature":sensor.data.temperature,"pressure":sensor.data.pressure,"humidity":sensor.data.humidity}}]

#import json

#dp_wp_body = json.dumps(wp_body)
#wp_json_body = json.loads(dp_wp_body)

wp_json_body = wp_body

#print(output)

#print(wp_json_body)

client = InfluxDBClient('192.168.1.180',8086,'root','','sensor')
client.write_points(wp_json_body)
