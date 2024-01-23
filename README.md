# CO2 Monitor Exporter

Prometheus exporter for CO2 concentration and indoor temperature from TFA Dostmann AirCO2NTROL Mini in Python.

Based on [node-co2-monitor](https://github.com/huhamhire/node-co2-monitor) and [python-co2-monitor](https://github.com/insunaa/python-co2-monitor).

## Contents

* [Supported Hardware](#supported-hardware)
* [Install](#install)
* [Usage](#usage)
* [Metrics](#metrics)
* [License](#license)


## Supported Hardware

* [TFA Dostmann AirCO2NTROL Mini - Monitor CO2 31.5006.02](https://www.amazon.de/dp/B00TH3OW4Q)



## Usage

```bash
python3 exporter.py
```

By default the exporter will accept connections on `0.0.0.0:9101`. After the exporter is started, prometheus server would be able to retrieve metric data from the exporter.

![Grafana](https://huhamhire.github.io/co2-monitor-exporter/images/grafana.png)


## Metrics

  Name  | Description
--------|-------------
air_temp| Ambient Temperature (Tamb) in ℃.
air_co2 | Relative Concentration of CO2 (CntR) in ppm.
air_hum | Relative Humidity (not currently measured by hardware)

## License

MIT
