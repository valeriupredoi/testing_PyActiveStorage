import os
import numpy as np


from activestorage.active import Active


S3_ACTIVE_URL_Bryan = "https://192.171.169.248:8080"
S3_BUCKET = "bnl"

def gold_test():
    """Run somewhat as the 'gold' test."""
    storage_options = {
        'key': "f2d55c6dcfc7618b2c34e00b58df3cef",
        'secret': "$/'#M{0{/4rVhp%n^(XeX$q@y#&(NM3W1->~N.Q6VP.5[@bLpi='nt]AfH)>78pT",
        'client_kwargs': {'endpoint_url': "https://uor-aces-o.s3-ext.jc.rl.ac.uk"},
    }
    # old Reductionist deployed on 1x machine (active)
    active_storage_url = "https://192.171.169.248:8080"
    # bigger_file = "ch330a.pc19790301-bnl.nc"  # 18GB 3400 HDF5 chunks
    bigger_file = "ch330a.pc19790301-def.nc"  # 17GB 64 HDF5 chunks
    # bigger_file = "da193a_25_day__198808-198808.nc"  # 3GB 30 HDF5 chunks

    test_file_uri = os.path.join(
        S3_BUCKET,
        bigger_file
    )
    print("S3 Test file path:", test_file_uri)
    # big file bnl: 18GB/3400 HDF5 chunks; def: 17GB/64 HDF5 chunks
    active = Active(test_file_uri, 'UM_m01s16i202_vn1106', storage_type="s3",
                    storage_options=storage_options,
                    active_storage_url=active_storage_url)
    # old test with 3GB file and 30 chunks
    # active = Active(test_file_uri, 'm01s06i247_4', storage_type="s3",
    #                 storage_options=storage_options,
    #                 active_storage_url=active_storage_url)

    active._version = 1
    active._method = "min"

    result = active[:]
    # result = active[0:3, 4:6, 7:9]  # standardized slice

    print("Result is", result)
    return result

gold_test()
