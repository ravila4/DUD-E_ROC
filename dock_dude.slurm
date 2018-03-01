#!/bin/bash
#SBATCH -J docktest
#SBATCH -N 1                # number of nodes requested
#SBATCH -n 56               # total number of mpi tasks requested


# Slurm email notifications are now working on Lonestar 5
#SBATCH --mail-user=ravila11@miners.utep.edu
#SBATCH --mail-type=all   


# Slurm logfiles
#SBATCH --output=%j.out
#SBATCH --error=%j.err

python dock_dude.py all/aa2ar/ decoys 56 1
python dock_dude.py all/abl1/ decoys 56 1
python dock_dude.py all/ace/ decoys 56 1
python dock_dude.py all/aces/ decoys 56 1
python dock_dude.py all/ada/ decoys 56 1
python dock_dude.py all/ada17/ decoys 56 1
python dock_dude.py all/adrb1/ decoys 56 1
python dock_dude.py all/adrb2/ decoys 56 1
python dock_dude.py all/akt1/ decoys 56 1
python dock_dude.py all/akt2/ decoys 56 1
python dock_dude.py all/aldr/ decoys 56 1
python dock_dude.py all/ampc/ decoys 56 1
python dock_dude.py all/andr/ decoys 56 1
python dock_dude.py all/aofb/ decoys 56 1
python dock_dude.py all/bace1/ decoys 56 1
