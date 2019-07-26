# **************************************************************************
# *
# * Authors:     Roberto Marabini (roberto@cnb.csic.es)
# *
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import os

import pyworkflow.utils as pwutils
from pyworkflow import VERSION_1_2
from pyworkflow.em.data import Volume, EMObject
try:
    from pyworkflow.em.data import AtomStruct
except:
    from pyworkflow.em.data import PdbFile as AtomStruct
from pyworkflow.em.convert import ImageHandler, Ccp4Header
from ccp4 import Plugin
from ccp4.convert import (runCCP4Program, validVersion)
from pyworkflow.em.protocol import EMProtocol
from pyworkflow.protocol.constants import STATUS_FINISHED
from pyworkflow.protocol.params import (MultiPointerParam, PointerParam,
                                        BooleanParam, StringParam)
from pyworkflow.utils.properties import Message
from ccp4.constants import CCP4_BINARIES
import sqlite3

cootPdbTemplateFileName = "cootOut%04d.pdb"
cootScriptFileName = "cootScript.py"
outpuDataBaseNameWithLabels = "outpuDataBaseNameWithLabels.sqlite"
databaseTableName = 'pdb'

class CootRefine(EMProtocol):
    """Coot is an interactive graphical application for
macromolecular model building, model completion
and validation. IMPORTANT: press "w" in coot to transfer
the pdb file from coot  to scipion '
"""
    _label = 'coot refinement'
    _program = ""
    _version = VERSION_1_2
    COOT = CCP4_BINARIES['COOT']
    COOTINI='coot.ini'

    # --------------------------- DEFINE param functions -------------------
    def _defineParams(self, form):
        form.addSection(label='Input')
        form.addParam('inputVolumes', MultiPointerParam, pointerClass="Volume",
                      label='Input Volume/s', allowsNull=True,
                      help="Set of volumes to process")
        form.addParam('doNormalize', BooleanParam, default=True,
                      label='Normalize', important=True,
                      help='If set to True, particles will be normalized in '
                           'the way COOT prefers it. It is recommended to '
                           '*always normalize your particles* if the maximum '
                           'value is higher than 1.')
        form.addParam('pdbFileToBeRefined', PointerParam,
                      pointerClass="AtomStruct",
                      label='Atomic structure to be refined',
                      help="PDBx/mmCIF file to be refined. This PDBx/mmCIF object "
                           "will be saved after refinement, will be saved")
        form.addParam('inputPdbFiles', MultiPointerParam,
                      pointerClass="AtomStruct",
                      label='Other reference atomic structures',
                      help="Other PDBx/mmCIF files used as reference. These PDBx/mmCIF "
                           "objects will not be saved")
        form.addParam('extraCommands', StringParam,
                      default='',
                      condition='False',
                      label='Extra commands for chimera viewer',
                      help="""Add extra commands in cmd file. Use for testing
                      """)
        form.addParam('doInteractive', BooleanParam, default=True,
                      label='Interactive', condition='False',
                      help="""It makes coot an interactive protocol""")
        form.addParam('phythonscript', StringParam, default="",
                      label='pythonScript', condition='False',
                      help="""calls coot with '--python string'""")
        form.addParam('inputProtocol', PointerParam, allowsNull=True,
                      default=None,
                      condition='False',
                      label="Input protocols", important=True,
                      pointerClass='PhenixProtRunMolprobity, '
                               'PhenixProtRunRSRefine',
                      help="Father protocol. This is used for trazability "
                       "when coot is launched by a viewer ")

        form.addSection(label='Help')
        form.addLine('Press "w" in coot to transfer the pdb file from coot '
                     'to scipion.\nYou may also execute (Calculate -> '
                     'Scripting -> Python) the command scipion_write(imol, '
                     '[pdblabel]).\nExample: scipion_write(0,"new_name")\n'
                     'imol is the PDB id.\npdblabel is an optional parameter '
                     'that assign that label to the produced pdb. By default '
                     'the label is outcoot0001\n'
                     'Press "x" in coot to change from one chain to '
                     'the previous one.\nPress "X" in coot to change from one '
                     'chain to the next one.\nPress "U" in coot to initiate '
                     'global variables.\nYou have to set in advance the '
                     'protocolDirectory/extra/coot.ini text file:\n['
                     'myvars]\nimol: '
                     '0\naa_main_chain: '
                     'X\naa_auxiliary_chain: XX\naaNumber: 160\nstep: 15\nIn '
                     'this case global variables will initiate in '
                     'aminoacid number 160\nand each shift over the '
                     'sequence will include a segment of 15 aminoacids.\n'
                     'Press "z" in coot to refine those upstream 15 '
                     'aminoacids included in each step.\nPress "Z" in coot ' \
                     'to refine those downstream 15 aminoacids included in ' \
                     'each step.\nPress "E" in coot to print the ' \
                     'environment.\nPress "e" in coot to finish your ' \
                     'project. Then your project will not be interactive ' \
                     'anymore.')

        # --------------------------- INSERT steps functions ---------------

    def _insertAllSteps(self):
        # test loop over inputVol
        self.inVolumes = []
        self.norVolumesNames = []
        # if self.inputVolumes is None:
        if len(self.inputVolumes) is 0:
            if self.pdbFileToBeRefined.get().getVolume() is not None:
                vol = self.pdbFileToBeRefined.get().getVolume()
                inFileName = vol.getFileName()
                self.inVolumes.append(vol)
                self.norVolumesNames.append(self._getVolumeFileName(inFileName))
        else:
            for vol in self.inputVolumes:
                inFileName = vol.get().getFileName()
                self.inVolumes.append(vol.get())
                self.norVolumesNames.append(
                    self._getVolumeFileName(inFileName))

        convertId = self._insertFunctionStep('convertInputStep',
                                             self.inVolumes,
                                             self.norVolumesNames)

        self.step = self._insertFunctionStep('runCootStep', self.inVolumes,
                                 self.norVolumesNames,
                                 prerequisites=[convertId],
                                 interactive=self.doInteractive)


    # --------------------------- STEPS functions --------------------------

    def convertInputStep(self, inVolumes, norVolumesNames):
        """ convert 3D maps to MRC '.mrc' format
        """
        ih = ImageHandler()
        for inVol, norVolName in zip(inVolumes, norVolumesNames):
            inVolName = inVol.getFileName()

            if inVolName.endswith(".mrc"):
                inVolName += ":mrc"
            if norVolName.endswith(".mrc"):
                norVolName += ":mrc"
            if not ih.existsLocation(norVolName):
                if True:  # self.doNormalize:
                    img = ImageHandler()._img
                    img.read(inVolName)
                    mean, dev, min, max = img.computeStats()
                    img.inplaceMultiply(1./max)
                    img.write(norVolName)
                else:
                    ImageHandler().convert(inVolName, norVolName)
                Ccp4Header(norVolName).copyCCP4Header(
                    inVolName, inVol.getOrigin(
                               force=True).getShifts(),
                               inVol.getSamplingRate(), originField=Ccp4Header.START)

    def runCootStep(self, inVolumes, norVolumesNames):

        # PDB
        # find last created PDB output file
        listOfPDBs = []
        template = self._getExtraPath(cootPdbTemplateFileName)

        # if there is no database use pdb file from the form
        # otherwise use last created pdb file
        databasePath = self._getExtraPath(outpuDataBaseNameWithLabels)
        if not os.path.exists(databasePath):
            pdbFileToBeRefined = self.pdbFileToBeRefined.get().getFileName()
        else:
            # open database
            conn = sqlite3.connect(databasePath)
            # check tables exists
            if not _checkTableExists(conn, databaseTableName):
                 pdbFileToBeRefined = self.pdbFileToBeRefined.get().getFileName()
            else:
                c = conn.cursor()

                # read filename and label in a loop
                c.execute(
                    'SELECT pdbFileName FROM %s order by id DESC limit 1' %
                    databaseTableName)
                pdbFileToBeRefined = c.fetchone()[0]

        listOfPDBs.append(pdbFileToBeRefined)
        for pdb in self.inputPdbFiles:
            listOfPDBs.append(pdb.get().getFileName())  # other pdb files

        createScriptFile(0,  # imol
                         self._getExtraPath(cootScriptFileName), # save script in extra otherwise is lost
                                                               # when continue
                         self._getExtraPath(cootPdbTemplateFileName),
                         norVolumesNames,
                         listOfPDBs,
                         self.extraCommands.get(),
                         self._getExtraPath(self.COOTINI),  # coot.ini
                         self._getExtraPath(outpuDataBaseNameWithLabels),
                         table_name=databaseTableName
                         )

        args = ""

        #  extraCommands option is only used for tests
        if self.extraCommands.get() != '':
            args += " --no-graphics "
        args += " --script " + self._getExtraPath(cootScriptFileName)
        if len(self.phythonscript.get()) > 1:
            args += " --python {phythonscript}".format(
                phythonscript=self.phythonscript.get())
        # script with auxiliary files
        self._log.info('Launching: ' + Plugin.getProgram(self.COOT) + ' ' + args)

        # run in the background
        runCCP4Program(Plugin.getProgram(self.COOT), args)

        counter = self.getCounter()
        self.createOutputStep(inVolumes, norVolumesNames, counter)

    def createOutputStep(self, inVolumes, norVolumesNames, init_counter=1):
        """ Copy the PDB structure and register the output object.
        """
        databasePath = self._getExtraPath(outpuDataBaseNameWithLabels)
        # open database
        conn = sqlite3.connect(databasePath)
        if not _checkTableExists(conn, databaseTableName):
            conn.close()
            return

        c = conn.cursor()

        # read filename and label in a loop
        c.execute('SELECT pdbFileName, pdbLabelName FROM %s where saved = 0' %
                  databaseTableName)
        for row in c:
            pdbFileName = row[0]
            pdbLabelName = row[1]
            pdb = AtomStruct()
            pdb.setFileName(pdbFileName)
            outputs = {str(pdbLabelName) : pdb}
            self._defineOutputs(**outputs)
            # self._defineOutputs(outputPdb=pdb)
            self._defineSourceRelation(self.inputPdbFiles, pdb)

            # self._defineSourceRelation(self.inputVolumes, self.outputPdb)

            for vol in inVolumes:
                self._defineSourceRelation(vol, pdb)


        # clear database. Not very important since it will be deleted
        # since it is wrotten in tmp
        sql = 'update %s set saved = 1' % databaseTableName
        c.execute(sql)
        conn.commit()
        conn.close()

        template = self._getExtraPath(cootPdbTemplateFileName)
        counter = init_counter
        counter -= 1

        if not os.path.isfile(template % 2):  # only the first time get inside
            # here
            counter = 1
            for inVol, norVolName in zip(inVolumes, norVolumesNames):
                outVol = Volume()
                sampling = inVol.getSamplingRate()
                origin = inVol.getOrigin(
                    force=True)
                outVol.setSamplingRate(sampling)
                outVol.setOrigin(origin)

                if norVolName.endswith('.mrc'):
                    norVolName = norVolName + ":mrc"
                outFileName = self._getVolumeFileName(norVolName)
                outVol.setFileName(outFileName)
                outputs = {"output3DMap_%04d" % counter: outVol}
                counter += 1
                self._defineOutputs(**outputs)
                self._defineSourceRelation(inVol, outVol)

        if os.path.isfile(self._getExtraPath('STOPPROTCOL')):
            self.setStatus(STATUS_FINISHED)
            # NOTE: (ROB) can a dirty way to make an interactive process finish but I do not
            # think there is a clean one
            self._steps[self.step-1].setInteractive(False)

    # --------------------------- INFO functions ---------------------------
    def _validate(self):
        errors = []

        if not validVersion(7, 0.056):
            errors.append("CCP4 version should be at least 7.0.056")

        if self.inputProtocol.get() is not None and \
                self.inputProtocol.get().getClassName().startswith("PhenixProtRunMolprobity"):
                 return errors
        else:
            # Check that the input volume exist
            if self.pdbFileToBeRefined.hasValue():
                if (not self.pdbFileToBeRefined.get().hasVolume()) \
                        and self.inputVolumes.isEmpty():
                    errors.append("Error: You should provide a volume.\n")

            return errors

    @classmethod
    def validateInstallation(cls):

        # Check that the programs exist
        installed, message = Plugin.checkBinaries(cls.COOT)
        if not installed:
            return [message]
        else:
            return []

    def _summary(self):
        #  Think on how to update this summary with created PDB
        summary = []
        if self.getOutputsSize() >= 1:
            for key, output in self.iterOutputAttributes(EMObject):
                summary.append("*%s:* \n %s " % (key, output.getObjComment()))
        else:
            summary.append(Message.TEXT_NO_OUTPUT_CO)
        return summary

    def _methods(self):
        methodsMsgs = []
        methodsMsgs.append("TODO")

        return methodsMsgs

    def _citations(self):
        return ['Emsley_2004']

    # --------------------------- UTILS functions --------------------------

    def _getVolumeFileName(self, inFileName):
        return os.path.join(self._getExtraPath(''),
                            pwutils.replaceBaseExt(inFileName, 'mrc'))

    def replace_at_index(self, tup, ix, val):
        return tup[:ix] + (val,) + tup[ix+1:]

    def getCounter(self):
        template = self._getExtraPath(cootPdbTemplateFileName)
        counter = 1
        while os.path.isfile(template % counter):
            counter += 1
        return counter  # returns next free

cootScriptHeader = '''import ConfigParser
import os
from subprocess import call
mydict={}
mydict['imol']=%d
mydict['aa_main_chain']="B"
mydict['aa_auxiliary_chain']="BB"
mydict['aaNumber']=37
mydict['step']=5
mydict['outfile']='%s'
cootPath='%s'
databasePath='%s'
table_name = '%s'
'''

cootScriptBody = '''

def beep(time):
   """I simply do not know how to create a portable beep sound.
      This system call seems to work pretty well if you have sox
      installed"""
   try:
      command = "play --no-show-progress -n synth %f sin 880"%time
      print command
      os.system(command)
   except:
      pass

def _change_chain_id(signStep):
    """move a few aminoacid between chains"""
    global mydict
    dic = dict(mydict)
    if signStep < 0:
        dic['fromAaNumber'] = mydict['aaNumber'] - dic['step'] +1
        dic['toAaNumber']   = mydict['aaNumber']
        dic['fromAaChain']  = mydict['aa_auxiliary_chain']
        dic['toAaChain']    = mydict['aa_main_chain']
    else:
        dic['fromAaNumber'] = mydict['aaNumber']
        dic['toAaNumber']   = mydict['aaNumber'] + dic['step'] -1
        dic['fromAaChain']  = mydict['aa_main_chain']
        dic['toAaChain']    = mydict['aa_auxiliary_chain']
    mydict['aaNumber'] = mydict['aaNumber'] + (dic['step'] * signStep)
    command = "change_chain_id(%(imol)d, '%(fromAaChain)s', '%(toAaChain)s', 1, %(fromAaNumber)d, %(toAaNumber)d)"%dic

    doIt(command)

def _refine_zone(signStep):
    """Execute the refine command"""
    global  mydict
    dic = dict(mydict)
    if signStep <0:
        dic['fromAaNumber'] = mydict['aaNumber'] - dic['step']
        dic['toAaNumber']   = mydict['aaNumber'] + 2
        mydict['aaNumber']  = mydict['aaNumber'] - dic['step']
    else:
        dic['fromAaNumber'] = mydict['aaNumber'] - 2
        dic['toAaNumber']   = mydict['aaNumber'] + dic['step']
        mydict['aaNumber']  = mydict['aaNumber'] + dic['step']
    command = 'refine_zone(%(imol)s, "%(aa_main_chain)s", %(fromAaNumber)d, %(toAaNumber)d, "")'%dic

    doIt(command)

def _updateMol():
    """update global variable using a file as
    [myvars]
    imol: 0
    aa_main_chain: A
    aa_auxiliary_chain: AA
    aaNumber: 82
    step: 15
    called protocolDirectory/extra/coot.ini"""
    global mydict
    config = ConfigParser.ConfigParser()
    config.read(os.environ.get('COOT_INI',cootPath))
    try:
        mydict['imol']               = int(config.get("myvars", "imol"))
        mydict['aa_main_chain']      = config.get("myvars", "aa_main_chain")
        mydict['aa_auxiliary_chain'] = config.get("myvars","aa_auxiliary_chain")
        mydict['aaNumber']           = int(config.get("myvars", "aaNumber"))
        mydict['step']               = int(config.get("myvars", "step"))
        mydict['outfile']            = config.get("myvars", "outfile")
    except ConfigParser.NoOptionError:
        pass
    beep(0.1)


def getOutPutFileName(template):
    """get name based on template that does not exists
    %04d will be incremented untill it does not exists"""
    counter=1
    if "%04d" in template:
        while os.path.isfile(template%counter):
             counter += 1

    return template%counter

def storeFileNameDataBase(outFileName, outLabel=None):
    import sqlite3
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    #create_database if it does not exists
    sql = """create table if not exists %s (id integer primary key AUTOINCREMENT,
                                            pdbFileName text,
                                            pdbLabelName text,
                                            saved integer default 0
                                            )""" % (table_name)
    c.execute(sql)
    # insert record
    if outLabel is None:
        outLabel = os.path.splitext(os.path.basename(outFileName))[0]

    sql = 'insert into ' + table_name + """ (pdbFileName,
                                             pdbLabelName) values
                                            ('%s', '%s')""" % (outFileName, outLabel)
    c.execute(sql)

    # commit
    conn.commit()
    # close connection
    conn.close()

def _write(outLabel=None):
    """write pdb file, default names
       can be overwritted using coot.ini"""
    #imol = getOutPutFileName(mydict['imol'])
    #outFile = getOutPutFileName(mydict['outfile'])
    dic = dict(mydict)
    outFileName=getOutPutFileName(dic['outfile'])
    
    if outLabel is None:
        outLabel = os.path.splitext(os.path.basename(outFileName))[0]
    else:
        ext = os.path.splitext(outFileName)[1]
        dir = os.path.dirname(outFileName)
        basename = os.path.splitext(outLabel)[0]
        outFileName = os.path.join(dir, basename + ext)
    
    dic['outfile'] = outFileName
    command = "write_pdb_file(%(imol)s,'%(outfile)s')"%dic
    storeFileNameDataBase(outFileName, outLabel)
    doIt(command)
    beep(0.1)

def scipion_write(imol=0, outLabel=None):
    """scipion utility for writting files
    args: model number, 0 by default"""
    global mydict
    mydict['imol']=imol
    _write(outLabel)

def doIt(command):
    """launch command"""
    eval(command)
    #beep(0.1)

def _printEnv():
    for key in os.environ.keys():
       print "%30s %s \\n" % (key,os.environ[key])

def _finishProj():
    global mydict
    filenName = mydict['outfile']%1
    dirPath = os.path.dirname(filenName)
    fileName = os.path.join(dirPath,"STOPPROTCOL")
    open(fileName,"w").close()
    beep(0.1)

#change chain id
add_key_binding("change_chain_id_down","x", lambda: _change_chain_id(-1))
add_key_binding("change_chain_id_down","X", lambda: _change_chain_id(1))

#refine aminoacid segment
add_key_binding("refine zone m","z", lambda: _refine_zone(1))
add_key_binding("refine zone m","Z", lambda: _refine_zone(-1))

#update global variables
add_key_binding("init global variables","U", lambda: _updateMol())

#write file
add_key_binding("write pdb file","w", lambda: _write())

#print environ
add_key_binding("print enviroment","E", lambda: _printEnv())

#finish project
add_key_binding("finish project","e", lambda: _finishProj())

'''


def createScriptFile(imol,  # problem PDB id
                     scriptFile,  # name of temporary script file
                                  # loads pdbs, 3Dmap and commands defined
                                  # by the user
                     pdbFile,  # output PDB file
                     listOfMaps,  # 3Dmaps to be loaded, first one is the
                                  # reference
                     listOfPDBs,  # PDB to be loaded, first one
                                  # is the problem PDB
                     extraCommands='',  # extra commands to add at the
                                       # end of the file
                                       # mainly used for testing
                     cootFileName='/tmp/coot.ini',
                     outpuDataBaseNameWithLabels='output.db',
                     table_name='pdb'
                     ):
    f = open(scriptFile, "w")
    f.write(cootScriptHeader % (imol, pdbFile, cootFileName,
                                outpuDataBaseNameWithLabels,
                                table_name))
    f.write(cootScriptBody)
    # load PDB and MAP
    f.write("\n#load Atomic Structures\n")  # problem atomic structure must be
    # model 0
    for pdb in listOfPDBs:
        f.write("read_pdb('%s')\n" % pdb)
    f.write("\n#load 3D maps\n")
    for vol in listOfMaps:
        f.write("handle_read_ccp4_map('%s', 0)\n" % vol)
    f.write("\n#Extra Commands\n")
    f.write(extraCommands)
    f.close()


    # create coot.ini if it does not exist
    if os.path.exists(cootFileName):
        pass
    else:
        f = open(cootFileName,"w")
        f.write("""[myvars]
imol: 0
aa_main_chain: A
aa_auxiliary_chain: AA
aaNumber: 100
step: 10
""")
        f.close()

def _checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM sqlite_master
        WHERE type='table'
         AND name='%s'
        """%tablename)
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False
