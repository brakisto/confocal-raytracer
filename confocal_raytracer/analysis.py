import os
import glob
from chromatic_confocal.utils import read_csv, get_peak, normalize
import numpy as np
from tqdm import tqdm


def average_spectra(csvs: list, limit_to: int, n: int) -> np.ndarray:
    """Function to average spectra from ThorlabsSpectrum software

    Args:
        csvs (list): list with patsh to csv spectra files
        limit_to (int): limit number of spectra to be used
        n (int): average every n spectra
    Returns:
        avg_spectra (np.ndarray): array with limit_to // n number of spectra
        with its respective intensity and wavelength
    """
    spectra = np.zeros((len(csvs), 2, 3648))  # TODO: 3648 wavelenght values
    for i, csv_path in enumerate(csvs):
        df = read_csv(csv_path)
        spectra[i, 0, ...] = df.index
        spectra[i, 1, ...] = df.intensity

    avg_spectra = np.average(
        spectra.reshape(n, limit_to // n, 2, 3648), axis=0
    )

    return avg_spectra


def get_peaks(
    path: str, n: int, limit_to: int, num: int = 10, fitgauss=True
) -> np.ndarray:
    """Obtain peaks for each one of the directories. Each directory
    corresponds to different distances.

    Args:
        path (str): path to measurement directory.
        n (int): number of spectra to be averaged.
        limit_to (int): number of csv files to be used during calculations.
        num (int): number of values to interpolate between two real values.
        fitgauss (bool): if True fits a gaussian distribution over spectrum.
        If False makes a lowpass filter.
    Raises:
        ValueError: if n and limit_to do not stick to the constraints

    Returns:
        result, np.ndarray: matrix with mean and standard deviation for each
        one of the distances measured
    """
    if limit_to % n != 0:
        raise ValueError("'n' must be a multiple of 'limit_to'.")
    # List all directories with different distances
    dirs = sorted(os.listdir(path), key=lambda x: int(x))
    # Create result array which will store peaks and stds for each directory
    result = np.zeros((2, len(dirs)))
    # Go through each directory
    for j, dir in tqdm(enumerate(dirs), desc="Folders processed"):
        # List all csv files in a directory
        csvs = glob.glob(os.path.join(path, dir, "*.csv"))[:limit_to]
        # Average every "n" spectras
        avg_spectra = average_spectra(csvs, limit_to=limit_to, n=n)
        # Create empty array to store peak values
        array = np.zeros(len(avg_spectra))
        # Go through all averaged spectra
        for i in range(len(avg_spectra)):
            wavelenght = avg_spectra[i, 0, ...]
            intensity = normalize(avg_spectra[i, 1, ...])
            # Adjust to gaussian distribution and extract peak for averaged
            # spectrum
            peak = get_peak(
                wavelenght=wavelenght,
                intensity=intensity,
                num=num,
                fitgauss=fitgauss,
            )
            # plt.show()
            array[i] = peak

        result[0, j] = np.median(array)
        result[1, j] = np.std(array, ddof=1)

    return result
