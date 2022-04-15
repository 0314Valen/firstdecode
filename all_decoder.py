#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import base64
import binascii
import html
import string
import urllib
import urllib.parse
import base128
import base36
import base58
import base91
import py3base92
from pyDes import CBC, des, PAD_PKCS5
import Crypto.Cipher.AES
import Crypto.Random
import Crypto.Cipher.DES3


class Cryptoall:
    def __init__(self):
        print("目前支持解密语言包括:rot47、rot18、rot13、rot5、des3、aes、des、\n"
              "维吉尼亚密码、莫斯密码、栅栏密码、凯撒密码、图片转base64、base64转成图片、\n"
              "base16、base32、base36、base58、base64、base85,RFC1924型（没什么卵用，就是花里胡哨）、base85,ASCII85型（ctf常用）、base91、base92、base128_2、base128_1、\n"
              "html解码、URL解码、utf-8转码、\xe4\xb8\xad\xe6\x96\x87转中文、字符转成二进制、二进制转成字符、二进制转十六进制、十六进制转二进制\n\n")
        # self.content=content
        # self.key=keys

    def six_to_chr(self, content):
        # unhexlify则执行反向操作,HEX转BIN：
        # content = '61626364'
        try:
            a = binascii.unhexlify(content)
            print('16进制转2进制字符:',a)
            return a
        except:
            print('binascii.unhexlify-------------------------------解密失败')
            return False

    def chr_to_six(self, content):
        # hexlify作用是二进制转十六进制，产生的字串是源数据两倍长度
        # content=binascii.hexlify
        try:
            a = binascii.b2a_hex(bytes(content, 'utf-8'))
            print('2进制转16进制字符:',a)
            return a
        except:
            print('binascii.hexlify-------------------------------解密失败')
            return False

    def two_to_chr(self, content):
        # 二进制转字符
        # 011011110011100001000100011011000111100001001011001010110100100000111000011101110111001101101001010110000110010100101111010001010101001001000110011100000100000101001101011000010100001001010000011010010100100101100011011010100011000101110011010010000111100101000111010011110100110101101101010100010100010001101011010010110010101101110101010110000111001101010110010110100110011101110010011001010011010101000100010100110101100001110111001111010011110101101000011010000110100001101000011010000110100001101000011010000110100001101000011010000110100001101000011010000110100001101000
        try:
            if len(content) / 8 == 0:
                content = content
            else:
                d = len(content) % 8
                content = content[:-d]
            a = int(content, 2)
            b = a.to_bytes((a.bit_length() + 7) // 8, 'big').decode()
            print('二进制转换ASCII:', b)
            return b
        except:
            print('二进制转换ASCII-------------------------------解密失败')
            return False

    def chr_to_two(self, content):
        # 字符转成二进制
        try:
            a = bin(int.from_bytes(content.encode(), 'big'))
            print('ASCII转换二进制:', a)
            return False
        except:
            print('ASCII转换二进制-------------------------------解密失败')
            return False

    def str_to_str(self, content):
        # \xe4\xb8\xad\xe6\x96\x87
        try:
            s = content.encode('raw_unicode_escape').decode()
            print('\\x转字符:',s)
            return s
        except:
            print('\\x转字符-------------------------------解密失败')
            return False

    def Unicode(self, content):
        try:
            # 转为utf-8(明文)
            a = content.encode('utf8').decode('unicode_escape')
            print(a)
            # 转为utf-8编码
            b = content.encode('utf8').decode('unicode_escape').encode('utf8')
            print('UnicodeUTF-8解码:',b)
            return False
        except:
            print('UnicodeUTF-8解码-------------------------------解密失败')
            return False

    def urldecode(self, content):
        # %E7%BC%96%E7%A0%81
        try:
            str2 = urllib.parse.quote(content)  # 将字符串进行编码
            print(str2)  #
            str3 = urllib.parse.unquote(content)  # 解码字符串
            print('URL编码:',str3)  # str3=url编码
        except:
            print('URL编码-------------------------------解密失败')
            return False

    def htmlencode(self, content):
        # a='&lt;li&gt;&#26085;&#21888;&#21017;'
        try:
            a = html.unescape(content).encode('utf-8')
            print("转html:",a)
            return a
        except:
            print('html解密-------------------------------解密失败')
            return False

    def decrypt(self, content):
        try:
            mydisc = {'坤': '000000', '剥': '000001', '比': '000010', '观': '000011', '豫': '000100', '晋': '000101',
                      '萃': '000110', '否': '000111', '谦': '001000', '艮': '001001', '蹇': '001010', '渐': '001011',
                      '小过': '001100',
                      '旅': '001101',
                      '咸': '001110', '遁': '001111', '师': '010000', '蒙': '010001', '坎': '010010', '涣': '010011',
                      '解': '010100',
                      '未济': '010101', '困': '010110', '讼': '010111', '升': '011000', '蛊': '011001', '井': '011010',
                      '巽': '011011',
                      '恒': '011100', '鼎': '011101', '大过': '011110', '姤': '011111', '复': '100000', '颐': '100001',
                      '屯': '100010',
                      '益': '100011', '震': '100100', '噬嗑': '100101', '随': '100110', '无妄': '100111', '明夷': '101000',
                      '贲': '101001', '既济': '101010', '家人': '101011', '丰': '101100', '离': '101101', '革': '101110',
                      '同人': '101111', '临': '110000', '损': '110001', '节': '110010', '中孚': '110011', '归妹': '110100',
                      '睽': '110101', '兑': '110110', '履': '110111', '泰': '111000', '大畜': '111001', '需': '111010',
                      '小畜': '111011',
                      '大壮': '111100', '大有': '111101', '夬': '111110', '乾': '111111'}
            keys = ['坤', '剥', '比', '观', '豫', '晋', '萃', '否', '谦', '艮', '蹇', '渐', '小过', '旅', '咸', '遁', '师', '蒙', '坎', '涣',
                    '解', '未济', '困', '讼', '升', '蛊', '井', '巽', '恒', '鼎', '大过', '姤', '复', '颐', '屯', '益', '震', '噬嗑', '随',
                    '无妄', '明夷',
                    '贲', '既济', '家人', '丰', '离', '革', '同人', '临', '损', '节', '中孚', '归妹', '睽', '兑', '履', '泰', '大畜', '需',
                    '小畜',
                    '大壮', '大有', '夬', '乾']
            for each in keys:
                content = content.replace(each, mydisc[each])
            print('伏羲六十四:',content)
            return content
        except:
            print('伏羲六十四-------------------------------解密失败')
            return False

    def b128decode1(self, content):
        # base128解密1
        # m = b128.encode(plain_text.encode(encoding="utf-8"))  # 加密
        try:
            a = base128.base128.encode((content.encode("utf-8")).decode("utf-8"))
            print('base128:',a)
            return a
        except:
            print('base128第一次-------------------------------解密失败')
            return False

    def b128decode2(self, content):
        # base128解密2
        # b128 = base128.base128(chars = None, chunksize = 7)
        # m = b128.encode(plain_text.encode(encoding="utf-8"))  # 加密
        # c = b''.join(b128.decode(cipher_text)).decode()   #解密
        try:
            c = b''.join(base128.base128(chars=None, chunksize=7).decode(content)).decode()
            print('base128:',c)
            return c
        except:
            print('base128第二次-------------------------------解密失败')
            return False

    def b92decode(self, content):
        # base92解密
        # m = py3base92.encode(plain_text)  #加密
        # c = py3base92.decode(cipher_text) #解密
        try:
            a = py3base92.b92decode(content.encode("utf-8")).decode("utf-8")
            print('base92:',a)
            return a
        except:
            print('base92-------------------------------解密失败')
            return False

    def b91decode(self, content):
        # base91解密
        # m = base91.encode(plain_text.encode('utf-8')) #加密
        # c = base91.decode(cipher_text).decode()       #解密
        try:
            a = base91.encode(content.encode("utf-8")).decode("utf-8")
            print('base91:', a)
            return a
        except:
            try:
                a = base91.decode(content).decode()
                print('base91:', a)
                return a
            except:
                print('base91-------------------------------解密失败')
                return False

    def a85decode(self, content):
        # base85第二次解密，#RFC1924型（没什么卵用，就是花里胡哨）
        # m = base64.b85encode(plain_text.encode('utf-8')).decode()#加密
        # c = base64.a85decode(cipher_text).decode() #解密
        try:
            a = base64.b85decode(content.encode("utf-8")).decode("utf-8")
            print('abase85:', a)
            return a
        except:
            print('base85-------------------------------第二次解密失败')
            return False

    def b85decode(self, content):
        # base85第一次解密，###ASCII85型（ctf常用）
        # m = base64.a85encode(plain_text.encode('utf-8')).decode()#加密
        # c = base64.b85decode(cipher_text).decode() #解密
        try:
            a = base64.a85decode(content.encode("utf-8")).decode("utf-8")
            print('bbase85:', a)
            return a
        except:
            print('base85-------------------------------第一次解密失败')
            return False

    def b64decode(self, content):
        # base64解密
        # m = base64.b64encode(plain_text.encode('utf-8')).decode() #加密
        # c = base64.b64decode(cipher_text).decode() #解密
        try:
            a = base64.b64decode(content.encode("utf-8")).decode("utf-8")
            print('base64:', a)
            return a
        except:
            print('base64-------------------------------解密失败')
            return False

    def b58decode(self, content):
        # base58解密
        # m =  base58.b58encode(plain_text.encode('utf-8')).decode() #加密
        # c =  base58.b58decode(cipher_text).decode() #解密
        try:
            a = base58.b58decode(content.encode("utf-8")).decode("utf-8")
            print('base58:', a)
            return a
        except:
            print('base58-------------------------------解密失败')
            return False

    def b36decode(self, content):
        # base36解密
        # c = base36.dumps(int(cipher_text)) #解密
        # m = base36.loads(plain_text)       #加密
        try:
            a = base36.dumps(int(content.encode("utf-8")).decode("utf-8"))
            print('base36:', a)
            print('base36:', base36.dumps(int(content)))
            return a
        except:
            print('base36-------------------------------解密失败')
            return False

    def b32decode(self, content):
        # base32解密
        # m = base64.b32decode(cipher_text).decode()  # 解密
        # c = base64.b32encode(plain_text.encode('utf-8')).decode()  # 加密
        try:
            a = base64.b32decode(content.encode("utf-8")).decode("utf-8")
            print('base32:', a)
            return a
        except:
            print('base32-------------------------------解密失败')
            return False

    def b16decode(self, content):
        # base16解密
        # c = base64.b16decode(cipher_text)  #加密
        # m = base64.b16encode(plain_text) #解密
        try:
            a = base64.b16decode(content.encode("utf-8")).decode("utf-8")
            print('base16:', a)
            return a
        except:
            print('base16-------------------------------解密失败')
            return False

    def img_to_base64(self):
        # image转base64
        try:
            with open(r"1.jpg", "rb") as f:  # 转为二进制格式
                base64_data = str(base64.b64encode(f.read()), encoding='utf-8')  # 使用base64进行加密
                print(base64_data)
                file = open('1.txt', 'wt')  # 写成文本格式
                file.write(base64_data)
                file.close()
            return False
        except:
            print('image转base64-------------------------------解密失败')
            return False

    def base_to_img(self, content):
        # base64转为图片
        try:
            # a = "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"
            with open('1.txt', 'rb') as f:
                content = f.read()
            imgdata = base64.b64decode(content)
            file = open('1.jpg', 'wb')
            file.write(imgdata)
            file.close()
            print('base64转为image')
        except:
            print('base64转为image-------------------------------解密失败')
            return False

    def VigenereDecrypto(self, output, key):
        # 请输入需要解密的字符：NIMCIGTURIBNMUMRZMABUK
        # 请输入Key:beijingmeetatnineinthe
        # 解密后的字符： meetatnineintheevening
        try:
            # 实现列表元素对应相减（解密部分）
            def sub_list(x, y):
                result = []
                for i in range(len(x)):
                    z = x[i] - y[i]
                    result.append(z)
                return result

            # 构造映射 字符---->num
            def c2n():
                list_c = []
                list_n = []
                for i in range(26):
                    list_n.append(i)
                    list_c.append(chr(i + 97))
                dic_c2n = dict(map(lambda x, y: [x, y], list_c, list_n))
                return dic_c2n

            # 构造映射 num---->字符
            def n2c():
                list_c = []
                list_n = []
                for i in range(26):
                    list_n.append(i)
                    list_c.append(chr(i + 97))
                dic_n2c = dict(map(lambda x, y: [x, y], list_n, list_c))
                return dic_n2c

            # 解密
            def decode(s, key):
                print('解密后的字符： ', end='')
                dic_c2n = c2n()
                dic_n2c = n2c()
                list_s = []
                list_key = []
                list_finall = []
                for i in s:
                    i = i.lower()
                    list_s.append(dic_c2n[i])
                for i in key:
                    i = i.lower()
                    list_key.append(dic_c2n[i])
                for i in list_key:
                    if len(list_key) < len(list_s):
                        list_key.append(i)
                list_result = sub_list(list_s, list_key)
                for i in list_result:
                    if i < 0:
                        i += 26
                    list_finall.append(dic_n2c[i])
                for i in list_finall:
                    print(i, end='')
                return i

            a = decode(output, key)
            print('维吉尼亚密码:',a)
            return a
        except:
            print('维吉尼亚密码-------------------------------解密失败')
            return False

    def caesar_Crypto(self, content):
        try:
            lowercase = 'abcdefghijklmnopqrstuvwxyz'
            uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            result = []
            offset = 1
            while offset <= 26:
                temp = []
                for char in content:
                    if char in lowercase:
                        temp.append(chr(97 + (ord(char) - 97 + offset) % 26))
                    elif char in uppercase:
                        temp.append(chr(65 + (ord(char) - 65 + offset) % 26))
                    else:
                        temp.append(char)
                string = "".join(temp)
                # print(admin)
                result.append(string)
                offset += 1
            print('凯撒密码:',result)
        except:
            print('凯撒密码-------------------------------解密失败')

    def railfence(self, string):
        try:
            if string < 50:
                def generate_w(string, n):
                    '''将字符排列成w型'''
                    array = [['.'] * len(string) for i in range(n)]  # 生成初始矩阵
                    row = 0
                    upflag = False
                    for col in range(len(string)):  # 在矩阵上按w型画出string
                        array[row][col] = string[col]
                        if row == n - 1:
                            upflag = True
                        if row == 0:
                            upflag = False
                        if upflag:
                            row -= 1
                        else:
                            row += 1
                    return array

                def decode(string, n):
                    '''解密'''
                    array = generate_w(string, n)
                    sub = 0
                    for row in range(n):  # 将w型字符按行的顺序依次替换为string
                        for col in range(len(string)):
                            if array[row][col] != '.':
                                array[row][col] = string[sub]
                                sub += 1
                    msg = []
                    for col in range(len(string)):  # 以列的顺序依次连接各字符
                        for row in range(n):
                            if array[row][col] != '.':
                                msg.append(array[row][col])
                    return array, msg

                print("栅栏密码成功")
                for n in range(2, len(string)):  # 遍历所有可能的栏数
                    print(str(n) + '栏：' + ''.join(decode(string, n)[1]))
            else:
                return False
        except:
            print('栅栏密码-------------------------------解密失败')

    def des_descrypt(self, content, key):
        """
        DES 解密
        Python 语言采用 pyDes 作为 DES 加解密处理的包。DES 解密时采用 CBC 模式，并采用 PAD_PKCS5 作为填充模式，使用解密密钥作为初始化向量。
        """
        try:
            iv = key
            k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
            de = k.decrypt(binascii.a2b_hex(content), padmode=PAD_PKCS5)
            print('DES 解密:',de)
        except:
            print('DES 解密-------------------------------解密失败')

    def aes_encode(self, content, key):
        try:
            def auto_fill(x):
                if len(x) <= 32:
                    while len(x) not in [16, 24, 32]:
                        x += " "
                    return x.encode()
                else:
                    raise Exception("密钥长度不能大于32位！")

            x = Crypto.Cipher.AES.new(auto_fill(key), Crypto.Cipher.AES.MODE_ECB)
            a = base64.encodebytes(x.encrypt(auto_fill(content)))
            b = x.decrypt(base64.decodebytes(a))
            print(a)
            print(b)
            a = binascii.b2a_base64(x.encrypt(auto_fill(content)))
            b = x.decrypt(binascii.a2b_base64(a))
            print(a)
            print(b)
            iv = Crypto.Random.new().read(16)  # 向量，必须为16字节
            y = Crypto.Cipher.AES.new(auto_fill(key), Crypto.Cipher.AES.MODE_CBC, iv)
            c = binascii.b2a_base64(y.encrypt(auto_fill(content)))
            z = Crypto.Cipher.AES.new(auto_fill(key), Crypto.Cipher.AES.MODE_CBC, iv)
            d = z.decrypt(binascii.a2b_base64(c))
            print(c)
            print(d)
            print('AES解密上面是')
        except:
            print('AES解密-------------------------------解密失败')

    def des3_encode(self, content, key):
        try:
            def auto_fill(x):
                if len(x) > 24:
                    raise Exception("密钥长度不能大于等于24位！")
                else:
                    while len(x) < 16:
                        x += " "
                    return x.encode()

            x = Crypto.Cipher.DES3.new(auto_fill(key), Crypto.Cipher.DES3.MODE_ECB)
            a = base64.encodebytes(x.encrypt(auto_fill(content)))
            print(a)
            b = x.decrypt(base64.decodebytes(a))
            print(b)
            a = binascii.b2a_base64(x.encrypt(auto_fill(content)))
            b = x.decrypt(binascii.a2b_base64(a))
            print(a)
            print(b)
            print('des3上面')
        except:
            print('des3-------------------------------解密失败')

    def rot5decoder(self, content):
        try:
            res = ''
            dict_rot5 = {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '0', '6': '1', '7': '2', '8': '3',
                         '9': '4'}
            for i in content:
                value = ord(i)
                if (value <= 57) and (value >= 48):
                    res += dict_rot5[i]
                else:
                    res += i
                    continue
            print('rot5:',res)
            return res
        except:
            print('rot5-------------------------------解密失败')
            return False

    def rot13decoder(self, crypt_str, shift=13):
        try:
            crypt_list = list(crypt_str)
            plain_str = ""
            num = int(shift)
            for ch in crypt_list:
                ch = ord(ch)
                if ord('a') <= ch and ch <= ord('z'):
                    ch = ch + num
                    if ch > ord('z'):
                        ch -= 26
                if ord('A') <= ch and ch <= ord('Z'):
                    ch = ch + num
                    if ch > ord('Z'):
                        ch -= 26
                a = chr(ch)
                plain_str += a
            print('rot13:', plain_str)
            return plain_str
        except:
            print('rot13-------------------------------解密失败')
            return False

    def rot18decoder(self, content):
        try:
            res = ''
            dict_rot5 = {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '0', '6': '1', '7': '2', '8': '3',
                         '9': '4'}
            keys_rot18 = str(string.ascii_lowercase) + str(string.ascii_uppercase)
            values_rot18 = [chr((ord(i) + 13 - 97) % 26 + 97) for i in string.ascii_lowercase] + [
                chr((ord(i) + 13 - 65) % 26 + 65) for i in string.ascii_uppercase]
            dict_rot18 = dict((zip(keys_rot18, values_rot18)), **dict_rot5)
            for index_key in content:
                try:
                    res += dict_rot18[index_key]
                except:
                    res += index_key
                    pass
            print('rot18:', res)
            return res
        except:
            print('rot18-------------------------------解密失败')
            return False

    def rot47decoder(self, content):
        try:
            x = []
            for i in range(len(content)):
                j = ord(content[i])  # 字符在ASCII中的序号
                if j >= 33 and j <= 126:  # 用于ROT47编码的字符其ASCII值范围是33－126
                    x.append(chr(33 + ((j + 14) % 94)))
                else:
                    x.append(content[i])
            a = "".join(x)
            print('rot47:', a)
            return a
        except:
            print('rot47-----------------------------解密失败')
            return False

    def mosdecrypt(self, content):
        try:
            MorseList = {'A': ".-",
                         'B': "-...",
                         'C': "-.-.",
                         'D': "-..",
                         'E': ".",
                         'F': "..-.",
                         'G': "--.",
                         'H': "....",
                         'I': "..",
                         'J': ".---",
                         'K': "-.-",
                         'L': ".-..",
                         'M': "--",
                         'N': "-.",
                         'O': "---",
                         'P': ".--.",
                         'Q': "--.-",
                         'R': ".-.",
                         'S': "...",
                         'T': "-",
                         'U': "..-",
                         'V': "...-",
                         'W': ".--",
                         'X': "-..-",
                         'Y': "-.--",
                         'Z': "--..",
                         '1': ".----",
                         '2': "..---",
                         '3': "...--",
                         '4': "....-",
                         '5': ".....",
                         '6': "-....",
                         '7': "--...",
                         '8': "---..",
                         '9': "----.",
                         '0': "-----",
                         '.': ".-.-.-",
                         '?': "..--..",
                         '!': "-.-.--",
                         '(': "-.--.",
                         '@': ".--.-.",
                         ':': "---...",
                         '=': "-...-",
                         '-': "-....-",
                         ')': "-.--.-",
                         '+': ".-.-.",
                         ',': "--..--",
                         '\'': ".----.",
                         '_': "..--.-",
                         '$': "...-..-",
                         ';': "-.-.-.",
                         '/': "-..-.",
                         '\"': ".-..-.",
                         '&': ".-...",
                         }
            if ' ' in content:
                lmorsecodeList = content.split(" ")
            else:
                lmorsecodeList = content.split("/")
            flag = ''
            for char in lmorsecodeList:
                for k, v in MorseList.items():
                    if v == char:
                        flag = flag + k
            print("莫斯密码:",flag)
            return flag
        except:
            print('莫斯密码-------------------------------解密失败')
            return False

    def toy_story(self, content):
        try:
            cipherdic = {'M': 'ACEG', 'R': 'ADEG', 'K': 'BCEG', 'S': 'BDEG', 'A': 'ACEH', 'B': 'ADEH', 'L': 'BCEH',
                         'U': 'BDEH', 'D': 'ACEI', 'C': 'ADEI', 'N': 'BCEI', 'V': 'BDEI', 'H': 'ACFG', 'F': 'ADFG',
                         'O': 'BCFG', 'W': 'BDFG', 'T': 'ACFH', 'G': 'ADFH', 'P': 'BCFH', 'X': 'BDFH', 'E': 'ACFI',
                         'I': 'ADFI', 'Q': 'BCFI', 'Y': 'BDFI'}
            # cipher = 'BCEHACEIBDEIBDEHBDEHADEIACEGACFIBDFHACEGBCEHBCFIBDEGBDEGADFGBDEHBDEGBDFHBCEGACFIBCFGADEIADEIADFH'
            flag = ''
            for i in range(0, len(content), 4):
                for k, v in cipherdic.items():
                    if v == content[i:i + 4]:
                        flag = flag + k
            print('toy_stort:',flag)
            return flag
        except:
            print('toy_stort-------------------------------解密失败')
            return False

    def toy_story_d(self, content):
        try:
            original_list = ['M', 'R', 'K', 'S', 'A', 'B', 'L', 'U', 'D', 'C', 'N', 'V', 'H', 'F', 'O', 'W', 'T', 'G',
                             'P', 'X', 'E', 'I', 'Q', 'Y']
            reversed_list = original_list[::-1]  # 倒装后的表
            flag = ''
            for char in content:
                for i in range(len(original_list)):
                    if original_list[i] == char:
                        flag = flag + reversed_list[i]
            print('toy_stort_d:',flag)
            return flag
        except:
            print('toy_stort_d-------------------------------解密失败')
            return False

    def operate_decoder(self, content):
        try:
            charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
            ret = []
            plaintext = [i for i in content.split('0')]
            for i in plaintext:
                tmp = 0
                for j in range(len(i)):
                    tmp += int(i[j])
                ret.append(charList[tmp - 1])
            print('云影密码',''.join(ret).lower())
            return ''.join(ret).lower()
        except:
            print('云影密码-------------------------------解密失败')
            return False


if __name__ == '__main__':
    content = input('需要界面的字符串')
    key = input('需要界面的字符串对应key，没有则直接回车')
    cr = Cryptoall()

    cr.rot47decoder(content)  # rot47
    cr.rot18decoder(content)  # rot18
    cr.rot13decoder(content)  # rot13
    cr.rot5decoder(content)  # rot5

    cr.des3_encode(content, key)  # des3
    cr.aes_encode(content, key)  # aes
    cr.des_descrypt(content, key)  # des
    cr.VigenereDecrypto(content, key)  # 维吉尼亚密码,解不出ci{v3erf_0tygidv2_fc0}的key是xinan
    cr.toy_story(content)  # toy_stort解密
    cr.toy_story_d(content)  # toy_stort解密

    cr.mosdecrypt(content)  # 莫斯密码
    cr.railfence(content)  # 栅栏密码,解不出kanbbrgghjl{zb____}vtlaln,fa{i3eei_0llgvgn2_sc0}
    cr.caesar_Crypto(content)  # 凯撒密码
    cr.operate_decoder(content)  # 云影密码

    cr.img_to_base64()  # 图片转base64
    cr.base_to_img(content)  # base64转成图片
    cr.b16decode(content)  # base16
    cr.b32decode(content)  # base32     存在问题
    cr.b36decode(content)  # base36
    cr.b58decode(content)  # base58
    cr.b64decode(content)  # base64
    cr.b85decode(content)  # base85,RFC1924型（没什么卵用，就是花里胡哨）
    cr.a85decode(content)  # base85,ASCII85型（ctf常用）
    cr.b91decode(content)  # base91
    cr.b92decode(content)  # base92
    cr.b128decode2(content)  # base128_2
    cr.b128decode1(content)  # base128_1
    cr.decrypt(content)  # 伏羲64
    cr.htmlencode(content)  # html解码
    cr.urldecode(content)  # URL解码
    cr.Unicode(content)  # utf-8转码
    cr.str_to_str(content)  # \xe4\xb8\xad\xe6\x96\x87转中文
    cr.chr_to_two(content)  # 字符转成二进制
    cr.two_to_chr(content)  # 二进制转成字符
    cr.chr_to_six(content)  # 二进制转十六进制
    cr.six_to_chr(content)  # 十六进制转二进制
