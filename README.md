# IntelMat - Intel oneAPI Python Matrix Acceleration
![Intel oneAPI](https://img.shields.io/badge/Intel%20oneAPI-Python%20MatrixAcceleration-blue) ![License](https://img.shields.io/github/license/0xSaikat/IntelMat)

#### Northern University of Business & Technology Khulna | Python & AI enthusiast. Building fast, optimized tools for ML, data, and scientific computing.

This repository demonstrates the use of Intel technologies to accelerate matrix operations in Python. It leverages Intel's oneAPI ecosystem, specifically focusing on Intel optimizations for NumPy operations.

## Intel Technologies Used

- **Intel Extension for NumPy**: Optimizes NumPy operations on Intel CPUs using Intel oneAPI Math Kernel Library (oneMKL)
- **Intel Distribution for Python**: Provides accelerated Python packages optimized for Intel architectures
- **Intel Math Kernel Library (MKL)**: High-performance math routines for science, engineering, and financial applications

## Project Description

The project demonstrates matrix multiplication acceleration using Intel's optimized libraries. It compares the performance of standard NumPy operations with Intel-optimized equivalents to showcase the potential speedup.

### Key Features:

1. Benchmark functionality to compare standard vs Intel-optimized matrix multiplication
2. Automatic detection of available Intel extensions
3. Performance comparison across different matrix sizes
4. Verification of computational correctness

## Requirements

- Python 3.6+
- NumPy
- Intel Extension for NumPy (`pip install intel-extension-for-numpy`)
- (Optional) py-cpuinfo for CPU detection (`pip install py-cpuinfo`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/0xSaikat/IntelMat.git
   cd IntelMat
   ```

2. Install dependencies:
   ```
   python -m pip install -i https://pypi.anaconda.org/intel/simple numpy
   ```

## Usage

Run the benchmark script:

```bash
python3 intel-mat.py
```

This will:
1. Check for Intel optimizations
2. Run benchmarks on different matrix sizes
3. Compare performance between standard NumPy and Intel-optimized operations

## Expected Results

On Intel hardware, you should see significant performance improvements when using Intel-optimized libraries, particularly for larger matrices. The benchmark reports speedup factors and verifies that the computational results match.

## Why This Matters

Matrix operations are fundamental to many scientific computing, machine learning, and data science workflows. By leveraging Intel's specialized libraries, we can achieve significant performance improvements on Intel hardware without changing application code.

This project demonstrates Intel's commitment to providing optimized software libraries that take advantage of hardware capabilities to accelerate Python-based workloads.

## About Me

I am **Sakil Hasan Saikat**, a cybersecurity enthusiast and the founder of [HackBit](https://hackbit.org). I specialize in offensive security, penetration testing, and building automated tools for cybersecurity research. My passion for ethical hacking has driven me to create several tools that contribute to the security community.

You can learn more about my work on my personal website: [https://saikat.hackbit.org](https://saikat.hackbit.org).

Connect with me on [LinkedIn](https://www.linkedin.com/in/0xsaikat/) for updates and collaborations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Intel oneAPI team for developing high-performance computing libraries
- NumPy project for providing the foundation for numerical computing in Python

<br>
<br>
<br>

  <h6 align="center">By the Hackers for the Hackers!</h6>

<div align="center">
  <a href="https://github.com/0xSaikat"><img src="https://img.icons8.com/material-outlined/20/808080/github.png" alt="GitHub"></a>
  <a href="https://twitter.com/0xSaikat"><img src="https://img.icons8.com/material-outlined/20/808080/twitter.png" alt="X"></a>
</div>
