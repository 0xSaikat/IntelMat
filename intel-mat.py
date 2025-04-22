import numpy as np
import time
import os
import sys

try:
    
    import intel_extension_for_numpy as inpx
    INTEL_NUMPY_AVAILABLE = True
    print("Intel Extension for NumPy is available and will be used for acceleration")
except ImportError:
    INTEL_NUMPY_AVAILABLE = False
    print("Intel Extension for NumPy not found, using standard NumPy")

def generate_random_matrices(size):
    """Generate two random matrices of the specified size"""
    A = np.random.rand(size, size).astype(np.float32)
    B = np.random.rand(size, size).astype(np.float32)
    return A, B

def numpy_matrix_multiplication(A, B):
    """Standard NumPy matrix multiplication"""
    return np.matmul(A, B)

def intel_optimized_multiplication(A, B):
    """Intel-optimized matrix multiplication if available"""
    if INTEL_NUMPY_AVAILABLE:
        return inpx.matmul(A, B)
    else:
        
        return np.matmul(A, B)

def benchmark_multiplication(matrix_size=1000, num_runs=5):
    """Benchmark matrix multiplication using standard and Intel-optimized methods"""
    A, B = generate_random_matrices(matrix_size)
    
    
    _ = numpy_matrix_multiplication(A, B)
    
   
    start_time = time.time()
    for _ in range(num_runs):
        C_numpy = numpy_matrix_multiplication(A, B)
    numpy_time = (time.time() - start_time) / num_runs
    print(f"Standard NumPy: {numpy_time:.4f} seconds per run")
    
   
    start_time = time.time()
    for _ in range(num_runs):
        C_intel = intel_optimized_multiplication(A, B)
    intel_time = (time.time() - start_time) / num_runs
    print(f"Intel Optimized: {intel_time:.4f} seconds per run")
    
    
    if INTEL_NUMPY_AVAILABLE:
        is_equal = np.allclose(C_numpy, C_intel)
        print(f"Results match: {is_equal}")
    
    
    if intel_time > 0:
        speedup = numpy_time / intel_time
        print(f"Intel speedup: {speedup:.2f}x")
    
    return numpy_time, intel_time

def check_intel_optimization():
    """Check if NumPy is using Intel MKL"""
    
    mkl_info = np.show_config()
    print("\nNumPy Configuration:")
    
    
    try:
        import cpuinfo
        cpu_info = cpuinfo.get_cpu_info()
        print(f"CPU: {cpu_info.get('brand_raw', 'Unknown')}")
    except ImportError:
        print("cpuinfo package not available. Install with: pip install py-cpuinfo")
    
    
    print("\nIntel Optimization Detection:")
    if 'INTEL_NUMPY' in os.environ:
        print(f"Intel NumPy Environment Variable: {os.environ['INTEL_NUMPY']}")
    
   
    try:
        import intel
        print(f"Intel Distribution for Python: {intel.__version__}")
    except ImportError:
        print("Intel Distribution for Python not detected")

if __name__ == "__main__":
    print("Intel oneAPI Python Matrix Multiplication Benchmark")
    print("===================================================")
    
    
    check_intel_optimization()
    
    
    sizes = [500, 1000, 2000]
    for size in sizes:
        print(f"\nRunning benchmark with {size}x{size} matrices:")
        numpy_time, intel_time = benchmark_multiplication(matrix_size=size, num_runs=3)
