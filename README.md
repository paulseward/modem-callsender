Terrible PoC for using a modem to generate dummy traffic on a Strowger telephone exchange.

You probably don't need this, and if you do, there are better ways to do it!

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

# Modify to suit your exchange, then:

./callsender.py
```

