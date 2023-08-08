# {my_package} Documentation

## Introduction


### How to install
Without downloading the project, one can do:
```python
pip install git+URL
```
(URL being the github repository front page)

For developer that have the git repository, one can do:

```python
pip install .
pip install -e .
```


### How to use

First import the package:

```python
import {my_package}
```

## Tools
### init_log

```python
{my_package}.init_log(log="{my_package}.log", stdout_loglevel="INFO", file_loglevel="DEBUG")
```

parameters:
* `log`: filename where to store logs. By default "{my_package}.log"
* `stdout_loglevel`: log level for standard output (ERROR, WARNING, INFO, DEBUG)
* `file_loglevel`: log level for log file (ERROR, WARNING, INFO, DEBUG)
* [optional] `extra_config`: Set of extra properties to be added to the dict_config for logging

