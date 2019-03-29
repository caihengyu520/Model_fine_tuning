import os.path,sys
dirname=sys.argv[1]
i=10001
for f in os.listdir(dirname):
    src=os.path.join(dirname,f)
    if os.path.isdir(src):
        print(src)
        continue
    os.rename(src,'out/10001.txt')
    print("修改后:{}".format(src))
    i+=1