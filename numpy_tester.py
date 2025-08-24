import numpy as np
import time

# ----- 1. Make a synthetic 3D array -----
np.random.seed(0)
starttime = time.time()
arr = np.random.rand(1000, 1000, 1000)  # 3D array (Z, Y, X)

print("Array shape:", arr.shape)
print("Mean intensity:", arr.mean())
print('Time taken to make array:', time.time() - starttime)

# ----- 2. Create a 3D Gaussian kernel -----
def gaussian_kernel_3d(size=5, sigma=1.0):
    """Generate a 3D Gaussian kernel."""
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy, zz = np.meshgrid(ax, ax, ax, indexing='ij')
    kernel = np.exp(-(xx**2 + yy**2 + zz**2) / (2. * sigma**2))
    kernel /= kernel.sum()
    return kernel

starttime = time.time()
kernel = gaussian_kernel_3d(size=7, sigma=1.5)
print("Gaussian kernel shape:", kernel.shape)
print('Time taken Gaussian kernel:', time.time() - starttime)


# ----- 4. Evaluate if values are in the array -----
starttime = time.time()
vals_to_check = [0.1, 0.5, 0.9]
mask = np.isin(np.round(arr, 1), vals_to_check)
print(f"How many voxels are ~{vals_to_check}? ->", mask.sum())
print('Time taken np.isinl:', time.time() - starttime)


# ----- 5. Other NumPy operations -----
starttime = time.time()

# Max intensity projection along Z
mip = arr.max(axis=0)
print("MIP shape:", mip.shape)

# Normalize array to 0–1
norm_arr = (arr - arr.min()) / (arr.max() - arr.min())

# Compute per-slice statistics
slice_means = arr.mean(axis=(1, 2))
print("Per-slice means shape:", slice_means.shape)

# Broadcasting: scale each z-slice by its mean
scaled = arr / slice_means[:, None, None]
print("Scaled array mean:", scaled.mean())
print('Time taken max, mean, min:', time.time() - starttime)

starttime = time.time()
quant = np.quantile(arr, q=[0.25, 0.5, 0.75], axis=(1, 2))
print("Quantiles shape:", quant.shape)
print('Time taken quantile:', time.time() - starttime)
