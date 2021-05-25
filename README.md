# Try-Lammps-ReaxFF

An MD Experiment about ReaxFF.

## Files

* `CH4_O2.car`, generated with Material Studio, with 10 CH4 & 20 O2 inside
* `CH4_O2.lammpstrj`, generated with VMD, contains the coordinates of atoms
* `CH4_O2_processed.lammpstrj.csv`, swapped the atom type of H and O, and inserted a column with value 1.0,  generated with `process_lammpstrj.py`
* `my_data.CHO`, atoms replaced with data in `CH4_O2_processed.lammpstrj.csv`
* `my_in.CHO`, add fix and set number of timesteps to run as `5e+6`
* `my_species.out`, output file
* `my_species_processed.csv`, processed output file, concats all the tables in `my_species.out`, generated with `process_species.py`
