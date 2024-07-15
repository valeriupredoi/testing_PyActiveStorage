## Testing JASMIN's new `ext.proxy` domain

### Test settings

- pipeline: PyActiveStorage/`test_optimal_kerchink`
- file tested with: bnl/ch330a.pc19790301-bnl.nc with variable `UM_m01s16i202_vn1106` for storage type `s3`
- start from: UoR network
- end (Reductionist): `activeh`
- new domain: `'client_kwargs': {'endpoint_url': "https://uor-aces-o.ext.proxy.jc.rl.ac.uk"}`
- old domain: `'client_kwargs': {'endpoint_url': "https://uor-aces-o.s3-ext.jc.rl.ac.uk"}`
- file chunks: 3400
- PyActive/active threads: 150
- function: max
- slicing on file: none, entire file

### Results (time)

- new domain (seconds, elapsed): [27.4, 27.5, 28.0, 27.7, 27.7, 27.6, 28.1, 27.1, 27.7, 27.6]
- old domain (seconds, elapsed): [27.4, 28.5, 42.2, 28.0, 37.3, 27.9, 24.9, 27.0, 28.1, 28.8]
- new domain (mean, std dev, seconds): 27.6 +/- 0.3
- new domain (mean, std dev, seconds): 30.1 +/- 5.1
- previous tests (same test settings, March 2024): 75-80
