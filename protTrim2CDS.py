'''

Description:
    Tool to reconcile CDS sequence with trimmed protein sequence produced by 
    ClipKit (https://github.com/JLSteenwyk/ClipKIT). 
    
    Will take trimmed amino acid alignment and the log file produced by 
    ClipKit (using -l flag) and trim CDS sequence alignment accordingly.
    
    Requires Fasta format.
    
    Outputs trimmed CDS multiple sequence alignment in Fasta format to the 
    standard output.

USAGE:
    
    python protTrim2CDS.py <trimmed.prot.MSA.fasta> <clipkit.log> <cds.MSA.fasta> > trimmed.cds.MSA.fasta

To generate this help screen, type:
    python protTrim2CDS.py -h


Copyright 2021 by Joel Sharbrough under the MIT Liscence. All rights reserved.
    

'''

import sys

def protTrim2CDS(trimmedProt,log,cdsFasta):
    cdsList,cdsDict=buildSeqDict(cdsFasta)
    protList,protDict=buildSeqDict(trimmedProt)
    keepCodons = {}
    infile = open(log,'r')
    for line in infile:
        lineSplit = line.split(' ')
        if lineSplit[1] == 'keep':
            keepCodons[int(lineSplit[0])-1] = 'keep'
        else:
            keepCodons[int(lineSplit[0])-1] = 'trim'
    for cdsSeq in cdsList:
        sys.stdout.write('>' + cdsSeq + '\n')
        currSeq = cdsDict[cdsSeq]
        codonNum = 0
        i=0
        while i < len(currSeq):
            if keepCodons[codonNum] == 'keep':
                sys.stdout.write(currSeq[i:i+3])
            codonNum += 1
            i += 3
        sys.stdout.write('\n')
 

def buildSeqDict(fasta):
    infile = open(fasta,'r')
    scaffoldDict = {}
    scaffoldList = []
    seqName = ''
    currSeq = ''
    for line in infile:
        if line[0] == '>':
            if seqName != '':
                scaffoldDict[seqName] = currSeq
            seqName = line[1:]
            while seqName[-1] == '\n' or seqName[-1] == '\t' or seqName[-1] == '\r':
                seqName = seqName[0:-1]
            scaffoldList.append(seqName)
            currSeq = ''
        else:
            currSeq += line
            while currSeq[-1] == '\n' or currSeq[-1] == '\t' or currSeq[-1] == '\r':
                currSeq = currSeq[0:-1]
    scaffoldDict[seqName] = currSeq 
    infile.close()
    return scaffoldList,scaffoldDict


helpStatement='\nDescription:\n\tTool to reconcile CDS sequence with trimmed protein sequence produced by \n\tClipKit (https://github.com/JLSteenwyk/ClipKIT). \n\n\tWill take trimmed amino acid alignment and the log file produced by \n\tClipKit (using -l flag) and trim CDS sequence alignment accordingly.\n\n\tRequires Fasta format.\n\n\tOutputs trimmed CDS multiple sequence alignment in Fasta format to the \n\tstandard output.\n\nUSAGE:\n\n\tpython protTrim2CDS.py <trimmed.prot.MSA.fasta> <clipkit.log> <cds.MSA.fasta> > trimmed.cds.MSA.fasta\n\nTo generate this help screen, type:\n\n\tpython protTrim2CDS.py -h\n\nCopyright 2021 by Joel Sharbrough under the MIT Liscence. All rights reserved.\n\n'

if len(sys.argv) == 3:
    protTrim2CDS(sys.argv[1],sys.argv[1] + '.log',sys.argv[2],)
elif len(sys.argv) == 4:
    protTrim2CDS(sys.argv[1],sys.argv[2],sys.argv[3])
else:
    sys.stderr.write(helpStatement)
    