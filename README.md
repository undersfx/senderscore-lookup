# Senderscore
Command line tool for Sender Score lookups.

### What the heck is Sender Score ?
Sender Score is a number between 0 and 100 that identifies your sender reputation and shows you how mailbox providers view your IP address.

The project is maintained by Return Path. For more information about the Sender Score project, visit the official FAQ page at https://www.senderscore.org/faq/.

## Installation
```shell
pip install senderscore
```

## Usage

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

## API
```python
is_valid_ip(ip: str) -> bool
```
Validate the syntax of a given IP.
```python
get_score(ip: str) -> str
```
Retrieve the Sender Score value for the given IP.
```python
cli(ip: str) -> None
```
Run the cli resolution for the given IP.

# How to Contribute
Just fork the project and send your pull requests (with tests please).