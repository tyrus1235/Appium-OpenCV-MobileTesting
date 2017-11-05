# Appium-OpenCV-MobileTesting
A Python class with helper functions for developing automated test scripts for mobile games.

## Prerequisites

 * Python (2.7 or 3+)
 * OpenCV Python library

```
pip install opencv-python
```
 * NumPy

```
pip install numpy
```
## Functions

 * find_matches(mat screenshot, mat template, float threshold)
    * Uses OpenCV's Template Matching to find any matches between a screenshot (matrix) and a template (matrix).
    * The threshold is a floating point number between 0 and 1 that determines how precise the matching will be (with 1 being the most precise).
    * It returns an array of coordinates with each coordinate being a match found. Those coordinates come from the screenshot matrix.
    * Ex.:
```
find_matches(screenshotMatrix, templateMatrix, 0.8)
```

 * wait_for_loading(self, string pathToTemplate, string pathToScreenshot, int timeout)
    * Waits for a loading screen to end - has a timeout (in seconds) so it does not keep waiting forever (and the test will fail if the timeout is reached).
    * Note that the screenshot path does not need to point to an exisiting image (it will be created at that path and with that filename).
    * Ex.:
```
wait_for_loading(self, '/path/to/template/file', '/path/to/screenshot/file', 60)
```

  * skip_ads(self, string pathToTemplate, string pathToAlternateTemplate, string pathToScreenshot, int timeout)
    * Skips an ad screen - has a timeout (in seconds) so it does not keep waiting forever (and the test will fail if the timeout is reached).
    * Note that the screenshot path does not need to point to an exisiting image (it will be created at that path and with that filename).
    * Ex.:
```
skip_ads(self, '/path/to/template/file', '/path/to/alternate/template/file', '/path/to/screenshot/file', 60)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

  * My professors, Dr. Endo and Dr. Nardi, who helped guide this project.