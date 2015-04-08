
ArmJnts = (['jnt_clavicle',[2.0,0.0,0.0]],['jnt_shoulder',[6.0,0.0,0.0]],['jnt_elbow',[12.0,0.0,-2.0]],['jnt_wrist',[18.0,0.0,0.0]])
\ No newline at end of file
def createArm():
    for item in ArmJnts:
        cm.joint(n=item[0], p = item[1],sym=True)
        
    cm.select(cm.ls('jnt_*',type='joint'))
    cm.joint(e=True,oj='xyz',sao='xup')
    cm.delete(cn=True,hi=True)
createArm()
\ No newline at end of file
