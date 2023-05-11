# repetitions

## Description:
Can you make sense of this file?

Download the file [here](https://artifacts.picoctf.net/c/475/enc_flag).

## Hints:
1. Multiple decoding is always good.

## Tags:
picoCTF 2023

General Skills

base64

## solve:
這題提到了base64，而且文件尾有兩個=，基本上可以判斷他是要將base64解碼回UTF-8。所以我就用Python寫了解碼程式，解碼一次後還是沒看到flag的蹤影，提示又說多重解碼，所以我更改程式讓它多解碼幾次，flag就出現了。

Python解碼程式:

```python
import base64

with open('YOUR_ROUTE/enc_flag') as f:
    flag_file = f.read()
    try:
        for i in range(0, 10):
            flag_file = (lambda flag: base64.b64decode(flag).decode('UTF-8') )(flag_file)
            print(flag_file)
    except:
        print('decode complete!')

```

## flag:
**picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}**