package main

import (
	"log"
	"runtime"
	"fmt"

	"github.com/golang/protobuf/proto"
	pb "github.com/kbehouse/test/nats-protobuf/go/tutorial"
	nats "github.com/nats-io/nats.go"
)

func main() {
	// Connect to a server
	nc, err := nats.Connect(nats.DefaultURL)
	if err != nil {
		log.Fatal(err)
	}
	// Simple Async Subscriber
	nc.Subscribe("test_topic", func(m *nats.Msg) {
		// fmt.Printf("Received a message: %s\n", string(m.Data))
		book := &pb.AddressBook{}
		if err := proto.Unmarshal(m.Data, book); err != nil {
			log.Fatalln("Failed to parse address book:", err)
		}
		fmt.Println(book)
	})
	nc.Flush()

	runtime.Goexit()
}
