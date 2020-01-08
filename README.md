# Notebook for analyzing DUD-E docking results

This code will be used for comparing the results of machine learning rescoring functions, such as *nnscore* and *rfscore* agains the results of AutoDock Vina. Decoy compounds from the DUD-E dataset are docked to their receptors, and poses are scored using these functions.

This repository contains:
 - A python script for docking DUD-E compounds using ODDT
 - A SLURM bash file for docking to multiple receptors
 - A Jupyter notebook for generating ROC curves: `ODDT DUDE-E ROC curves.ipynb`

The scripts here are tested on two receptors, `abl1` and `aa2r`.