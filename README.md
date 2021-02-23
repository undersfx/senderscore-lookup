# Senderscore
Command line tool for Sender Score lookups.

[![Build Status](https://travis-ci.com/undersfx/senderscore-lookup.svg?branch=master)](https://travis-ci.com/undersfx/senderscore-lookup) [![codecov](https://codecov.io/gh/undersfx/senderscore-lookup/branch/master/graph/badge.svg)](https://codecov.io/gh/undersfx/senderscore-lookup) [![Python 3](https://pyup.io/repos/github/undersfx/senderscore-lookup/python-3-shield.svg)](https://pyup.io/account/repos/github/undersfx/senderscore-lookup)[![Updates](https://pyup.io/repos/github/undersfx/senderscore-lookup/shield.svg)](https://pyup.io/account/repos/github/undersfx/senderscore-lookup) [![Total alerts](https://img.shields.io/lgtm/alerts/g/undersfx/senderscore-lookup.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/undersfx/senderscore-lookup/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/undersfx/senderscore-lookup.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/undersfx/senderscore-lookup/context:python)

### What the heck is Sender Score ?
Sender Score is a number between 0 and 100 that identifies your sender reputation and shows you how mailbox providers view your IP address.

The project is maintained by Return Path. For more information about the Sender Score project, visit the official FAQ page at https://www.senderscore.org/faq/.


# Usage

### Installation
```shell
pip install senderscore
```

### CLI
```shell
senderscore <IP>
```

### Incorporate CLI
```python
from senderscore import senderscore

ip = '177.136.19.206' # e.g.

score = senderscore.cli(ip)
```

### Module Usage
```python
from senderscore import senderscore

ip = '177.136.19.206' # e.g.

score = senderscore.get_score(ip)
```


# API

Validate the syntax of a given IP:
```python
senderscore.is_valid_ip(ip: str) -> bool
```

Retrieve the Sender Score value for the given IP:
```python
senderscore.get_score(ip: str) -> str
```

Run the cli resolution for the given IP:
```python
senderscore.cli(ip: str) -> None
```


# How to Contribute
Just fork the project and send your pull requests (with tests please).
