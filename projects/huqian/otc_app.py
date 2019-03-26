#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# java应用分布
javaapps = {
    "acs": "192.168.2.202,192.168.7.206",
    "bank-btc": "192.168.2.203,192.168.7.207",
    "bank-usdt": "192.168.2.203,192.168.7.207",
    "basis": "192.168.2.201,192.168.7.205",
    "cert": "192.168.2.204,192.168.7.208",
    "cmf": "192.168.2.203,192.168.7.207",
    "cmf-task": "192.168.2.203",
    "counter": "192.168.2.201,192.168.7.205",
    "counter-api": "192.168.2.201,192.168.7.205",
    "dpm-accounting": "192.168.2.203,192.168.7.207",
    "dpm-manager": "192.168.2.204,192.168.7.208",
    "dpm-task": "192.168.2.203",
    "fag": "192.168.2.204,192.168.7.208",
    "fcw": "192.168.2.203,192.168.7.207",
    "fos": "192.168.2.202,192.168.7.206",
    "ma-web": "192.168.2.204,192.168.7.208",
    "mns-admin": "192.168.2.202,192.168.7.206",
    "mns-mq-listener": "192.168.2.202,192.168.7.206",
    "mns-scheduler-web": "192.168.2.202,192.168.7.206",
    "mns-web": "192.168.2.202,192.168.7.206",
    "notifychannel": "192.168.2.203,192.168.7.207",
    "oss-web": "192.168.2.201,192.168.7.205",
    "otc": "192.168.2.204,192.168.7.208",
    "otcg": "192.168.2.204,192.168.7.208",
    "payment": "192.168.2.202,192.168.7.206",
    "payment-carryover": "192.168.2.203,192.168.7.207",
    "payment-task": "192.168.2.203",
    "pbs": "192.168.2.202,192.168.7.206",
    "pbs-bos": "192.168.2.202,192.168.7.206",
    "pfs-basis": "192.168.2.203,192.168.7.207",
    "pfs-manager": "192.168.2.203,192.168.7.207",
    "pfs-payment": "192.168.2.203,192.168.7.207",
    "privilege-admin": "192.168.2.201,192.168.7.205",
    "privilege-api": "192.168.2.201,192.168.7.205",
    "rms-cep": "192.168.2.204,192.168.7.208",
    "rms-intra": "192.168.2.204,192.168.7.208",
    "rms-monitor": "192.168.2.204,192.168.7.208",
    "rms-rules": "192.168.2.204,192.168.7.208",
    "smsgateway-ws": "192.168.2.202,192.168.7.206",
    "tss": "192.168.2.202,192.168.7.206",
    "ues-console": "192.168.2.201,192.168.7.205",
    "ues-ws": "192.168.2.201,192.168.7.204",
    "ufs": "192.168.2.201,192.168.7.205",
    "ufs-admin": "192.168.2.201,192.168.7.205",
    "uni-audit": "192.168.2.201,192.168.7.205",
    "uni-auth": "192.168.2.201,192.168.7.205",
    "uni-login": "192.168.2.201,192.168.7.205",
    "voucher": "192.168.2.202,192.168.7.206"

}


# print(sys.argv[1])
# print(apps[sys.argv[1]])


if __name__ == "__main__":
    print(javaapps[sys.argv[1]])