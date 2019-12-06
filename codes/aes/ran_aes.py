# -*-coding:gbk*-

import time
import random
import logging
from Crypto.Cipher import AES,DES3,ARC4
import binascii
import base64

logging.basicConfig(level=logging.DEBUG,
                    filename='./log-20191206-AES(CBC)-crypt-' + '-' + '.log',
                    filemode='a+',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

ran_box = [ '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def get_random_16bytes():
    # 得到随机加密的字节数组
    res_ans = ""
    for i in range(32):
        res_ans += ran_box[random.randint(0, len(ran_box)-1)]
    return res_ans

def ms_time_count(func1,func2,alg,mode,data,key,n):
    """
    :param func1: 算法函数 加密函数
    :param func2: 解密函数
    test_time: 函数计算时间 由t1-t0得到
    alg: 算法名称
    mode：模式
    data:测试数据
    key:测试key
    res:测试结果
    n:测试次数
    :return:
    """
    t0 = time.perf_counter()
    # 加密
    res = func1(data)
    t1 = time.perf_counter()
    test_time = (t1 - t0) * 1000
    # 加密日志
    func_log_en(test_time,alg,mode,data,key,res,n)
    t3 = time.perf_counter()
    # 解密
    ans = func2(res)
    t4 = time.perf_counter()
    test_time = (t4 - t3) * 1000
    # 解密日志
    func_log_de(test_time,alg,mode,res,key,ans,n)

def func_log_en(test_time,alg,mode,data,key,res,n):
    """
    加密结果写日志
    :param
    test_time: 函数计算时间 由t1-t0得到
    alg: 算法名称
    mode：模式
    data:测试数据
    key:测试key
    res:测试结果
    n:测试次数
    :return:
    """
    logging.info(str(alg)+"算法"+
                 str(mode)+'-'+
                 '使用密钥'+str(key)+
                 " 加密数据"+str(data)+ "加密得到数据"+str(res)+
                 " 加密第"+str(n)+"次消耗时间" +
                 str(test_time) + "ms")

def func_log_de(test_time,alg,mode,data,key,res,n):
    """
    解密结果写日志
    :param
    test_time: 函数计算时间 由t1-t0得到
    alg: 算法名称
    mode：模式
    data:测试数据
    key:测试key
    res:测试结果
    n:测试次数
    :return:
    """
    logging.info(str(alg)+"算法"+
                 str(mode)+'-'+
                 '使用密钥'+str(key)+
                 " 解密数据,"+str(data)+ "解密得到数据"+str(res)+
                 " 解密第"+str(n)+"次消耗时间" +
                 str(test_time) + "ms")

def encrypt(data):
    demo = AES.new(binascii.unhexlify("404142434445464748494A4B4C4D4E4F"),mode=AES.MODE_CBC,iv=binascii.unhexlify("00000000000000000000000000000000"))
    data = binascii.unhexlify(data)
    res = demo.encrypt(data)
    return res.hex()

def decrypt(data):
    demo = AES.new(binascii.unhexlify("404142434445464748494A4B4C4D4E4F"),mode=AES.MODE_CBC,iv=binascii.unhexlify("00000000000000000000000000000000"))
    data = binascii.unhexlify(data)
    res = demo.decrypt(data)
    return res.hex()

for i in range(1000):
    test_data = get_random_16bytes()
    # 加密函数
    func1 = encrypt
    func2 = decrypt
    # def ms_time_count(func1, func2, alg, mode, data, key, n):
    ms_time_count(func1,func2 ,alg='AES',mode='AES.MODE_CBC',data=test_data,key='404142434445464748494A4B4C4D4E4F',n=i)








