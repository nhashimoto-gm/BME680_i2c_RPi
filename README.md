# BME680_i2c_RPi

https://github.com/nhashimoto-gm/BME680_i2c_RPi

## 使用センサー
Bosch Sensortec GmbH Smart sensor: BME680

( https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/ )

Pimoroni Ltd Product Number PIM323 BME680 SENSOR EVAL BOARD

( https://www.digikey.com/en/products/detail/pimoroni-ltd/PIM323/7933290 )

## 接続機器と接続方法
RaspberryPIにi2c接続で通信。

以下の公式ライブラリを使用します。

- https://github.com/pimoroni/bme680-python

(留意点) プルアップ抵抗は不要です。

## 注意
LOCAL NETWORK上のInfluxdb v1.8サーバーへデータを送信。

## Acknowledgments ( 謝辞 )

Pimoroni Ltd, you have been very helpful.

https://github.com/pimoroni/bme680-python
