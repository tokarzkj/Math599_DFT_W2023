import numpy as np
import matplotlib.pyplot as plt
from numpy import real, imag


def cosine_samples(f, N) -> np.array:
    """
    Calculates N-samples of a specific cosine signal
    :param f: An integer
    :param N: A non-zero integer representing how many samples to take
    :return: N length vector containing samples of a cosine signal
    """
    signal_vector_results = np.empty((N, 1))
    for n in range(0, N):
        signal_vector_results[n] = np.cos((2 * np.pi * f * n) / N)

    return signal_vector_results


def sin_samples(f, N) -> np.array:
    """
    Calculates N samples of a specific sin signal
    :param f: An integer
    :param N: A non-zero integer representing how many samples to take
    :return: N length vector containing samples of a sin signal
    """
    signal_vector_results = np.empty((N, 1))
    for n in range(0, N):
        signal_vector_results[n] = np.sin((2 * np.pi * f * n) / N)

    return signal_vector_results


def box_signal_samples(N, M, u = 0) -> np.array:
    samples = np.empty(N)
    start = u
    end = M + u

    for n in range(start, end):
        samples[n] = 1

    return samples


def dft_transform(signal) -> np.array:
    """
    Use the DFT summation technique to transform a signal vector into frequency vector
    :param signal: N length vector containing samples of a signal
    :return: An N length vector of frequency samples
    """
    i = complex(0, 1)
    N = len(signal)

    dft_samples = np.empty((N, 1), dtype=np.complex_)

    for n in range(0, N):
        sample_summation = np.float64(0)
        for k in range(0, N):
            signal_sample = signal[k]
            sample_summation += signal_sample * np.exp((-2 * np.pi * i * k * n) / N)
        dft_samples[n] = sample_summation

    return dft_samples


def inverse_dft_transform(frequency) -> np.array:
    """
    Uses the inverse DFT summation technique to recover the signal from a frequency.
    Currently subject to some rounding errors when comparing to the original signal values.
    :param frequency: N length vector containing samples of a frequency
    :return: An N length vector of signal samples
    """
    i = complex(0, 1)
    N = len(frequency)
    signal_samples = np.empty((N, 1), dtype=np.float_)

    for k in range(0, N):
        frequency_summation = np.float64(0)
        for n in range(0, N):
            frequency_sample = frequency[n]
            frequency_summation += frequency_sample * np.exp((2 * np.pi * i * k * n) / N)
        signal_samples[k] = np.float64((1 / N) * frequency_summation)

    return signal_samples


if __name__ == '__main__':
    print("Please select an integer f:")
    f = int(input())
    print("Please select a non-negative integer N")
    N = int(input())
    print("Please select a lower boundary u for the box signal")
    u = int(input())

    print("Please select an upper boundary M for the box signal (Must be less than N)")
    M = int(input())

    while M >= N:
        print("Please select an upper boundary M for the box signal (Must be less than N)")
        M = int(input())

    cos_signal = cosine_samples(f, N)
    sin_signal = sin_samples(f, N)
    simple_box_signal = box_signal_samples(N, M)
    shifted_box_signal = box_signal_samples(N, M, u)

    cos_frequency = dft_transform(cos_signal)
    sin_frequency = dft_transform(sin_signal)
    simple_box_frequency = dft_transform(simple_box_signal)
    shifted_box_frequency = dft_transform(shifted_box_signal)

    idft_cos_signal = inverse_dft_transform(cos_frequency)
    idft_sin_signal = inverse_dft_transform(sin_frequency)
    idft_simple_box_signal = inverse_dft_transform(simple_box_frequency)
    idft_shifted_box_signal = inverse_dft_transform(shifted_box_frequency)

    x = list(range(N))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 4)
    fig.subplots_adjust(wspace=0.5, hspace=0.75)
    fig.set_figheight(9)
    fig.set_figwidth(14)

####################################################################
# Create the Cosine plots                                          #
####################################################################
    ax1[0].set_ylabel('Signal')
    ax1[0].set_xlabel('Sample')
    ax1[0].set_title('Cosine Signal')
    ax1[0].stem(x, cos_signal)

    ax1[1].set_ylabel('Frequency')
    ax1[1].set_xlabel('Sample')
    ax1[1].set_title('Real Cosine Frequency')
    ax1[1].stem(x, [real(r) for r in cos_frequency])

    ax1[2].set_ylabel('Frequency')
    ax1[2].set_xlabel('Sample')
    ax1[2].set_title('Imaginary Cosine Frequency')
    ax1[2].stem(x, [imag(i) for i in cos_frequency])

    ax1[3].set_ylabel('Signal')
    ax1[3].set_xlabel('Sample')
    ax1[3].set_title('IDFT Cosine Signal')
    ax1[3].stem(x, idft_cos_signal)

####################################################################
# Create the Sine plots                                            #
####################################################################
    ax2[0].set_ylabel('Signal')
    ax2[0].set_xlabel('Sample')
    ax2[0].set_title('Sine Signal')
    ax2[0].stem(x, sin_signal)

    ax2[1].set_ylabel('Frequency')
    ax2[1].set_xlabel('Sample')
    ax2[1].set_title('Real Sine Frequency')
    ax2[1].stem(x, [real(r) for r in sin_frequency])

    ax2[2].set_ylabel('Frequency')
    ax2[2].set_xlabel('Sample')
    ax2[2].set_title('Imaginary Sine Frequency')
    ax2[2].stem(x, [imag(i) for i in sin_frequency])

    ax2[3].set_ylabel('Frequency')
    ax2[3].set_xlabel('Sample')
    ax2[3].set_title('IDFT Sine Signal')
    ax2[3].stem(x, idft_sin_signal)

####################################################################
# Create the Simple Box plots                                      #
####################################################################
    ax3[0].set_ylabel('Signal')
    ax3[0].set_xlabel('Sample')
    ax3[0].set_title('Simple Box Signal')
    ax3[0].stem(x, simple_box_signal)

    ax3[1].set_ylabel('Frequency')
    ax3[1].set_xlabel('Sample')
    ax3[1].set_title('Real Simple Box Frequency')
    ax3[1].stem(x, [real(r) for r in simple_box_frequency])

    ax3[2].set_ylabel('Frequency')
    ax3[2].set_xlabel('Sample')
    ax3[2].set_title('Imaginary Simple Box Frequency')
    ax3[2].stem(x, [imag(i) for i in simple_box_frequency])

    ax3[3].set_ylabel('Signal')
    ax3[3].set_xlabel('Sample')
    ax3[3].set_title('IDFT Simple Box Signal')
    ax3[3].stem(x, idft_simple_box_signal)

####################################################################
# Create the Shifted Box plots                                     #
####################################################################
    ax4[0].set_ylabel('Signal')
    ax4[0].set_xlabel('Sample')
    ax4[0].set_title('Shifted Box Signal')
    ax4[0].stem(x, shifted_box_signal)

    ax4[1].set_ylabel('Frequency')
    ax4[1].set_xlabel('Sample')
    ax4[1].set_title('Real Shifted Box Frequency')
    ax4[1].stem(x, [real(r) for r in shifted_box_frequency])

    ax4[2].set_ylabel('Frequency')
    ax4[2].set_xlabel('Sample')
    ax4[2].set_title('Imaginary Shifted Box Frequency')
    ax4[2].stem(x, [imag(i) for i in shifted_box_frequency])

    ax4[3].set_ylabel('Signal')
    ax4[3].set_xlabel('Sample')
    ax4[3].set_title('IDFT Shifted Box Signal')
    ax4[3].stem(x, idft_shifted_box_signal)

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
