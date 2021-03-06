#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import json
import base64

import rsa
import requests


def js_encrypt(text):
    b64der = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg/NOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0/nhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh+bvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB'
    der = base64.standard_b64decode(b64der)

    pk = rsa.PublicKey.load_pkcs1_openssl_der(der)
    v1 = rsa.encrypt(bytes(text, 'utf8'), pk)
    value = base64.encodebytes(v1).replace(b'\n', b'')
    value = value.decode('utf8')

    return value


session = requests.Session()

i1 = session.get('https://passport.cnblogs.com/user/signin')
rep = re.compile("'VerificationToken': '(.*)'")
v = re.search(rep, i1.text)
verification_token = v.group(1)

form_data = {
    'input1': js_encrypt('wptawy'),
    'input2': js_encrypt('asdfasdf'),
    'remember': False
}

i2 = session.post(url='https://passport.cnblogs.com/user/signin',
                  data=json.dumps(form_data),
                  headers={
                      'Content-Type': 'application/json; charset=UTF-8',
                      'X-Requested-With': 'XMLHttpRequest',
                      'VerificationToken': verification_token}
                  )

i3 = session.get(url='https://i.cnblogs.com/EditDiary.aspx')

print(i3.text)