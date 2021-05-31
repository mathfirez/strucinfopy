# Extracting structural information from atomic systems with Python: a case study for CO2 adsorbed on TM8 clusters.

The purpose of this tool is to gather data regarding structural parameters of the chemical species present on the system. Namely: C-O distances, O-C-O angles, and the shortest Transition Metal (TM)-O and TM-C distances. Here, the scripto.py file reads the geometry.in file containing the x, y and z coordinates for each atom in the system and calculate each given parameter.
----------------------------------------------------------
This script was developed to gather information about CO2 adsorbed on Transition Metal clusters containing 8 atoms, but can be modified to calculate structural parameters of CO2 (or other AB2 species) adsorbed on larger (or smaller) clusters upon modification of the 63rd line of the file (in this case, changing '11' to the number of lines in the geometry.in file).

The only requirements to run this script properly are:
1. The geometry.in file must be in the same format as the attached example file ('atom' x_coordinate  y_coordinate  z_coordinate  element_symbol)
2. The first three lines of the document must be with respect to:
  - The central atom (in this case carbon or A for generic AB2 systems)
  - First atom bonded to the central atom (in this case one of the oxygen atoms (O_1) or B_1 for generic AB2 systems)
  - Second atom bonded to the central atom (in this case the other oxygen atom (O_2) or B_2 for generic AB2 systems)
3. The remaining atoms (which do not belong to CO2 (or AB2) structure) must be ordered below these lines (see geometry.in file)
4. Changing the range on line 63 to the number of lines in the geometry.in file + 1 (due to the nature of python's range() usage):

```
      Line 00      atom         2.402734        -0.028403        -0.021966 	 C
      Line 01      atom         2.862152        -0.005643        -1.198981 	 O
      Line 02      atom         2.885556        -0.059046         1.145482 	 O
      Line 03      atom        -2.709473         0.058081        -1.142735 	 Os  <--------
      Line 04      atom        -1.006953         1.685384        -1.128112 	 Os
      Line 05      atom         0.641954         0.019298        -1.244085 	 Os
      Line 06      atom        -1.047341        -1.609438        -1.201554 	 Os
      Line 07      atom        -2.686439         0.005697         1.195205 	 Os
      Line 08      atom         0.666021        -0.036290         1.230236 	 Os
      Line 09      atom        -0.983869         1.632844         1.219978 	 Os
      Line 10      atom        -1.024342        -1.662483         1.146533 	 Os  <-------- 10 + 1 = 11

```
In the scripto.py file:

            for i in range(3, 11):
   
Feel free to fork, improve and share!
