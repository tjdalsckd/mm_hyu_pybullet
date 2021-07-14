import pybullet as p
import numpy as np
import time
import pybullet_data
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

useRealTimeSim = False
p.setRealTimeSimulation(useRealTimeSim)
plane= p.loadURDF("urdf/plane/plane.urdf")
robotPATH = "urdf/right_sim.urdf"
p.setGravity(0, 0, -10)
robotId = p.loadURDF(robotPATH,[0,0,0.5], p.getQuaternionFromEuler([0,0,0]))
NumberofJoint = p.getNumJoints(robotId)
MobileJoint = [0,1,2]
ArmJoint = [12,13,14,15,16,17]
for j in MobileJoint:
	p.setJointMotorControl2(robotId, j, p.VELOCITY_CONTROL, targetPosition=0, force=0)
for j in ArmJoint:
	p.setJointMotorControl2(robotId, j, p.VELOCITY_CONTROL, targetPosition=0, force=0)
	

for i in range(0,NumberofJoint):
	print(p.getJointInfo(robotId,i))
	

dt = 0.001
while(1):
	p.stepSimulation()
	time.sleep(dt)