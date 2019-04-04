# Azure-IoTHub-Data-Loader
Uploads data to IoTHub using statistical distrubutions

## Configure
You will need to grab a device id and key from IoT hub.  Put that in the appropriate spot in the code and you should be off and running.

## Editing the JSON document
If you want to send you own data format then simply edit the template.json file.
The program does a string replacement on the distributions.  So for example this:
```json
{
  "Temperature": "NormalDistribution",
  "Humidity": "Logicstic",
  "Sensor1": "Triangular",
  "Sensor2": "Beta"

}
```
becomes
```json

{
  "Temperature": 0.21976103851404127, 
  "Humidity": 10.208207305412358, 
  "Sensor2": 0.33004126435576014, 
  "Sensor1": 3.1849581097086297
}
```
# Usage
```sh
python IoTHubDataLoader.py
```

---
# Running program


Then run

```sh

cd Azure-IoTHub-Data-Loader/IoTHubDataLoader
pip3 install -r requirements.txt
python3 IoTHubDataLoader.py

```

[![full](https://img.youtube.com/vi/xxMrr21clFQ/0.jpg)](https://www.youtube.com/watch?v=xxMrr21clFQ)

