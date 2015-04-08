import maya.cmds as cmds

def runCommand(*args):
	print args
	print "Run Command"
	from Rigging import rig_arm
 
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'RDojo_Menu':
            cmds.deleteUI('RDojo_Menu', m=True)
 
    mymenu = cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
    cmds.menuItem(label='Rig Arm', parent=mymenu, command=runCommand)
createMenu()
\ No newline at end of file