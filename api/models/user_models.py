from pydantic import BaseModel


class Name(BaseModel):
    firstname: str
    lastname: str


class AddressGeolocation(BaseModel):
    lat: str
    long: str


class Address(BaseModel):
    city: str
    street: str
    number: int
    zipcode: str
    geolocation: AddressGeolocation


class User(BaseModel):
    id: int
    email: str
    username: str
    password: str
    name: Name
    address: Address
    phone: str