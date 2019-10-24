
# NATS Transfer using Protobuf

## Run NATS Server

```
nats-server
```

## Run Python

```
cd py/
```

```
protoc -I=../pb/ --python_out=./ ../pb/addressbook.proto
```

```
python3 sub.py
```

```
python3 pub.py
```

## Run Go

```
cd go/
```

```
protoc -I=../pb/ --go_out=./ addressbook.proto
```

```
go run sub.go
```

## Refer 

https://developers.google.com/protocol-buffers/docs/gotutorial