import base64

with open('O:/enc_flag') as f:
    flag_file = f.read()
    try:
        for i in range(0, 10):
            flag_file = (lambda flag: base64.b64decode(flag).decode('UTF-8') )(flag_file)
            print(flag_file)
    except:
        print('decode complete!')
