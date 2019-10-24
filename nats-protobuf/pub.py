#! /usr/bin/python
import sys
import asyncio
from nats.aio.client import Client as NATS
import addressbook_pb2

def AddPerson1(person):
  person.id = 1
  person.name = "test_name"
  person.email = "abcd@gmail.com"

  phone_number = person.phones.add()
  phone_number.number = "0912345678"
  phone_number.type = addressbook_pb2.Person.PhoneType.MOBILE

  phone_number = person.phones.add()
  phone_number.number = "042535425"
  phone_number.type = addressbook_pb2.Person.PhoneType.HOME

# This function fills in a Person message based on user input.
def AddPerson2(person):
  person.id = 2
  person.name = "test_name2"
  person.email = "abcd22@gmail.com"
  phone_number = person.phones.add()
  phone_number.number = "092222222"
  phone_number.type = addressbook_pb2.Person.PhoneType.MOBILE

  phone_number = person.phones.add()
  phone_number.number = "0222222"
  phone_number.type = addressbook_pb2.Person.PhoneType.HOME


async def run(loop):
  address_book = addressbook_pb2.AddressBook()
  AddPerson1(address_book.people.add())
  AddPerson2(address_book.people.add())

  nc = NATS()
  await nc.connect("127.0.0.1:4222", loop=loop)
  await nc.publish("test_topic", address_book.SerializeToString())
  await nc.close()
  
if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(run(loop))
  loop.close()
