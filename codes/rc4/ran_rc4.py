# -*-coding:gbk*-

import time
import random
import logging
from Crypto.Cipher import AES,DES3,ARC4
import binascii
import base64

logging.basicConfig(level=logging.DEBUG,
                    filename='./log-20191206-RC4-crypt-' + '-' + '.log',
                    filemode='a+',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

ran_box = [ '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def get_random_16bytes():
    # �õ�������ܵ��ֽ�����
    res_ans = ""
    for i in range(32):
        res_ans += ran_box[random.randint(0, len(ran_box)-1)]
    return res_ans

def ms_time_count(func1,func2,alg,mode,data,key,n):
    """
    :param func1: �㷨���� ���ܺ���
    :param func2: ���ܺ���
    test_time: ��������ʱ�� ��t1-t0�õ�
    alg: �㷨����
    mode��ģʽ
    data:��������
    key:����key
    res:���Խ��
    n:���Դ���
    :return:
    """
    t0 = time.perf_counter()
    # ����
    res = func1(data)
    t1 = time.perf_counter()
    test_time = (t1 - t0) * 1000
    # ������־
    func_log_en(test_time,alg,mode,data,key,res,n)
    t3 = time.perf_counter()
    # ����
    ans = func2(res)
    t4 = time.perf_counter()
    test_time = (t4 - t3) * 1000
    # ������־
    func_log_de(test_time,alg,mode,res,key,ans,n)

def func_log_en(test_time,alg,mode,data,key,res,n):
    """
    ���ܽ��д��־
    :param
    test_time: ��������ʱ�� ��t1-t0�õ�
    alg: �㷨����
    mode��ģʽ
    data:��������
    key:����key
    res:���Խ��
    n:���Դ���
    :return:
    """
    logging.info(str(alg)+"�㷨"+
                 str(mode)+'-'+
                 'ʹ����Կ'+str(key)+
                 " ��������"+str(data)+ "���ܵõ�����"+str(res)+
                 " ���ܵ�"+str(n)+"������ʱ��" +
                 str(test_time) + "ms")

def func_log_de(test_time,alg,mode,data,key,res,n):
    """
    ���ܽ��д��־
    :param
    test_time: ��������ʱ�� ��t1-t0�õ�
    alg: �㷨����
    mode��ģʽ
    data:��������
    key:����key
    res:���Խ��
    n:���Դ���
    :return:
    """
    logging.info(str(alg)+"�㷨"+
                 str(mode)+'-'+
                 'ʹ����Կ'+str(key)+
                 " ��������,"+str(data)+ "���ܵõ�����"+str(res)+
                 " ���ܵ�"+str(n)+"������ʱ��" +
                 str(test_time) + "ms")

def encrypt(data):
    rc4_demo = ARC4.new(binascii.unhexlify("404142434445464748494A4B4C4D4E4F"))
    data = binascii.unhexlify(data)
    res = rc4_demo.encrypt(data)
    return res.hex()

def decrypt(data):
    rc4_demo = ARC4.new(binascii.unhexlify("404142434445464748494A4B4C4D4E4F"))
    data = binascii.unhexlify(data)
    res = rc4_demo.decrypt(data)
    return res.hex()

for i in range(1000):
    test_data = get_random_16bytes()
    # ���ܺ���
    func1 = encrypt
    func2 = decrypt
    # def ms_time_count(func1, func2, alg, mode, data, key, n):
    ms_time_count(func1,func2 ,alg='rc4',mode='',data=test_data,key='404142434445464748494A4B4C4D4E4F',n=i)


for i in range(5):
    t1 = time.time()
    for j in range(10000):
        data = get_random_16bytes()
        rc4_demo = ARC4.new(binascii.unhexlify("404142434445464748494A4B4C4D4E4F"))
        data = binascii.unhexlify(data)
        rc4_demo.encrypt(data)
    t2 = time.time()
    print(t2-t1)

