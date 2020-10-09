import os
import h5py
import numpy as np


matrix1 = np.random.random(size=(1000,1000))
matrix2 = np.random.random(size=(10000, 100))
# MLS-Aura_L2GP-O3_v04-23-NRT-11-c01_2018d351t1710.he5
#with h5py.File('Users/student/Desktop/MLS-Aura_L2GP-O3_v04-23-NRT-11-c01_2018d351t1710.he5', 'w')
print("CHECK WORK")

# File name Checking.
if os.name == 'mac':
    print("MAC DETECT")

    with h5py.File('/Users/student/Desktop/Kevin.he5', 'w') as hdf:
        hdf.create_dataset('dataset1', data=matrix1)
        hdf.create_dataset('dataset2', data=matrix2)

elif os.name == 'nt': # means WindowsError
    print("WINDOW DETECT")
elif os.name == 'posix':
    print("LINUX DETECT")
else:
    print ("Please check your operating system.")
