import os
import numpy as np
import sys
from activestorage.active import Active

S3_BUCKET = "bnl"

def gold_test():
    """Run somewhat as the 'gold' test."""
    storage_options = {
        'key': "f2d55c6dcfc7618b2c34e00b58df3cef",
        'secret': "$/'#M{0{/4rVhp%n^(XeX$q@y#&(NM3W1->~N.Q6VP.5[@bLpi='nt]AfH)>78pT",
        'client_kwargs': {'endpoint_url': "https://uor-aces-o.s3-ext.jc.rl.ac.uk"},  # final proxy
    }

    # Reductionist in the Cloud (outside firewall)
    ##############################################
    # Reductionist on 1x machines (active)
    # active_storage_url = "https://192.171.169.248:8080"
    # Reductionist on 3x machines (activeh)
    # active_storage_url = "https://192.171.169.113:8080"  # 3xRed Bryan VM
    # active_storage_url = "https://192.171.169.248:8080"  # 1xRed Bryan VM

    # Reductionist on Wacasoft (behind firewall)
    ############################################
    active_storage_url = "https://reductionist.jasmin.ac.uk/"  # Wacasoft new Reductionist

    # Possible files
    ################
    #bigger_file = "ch330a.pc19790301-bnl.nc"  # 18GB 3400 HDF5 chunks; var=UM_m01s16i202_vn1106,UM_m01s30i202_vn1106
    #bigger_file = "cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc"  # 17GB 64 HDF5 chunks; var=UM_m01s16i202_vn1106,UM_m01s30i202_vn1106
    #bigger_file = "cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc"  # 2.3GB about 4800 chunks; var=cl
    #bigger_file = "da193a_25_day__198808-198808.nc"  # 3GB 30 HDF5 chunks; var=m01s30i111,m01s06i247_4. -- m01s30i111 does not work

    bigger_file = "da193a_25_6hr_t_pt_cordex__198807-198807.nc"  #'m01s30i111', interface_type="s3",  

    test_file_uri = os.path.join(
        S3_BUCKET,
        bigger_file
    )
    print("S3 Test file path:", test_file_uri)
    active = Active(test_file_uri, 'm01s30i111', interface_type="s3",  # 'm01s06i247_4', interface_type="s3",
                    storage_options=storage_options,
                    active_storage_url=active_storage_url)

    active._version = 2
    active._method = "min"

    #result = active.min()[:]

    result = active[0:30, 0:30, 0:30]  # random slice
    # result = active[40:80, 60:90]  # random slice
    # result = active.min(axis=(1, 2))[:]
    
    print("Result is", result)
    return result


def test_s3_file(filename, variable, sample_slice):
    """
    Run the 'gold' test with parameterized file, variable, and slicing.
    """
    storage_options = {
        'key': "f2d55c6dcfc7618b2c34e00b58df3cef",
        'secret': "$/'#M{0{/4rVhp%n^(XeX$q@y#&(NM3W1->~N.Q6VP.5[@bLpi='nt]AfH)>78pT",
        'client_kwargs': {'endpoint_url': "https://uor-aces-o.s3-ext.jc.rl.ac.uk"},  # final proxy
    }

    # Reductionist on Wacasoft (behind firewall)
    active_storage_url = "https://reductionist.jasmin.ac.uk/" 

    # Construct the URI using the passed filename
    test_file_uri = os.path.join(
        S3_BUCKET,
        filename
    )
    
    print(f"S3 Test file path: {test_file_uri}")
    print(f"Target Variable: {variable}")

    active = Active(
        test_file_uri, 
        variable, 
        interface_type="s3",
        storage_options=storage_options,
        active_storage_url=active_storage_url
    )

    active._version = 2
    active._method = "min"

    result = active[sample_slice]
    
    print("Result is", result)
    return result


def test_https_file():
    """Run a simple active storage instance test with https file."""

    test_file_uri = "https://esgf.ceda.ac.uk/thredds/fileServer/esg_cmip6/CMIP6/AerChemMIP/MOHC/UKESM1-0-LL/ssp370SST-lowNTCF/r1i1p1f2/Amon/cl/gn/v20200420/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_201501-204912.nc"
    active = Active(test_file_uri, ncvar="cl")
    active._version = 1
    active._method = "min"


    result = active[0:4, 0:1, 0:30, 0:30] # random slice

    return result  # numpy.array([0.6909787], dtype="float32")


if __name__ == "__main__":

    #test_files_info = [["ch330a.pc19790301-bnl.nc"                        , "UM_m01s16i202_vn1106", "UM_m01s30i202_vn1106" ], \
    #["ch330a.pc19790301-def.nc"                                           , "UM_m01s16i202_vn1106", "UM_m01s30i202_vn1106" ], \
    #["cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc" , "cl"                                           ], \
    #["da193a_25_day__198808-198808.nc"                                    , "m01s06i247_4"                                 ], \
    #["da193a_25_6hr_t_pt_cordex__198807-198807.nc"                        , "m01s30i111"                                   ]]

    ##target_file = "ch330a.pc19790301-def.nc"
    ##target_var = "UM_m01s30i202_vn1106"

    #active_slices = (slice(0, 4), slice(0, 30), slice(0, 30))
    ##active_slices = (slice(0, 4),slice(0, 1), slice(0, 30), slice(0, 30))

    ##final_result = test_s3_file(target_file, target_var, active_slices)



    test_https_file()

    # Check if we got the right number of arguments
    """
    if len(sys.argv) < 4:
        print("Usage: python script.py <file> <var> <slices_string>")
        sys.exit(1)

    target_file = sys.argv[1]
    target_var  = sys.argv[2]
    
    # Convert the string "(0,4,0,1,0,30,0,30)" back into slice objects
    # We split the string by commas and group them in pairs
    slice_data = [int(x) for x in sys.argv[3].strip("()").split(",")]
    active_slices = tuple(slice(slice_data[i], slice_data[i+1]) 
                          for i in range(0, len(slice_data), 2))

    final_result = test_s3_file(target_file, target_var, active_slices)
    """