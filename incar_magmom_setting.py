import pymatgen.io.vasp as vasp
from pymatgen.io.vasp.inputs import Incar, Kpoints, Potcar, Poscar
import os

cwd = os.getcwd()

standard_folder = '/scratch/x2813a04/c_li2mno3/4_charge_calculation/sample'
sample_folder = '/scratch/x2813a04/c_li2mno3/4_charge_calculation/gen_str/mp/0.75'
output_folder = '/scratch/x2813a04/c_li2mno3/4_charge_calculation/cal/mp/0.75'

for i in range(len(os.listdir(sample_folder))):
    poscar_file = os.path.join(sample_folder, f'{i}.vasp')
    if os.path.exists(poscar_file):
        poscar = Poscar.from_file(poscar_file)
        incar = Incar.from_file(standard_folder+'/INCAR')
        natoms = poscar.natoms
        MAGMOM = []
    for n_idx, n in enumerate(natoms):
        if n_idx == 0:
            MAGMOM.extend([0.6] * n)
        elif n_idx == 1:
            MAGMOM.extend([5.0] * n)
        elif n_idx == 2:
            MAGMOM.extend([0.6] * n)
    incar['MAGMOM'] = MAGMOM
    output_dir = os.path.join(output_folder, f'{i}')
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    Kpoints_setting = Kpoints.from_file(os.path.join(standard_folder, 'KPOINTS'))
    Potcar_setting = Potcar.from_file(os.path.join(standard_folder, 'POTCAR'))

    # Write new INCAR file
    incar.write_file('INCAR')
    poscar.write_file('POSCAR')
    Potcar_setting.write_file('POTCAR')
    Kpoints_setting.write_file('KPOINTS')