#Driving a linear actuator to a specified position (0-1.0), specified velocity (0-1.0), time for halting at specified position (0-99 seconds)
#You can change these parameters using Lines 55, 56, 57
#Need to install the Phidget22 package from the phidgets website for the code to work

from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.VoltageRatioInput import *
import traceback
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def onAttach(self):
	print("Attach!")

def onDetach(self):
	print("Detach!")

def onError(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")

def onVoltageRatioChange(self, voltageRatio):
    print("VoltageRatio: " + str(voltageRatio))
    pass

def main():
    try:
        #Create your Phidget channels
        dcMotor0 = DCMotor()
        voltageRatioInput0 = VoltageRatioInput()

        #Set addressing parameters to specify which channel to open (if any)
        dcMotor0.setHubPort(0)
        dcMotor0.setDeviceSerialNumber(636592)
        voltageRatioInput0.setHubPort(0)
        voltageRatioInput0.setDeviceSerialNumber(636592)

        #Assign any event handlers you need before calling open so that no events are missed.
        dcMotor0.setOnAttachHandler(onAttach)
        dcMotor0.setOnDetachHandler(onDetach)
        dcMotor0.setOnErrorHandler(onError)
        voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        voltageRatioInput0.setOnAttachHandler(onAttach)
        voltageRatioInput0.setOnDetachHandler(onDetach)
        voltageRatioInput0.setOnErrorHandler(onError)

        #Open your Phidgets and wait for attachment
        dcMotor0.openWaitForAttachment(5000)
        voltageRatioInput0.openWaitForAttachment(5000)

        #Do stuff with your Phidgets here or in your event handlers.
        current_pos = voltageRatioInput0.getVoltageRatio()
        target_pos = 0.7
        min_pos = 0.2
        velocity = 0.3
        while (min_pos < current_pos < target_pos) or (current_pos < min_pos):
            dcMotor0.setTargetVelocity(velocity)
            current_pos = voltageRatioInput0.getVoltageRatio()

        dcMotor0.setTargetVelocity(0)

        if current_pos > target_pos:
            while current_pos > min_pos:
                dcMotor0.setTargetVelocity(-1*velocity)
                current_pos = voltageRatioInput0.getVoltageRatio()

        dcMotor0.setTargetVelocity(0)
        time.sleep(2)

        try:
        	input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
        	pass

        #Close your Phidgets once the program is done.
        dcMotor0.close()
        voltageRatioInput0.close()

    except PhidgetException as ex:
        #We will catch Phidget Exceptions here, and print the error informaiton.
        traceback.print_exc()
        print("")
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()
