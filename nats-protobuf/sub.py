#! /usr/bin/python
import sys
from nats.aio.client import Client as NATS
import addressbook_pb2
import asyncio
# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book):
  for person in address_book.people:
    print("Person ID:", person.id)
    print("  Name:", person.name)
    
    print("  E-mail address:", person.email)

    for phone_number in person.phones:
      if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
        print("  Mobile phone #: ", phone_number.number)
      elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
        print("  Home phone #: ", phone_number.number)
      elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
        print("  Work phone #: ", phone_number.number)

async def message_handler(msg):
  address_book = addressbook_pb2.AddressBook()
  address_book.ParseFromString(msg.data)
  ListPeople(address_book)


async def run(loop):
  nc = NATS()
  await nc.connect("127.0.0.1:4222", loop=loop)
  await nc.subscribe("test_topic", cb=message_handler)

  

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(run(loop))
  try:
    loop.run_forever()
  finally:
    loop.close()