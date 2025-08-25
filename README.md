# Testing_nvidia_cupynumeric
Testing CuPyNumeric by Nvidia

CuPyNumeric appears in test by Nvidia and others to scale better with #GPUs and allow for faster computations.
https://developer.nvidia.com/blog/effortlessly-scale-numpy-from-laptops-to-supercomputers-with-nvidia-cupynumeric/
https://docs.nvidia.com/cupynumeric/latest/user/usage.html

# Numpy
Array shape: (100, 100, 100)
Mean intensity: 0.5003876981207729
Time taken to make array: 0.02014327049255371
Gaussian kernel shape: (7, 7, 7)
Time taken Gaussian kernel: 0.00017642974853515625
How many voxels are ~[0.1, 0.5, 0.9]? -> 300648
Time taken np.isinl: 0.012294292449951172
MIP shape: (100, 100)
Per-slice means shape: (100,)
Scaled array mean: 1.0
Time taken max, mean, min: 0.011892318725585938
Quantiles shape: (3, 100)
Time taken quantile: 0.030061006546020508

# CuPyNumeric (Nvidia)
Array shape: (100, 100, 100)
Mean intensity: 0.49994159164297053
Time taken to make array: 0.2684314250946045
Gaussian kernel shape: (7, 7, 7)
Time taken Gaussian kernel: 0.0010995864868164062
/mnt/md0/jacobkh/anaconda3/envs/numpy_cunumeric/lib/python3.12/site-packages/cupynumeric/_utils/coverage.py:215: RuntimeWarning: cuPyNumeric has not implemented numpy.isin and is falling back to canonical NumPy. You may notice significantly decreased performance for this function call.

Set CUPYNUMERIC_FALLBACK_STACKTRACE=1 and re-run to include a full stack trace with this warning.
  issue_fallback_warning(what=name)
How many voxels are ~[0.1, 0.5, 0.9]? -> 300092
Time taken np.isinl: 0.08496642112731934
MIP shape: (100, 100)
Per-slice means shape: (100, 100)
Scaled array mean: 1.0033749475720304
Time taken max, mean, min: 0.1864488124847412
Quantiles shape: (3, 100)
Time taken quantile: 0.005254268646240234

# Notes
Note some functions are not yet implemented thus mixing CPU/GPU:
eg. array.mean(axis=(1,2)) cant run

```
Set CUPYNUMERIC_FALLBACK_STACKTRACE=1 and re-run to include a full stack trace with this warning.
  issue_fallback_warning(what=name)
/mnt/md0/jacobkh/anaconda3/envs/pipeline_v3/lib/python3.12/site-packages/cupynumeric/_utils/coverage.py:215: RuntimeWarning: cuPyNumeric has not implemented numpy.intersect1d and is falling back to canonical NumPy. You may notice significantly decreased performance for this function call.


Set CUPYNUMERIC_FALLBACK_STACKTRACE=1 and re-run to include a full stack trace with this warning.
  issue_fallback_warning(what=name)
/mnt/md0/jacobkh/anaconda3/envs/pipeline_v3/lib/python3.12/site-packages/cupynumeric/_utils/coverage.py:215: RuntimeWarning: cuPyNumeric has not implemented numpy.isin and is falling back to canonical NumPy. You may notice significantly decreased performance for this function call.


TypeError: cuPyNumeric does not support dtype=<U104


NotImplementedError: cupynumeric.mean only supports int types for `axis` currently
```

