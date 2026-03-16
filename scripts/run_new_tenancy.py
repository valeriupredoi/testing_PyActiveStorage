import os
import numpy as np


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
    # bigger_file = "ch330a.pc19790301-bnl.nc"  # 18GB 3400 HDF5 chunks; var=UM_m01s16i202_vn1106,UM_m01s30i202_vn1106
    # bigger_file = "ch330a.pc19790301-def.nc"  # 17GB 64 HDF5 chunks; var=UM_m01s16i202_vn1106,UM_m01s30i202_vn1106
    # bigger_file = "cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc"  # 2.3GB about 4800 chunks; var=cl
    # bigger_file = "da193a_25_day__198808-198808.nc"  # 3GB 30 HDF5 chunks; var=m01s30i111,m01s06i247_4

    bigger_file = "da193a_25_6hr_t_pt_cordex__198807-198807.nc"

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

    result = active.min(axis=(0, 1))[:]
    # result = active[0:3, 4:6, 7:9]  # standardized slice
    # result = active[0:30, 4:60]  # random slice
    # result = active[40:80, 60:90]  # random slice

    print("Result is", result)
    return result

gold_test()
