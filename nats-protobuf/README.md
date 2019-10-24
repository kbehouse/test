
# NATS Transfer using Protobuf
## Run Python

```
protoc -I=./ --python_out=./ ./addressbook.proto
```

```
python3 sub.py
```

```
python3 pub.py
```