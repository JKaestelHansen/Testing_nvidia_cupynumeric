# Testing_nvidia_cupynumeric
Testing CuPyNumeric by Nvidia



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
