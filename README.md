# protTrim2CDS
*Description:*

    Tool to reconcile CDS sequence with trimmed protein sequence produced 
    by ClipKit (https://github.com/JLSteenwyk/ClipKIT).
    
    Will take trimmed amino acid alignment and the log file produced by 
    ClipKit (using -l flag) and trim CDS sequence alignment accordingly.
    
    Requires Fasta format.
    
    Outputs trimmed CDS multiple sequence alignment in Fasta format to the 
    standard output.

*USAGE:*
    
    python protTrim2CDS.py <trimmed.prot.MSA.fasta> <clipkit.log> <cds.MSA.fasta> > trimmed.cds.MSA.fasta

To generate this help screen, type:
    python protTrim2CDS.py -h


Copyright 2021 by Joel Sharbrough under the MIT Liscence. All rights reserved.
    
