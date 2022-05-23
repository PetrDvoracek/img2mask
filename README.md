# Awesome RGB to N-channels Mask Convertor for Image Segmentation

The image segmentation labels (aka masks) are usualy stored as 3-channel (RGB) images. This format is inappropriate for solutions based on neural networks, because some labels seems to be closer to each other in vector space than others (i.e. #000000 and #000011 is closer than #000000 and #FFFFFF). This usualy does not reflect the reality, all labels should be equally distant in general image segmentation task . For this purpose, labels must be converted from 3-channel to N-channel format, where N equals to number of classes. Labels in N-channel format are **orthogonal basis** from the mathematical perspective. 

## Contribute

Clone this repo, install dev dependencies with `pip install -r requirements-dev.txt`, run unittests with `python -m unittest tests/tests_convertor.py`, run performance tests with `python -m tests.performance`

## Common Problems
You will get following error when running `python tests/performance.py`:
```
Traceback (most recent call last):
  File "/home/somehome/img2mask/tests/performance.py", line 6, in <module>
    from src.img2mask import rgb2mask
ModuleNotFoundError: No module named 'src'
```
run performance test with  `python -m unittest tests/tests_convertor.py` to solve this error.