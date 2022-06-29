import urllib.request
import urllib.parse
import json

# 名片appId 与 appSecret
default_app_id = 'wx792adc9471d4d159'
default_app_secret = 'daa8ef22d6a6c6851f50162b42aa6537'


# 获取TOKEN
def get_token(app_id, app_secret):
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}'.format(
        appid=app_id, appsecret=app_secret)
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    read_data = response.read()
    read_data = read_data.decode('utf-8')
    obj = json.loads(read_data)
    print(obj['access_token'])
    return obj['access_token']


# 获取小程序码
# group_path: "pages/group/groupdetail/groupdetail"
# query: "?scene=1,2"
def get_code_image(token, file, path, value):
    url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token={token}'.format(token=token)
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    values = {path: value}
    data = json.dumps(values)
    data = bytes(data, 'utf8')
    request = urllib.request.Request(url, data, headers)
    read_data = urllib.request.urlopen(request).read()
    f = open(file, "wb")
    f.write(read_data)
    f.close()


# get_code_image(get_token(appid, appsecret), 'wxCode.jpg')

def main(argv):
    path = ''  # page_path
    value = ''  # value
    out_put_file = ''
    try:
        opts, args = getopt.getopt(argv, "hp:v:o:", ["path=", "value=", "out="])
    except getopt.GetoptError:
        print('generate_wx_code.py -p <page_path> -v <query> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('generate_wx_code.py -p <page_path> -v <query> -o <output_file>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-v", "--value"):
            value = arg
        elif opt in ("-o", "--out"):
            out_put_file = arg
    path = path if path else "pages/group/groupdetail/groupdetail"
    value = value if value else "?scene=1,2"
    out_put_file = out_put_file if out_put_file else 'wx_code.jpg'
    get_code_image(get_token(appid, appsecret), out_put_file, path, value)


if __name__ == "__main__":
    main(sys.argv[1:])
