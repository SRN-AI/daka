import json
import sys



info={}

if __name__ == '__main__':
    with open(sys.argv[1],'r',encoding='utf-8') as f:
        info=json.load(f)
    info['token']=sys.argv[2]
    info['session']=sys.argv[3]
    with open(sys.argv[1], 'w', encoding='utf-8') as f1:
        f1.write(json.dumps(info, indent=4, ensure_ascii=False))
        print("更新后为：")
        print(info)
