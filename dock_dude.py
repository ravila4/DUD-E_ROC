# Ricardo Avila
# Last Edited: February 9, 2018
# Script for docking DUDE data sets using ODDT

import sys
import time
from oddt.virtualscreening import virtualscreening as vs


def dock(d, f, proc, cpu):
    start_time = time.time()
    # Initiate virtual screening
    pipeline = vs(n_cpu=proc)
    # Load ligands
    pipeline.load_ligands('sdf', f + d + '_final.sdf.gz')
    # Dock entire library to receptor
    pipeline.dock(engine='autodock_vina',
	              protein=f + 'receptor.pdb',
                 auto_ligand=f + 'crystal_ligand.mol2',
	              n_cpu=cpu)
    # Rescore
    pipeline.score(function='rfscore', protein=f + 'receptor.pdb')
    pipeline.score(function='nnscore', protein=f + 'receptor.pdb')
    #pipeline.score(function='')
    # Write scores to csv
    pipeline.write_csv(f + d + '_docked.csv')
    # Log run time
    with open(f + d + '_run_time.txt', "a") as time_log:
        time_log.write("time= " + str(time.time() - start_time))


f = sys.argv[1]          # base dir
d = sys.argv[2]          # one of 'actives' or 'decoys'
proc = int(sys.argv[3])  # number of concurrent jobs
cpu = int(sys.argv[4])   # number of processors per job

dock(d, f, proc, cpu)
