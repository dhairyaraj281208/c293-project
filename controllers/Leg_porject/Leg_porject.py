from controller import Robot


robot = Robot()

timestep = 320
flag = 0

motorRPC =robot.getDevice("RPC")
motorRPF=robot.getDevice("RPF")
motorRMC= robot.getDevice("RMC")
motorRMF= robot.getDevice("RMF")
motorRAC= robot.getDevice("RAC")
motorRAF= robot.getDevice("RAF")

motorLPC= robot.getDevice("LPC")
motorLPF= robot.getDevice("LPF")
motorLMC= robot.getDevice("LMC")
motorLMF= robot.getDevice("LMF")
motorLAC= robot.getDevice("LAC")
motorLAF= robot.getDevice("LAF")

while (robot.step(timestep) != -1):  #until the robot stop the controller
    motorRPC.setPosition(-0.3)
    motorLPC.setPosition(-0.3)