#!/usr/bin/python3

encode_dct = {}
decode_dct = {}

letters = "abcdefghijklmnopqrstuvwxyz"

len_let = len(letters)

for i in range(0,len_let):
  if i < len_let - 2:
    encode_dct[letters[i]] = letters[i+2]
    decode_dct[letters[i+2]] = letters[i]
    
  elif i == len_let - 2:
    encode_dct[letters[i]] = letters[0]
    decode_dct[letters[0]] = letters[i]

  elif i == len_let - 1:
    encode_dct[letters[i]] = letters[1]
    decode_dct[letters[1]] = letters[i]

  else:
    print("something went wrong! Check your code!")

#print(encode_dct)
#print(decode_dct)
def cypher():
  word = input("type a word: ")
  todo = None
  acceptable_commands = ["encode" , "decode"]

  while todo not in acceptable_commands:
    todo = input("Do you want to encode or decode? ")
    if todo not in acceptable_commands:
      print("Not an acccpetable command. Please try again. ")

  if todo == "encode":
    encoded = ""
    for i in word:
      encoded += encode_dct[i]
    print(encoded)
    
  if todo == "decode":
    decoded = ""
    for i in word:
      decoded += decode_dct[i]
    print(decoded)

cypher()

repeat = None
acceptable_responses = ["yes" , "no"]

while repeat not in acceptable_responses:
  repeat = input("Do you want to en/decode another word? ")
  if repeat not in acceptable_responses:
    print("Not an acceptable response. Please try again. ")

  if repeat == "no":
    print("Good Bye.")

  if repeat == "yes":
    cypher()
    repeat = None
