#!/usr/bin/env python3
#IOT Smart Pantry Inventory System
#Capstone 2 Fall 2020
#Group: Katherine Fauci, Erik Rodriguez, Keshawn Smith
#Code Writen By: Erik Rodriguez
#Version 1 (Oct. 10, 2020)

#Importing Packages Needed To Read RFID Tag
import RPi.GPIO as GPIO                                    #Sets pins on raspberry Pi
import MFRC522                                             #Allows for RFID read and write commands
import signal                                              #Use signal handlers

continue_read = True

#Clears information when there is no more to read
def end_read(signal,frame):
    global continue_read
    print ("Press Control C to end tag reading")
    continue_read = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read) #Define a custom handler to be executed when signal is recieved

RFID_Reader = MFRC522.MFRC522() #Object class for the RFID MFRC522 class

#User messages
print ("Welcome to the Smart Pantry Inventory System!")
print ("If you are scanning a new item, please scan barcode, then tag and stick tag to product.")
print ("If you are scanning an already inputed product, just scan the attached tag.")
print ("Press Control-C to end scanning.")

while continue_read:
    (status,TagType) = RFID_Reader.MFRC522_Request(RFID_Reader.PICC_REQIDL) #Scans for tags

    if status == RFID_Reader.MI_OK: #Checks if tag is present
        print ("Tag detected")

    (status,uid) = RFID_Reader.MFRC522_Anticoll() #Pulls RFID from tag

    if status == RFID_Reader.MI_OK: #If the tag is valid
        print ("Card read RFID: %s,%s,%s,%s") % (uid[0], uid[1], uid[2], uid[3])

        RFID_Reader.MFRC522_SelectTag(uid) #Selects the tag that was scanned
