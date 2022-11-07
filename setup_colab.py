import os
import sys
import subprocess


drivepath='/content/drive/'


from   google.colab import drive

drive.mount(drivepath, force_remount=True)

mydrive = drivepath + '/MyDrive/'

os.chdir(mydrive)

try:
    import  desihigh

except:
    print('Failed to import desihigh; Cloning.')

    print('git clone https://github.com/apalmese/desihigh.git --depth=1')

    subprocess.run('git clone https://github.com/apalmese/desihigh.git --depth=1', shell=True, check=True)    

    try:
        sys.path.append(mydrive)

        import  desihigh

        print('Successfully cloned DESI High to Google Drive.')

    except Exception as EE:
        emessage = 'Failed to setup DESI High @ colab.  Please create a ticket at https://github.com/michaelJwilson/desihigh.git and include:\n\n{}\n\n{}'.format(EE, sys.path)

        raise  RuntimeError(emessage)

