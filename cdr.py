import json
import time
import os
answ = open('.\\answer.txt','r', encoding='utf-8')
answ = answ.read()
back_j=''
#a = str(answ).split('}{')
#print(len(a))
#gu = eval('{'+a[1]+'}')
##gu = json.load(str(gu))
#for key,val in  gu.items():
#    print(key+':'+str(val))
while True:
    f = open('c:\\cdr\\responseBody.txt', 'r', encoding='utf-8')
    #ooo = open('c:\\cdr\\responseBody.txt', 'r', encoding='utf-8')
    #print(ooo.read())
    try:
        j = json.load(f)
    except:
        print("????")
        break
    if(back_j==j):
        time.sleep(0.1)
        continue
    else:
        i = os.system('cls')
    back_j = j
    #print(j['data']['task_type'])
    #print(j['data'])
    mmp = True
    opt = []
    if('stem' in j['data']): print('题目：'+j['data']['stem']['content'])
    else: mmp = False
    if 'options' in j['data']:
        print("选项:")
        lenth=len(j['data']['options'])
        for i in range(0,lenth):
            # print(j['data']['options'][i]['answer'])
            opt.append(str(j['data']['options'][i]['content']))
            print(opt[-1])

    # 拼短语
    if(mmp and j['data']['stem']['content'][0] == "_"):
        mmp = False
        print('提示：'+str(j['data']['stem']['remark']))
        x = answ.find(str(j['data']['stem']['remark']+"'"))
        fr = x
        while(answ[fr]!="'"):
            fr-=1
        # nowa = answ[fr+1:x-1].split(" ");
        print("\n\n答案："+answ[fr+1:x])

    # 搭配单词
    if(mmp and j['data']['answer_num']>1):
        mmp = False
        print("\n\n答案：")
        if 'remark' in j['data']['stem']:
            # lenth=len(j['data']['stem']['remark'])
            for rem in j['data']['stem']['remark']:
                remark_ans = str(rem['relation'])
                remark_cn = str(rem['sen_cn'])
                remark_en = str(rem['sen_marked'])
                print(remark_ans+'\t\t\t'+remark_en+'('+remark_cn+')')

    # 给句子选单词
    if(mmp and j['data']['stem']['content'].find('{}')!=-1 and len(j['data']['options'])!=0):
        mmp = False
        print('句子翻译：'+j['data']['stem']['remark'])
        x = answ.find(j['data']['stem']['remark'])
        fr=x
        while(answ[fr]!="{"):
            fr-=1
        too = fr
        while(answ[too]!="}"):
            too+=1
        anss = answ[fr+1:too]
        print("答案："+answ[fr+1:too])
        fr-=1
        while(answ[fr]!="{"):
            fr-=1
        while(answ[x]!="}"):
            x+=1
        answw=eval(answ[fr:x+1])
        print("原句：",str(answw['sen_content']),'(',str(answw['sen_mean_cn']),')')
        print("\n\n明确答案："+anss)
        print("如答案错误，请参考原句")

    # 中文意思填单词
    if(mmp and j['data']['stem']['content'].find('{}')!=-1 and len(j['data']['options'])==0):
        mmp = False
        print('短语翻译：'+j['data']['stem']['remark'])
        x = answ.find(j['data']['stem']['remark'])
        fr=x
        while(answ[fr]!="{"): fr-=1
        too = fr
        while(answ[too]!="}"): too+=1
        anss=answ[fr+1:too]
        print("答案："+answ[fr+1:too])
        fr-=1
        while(answ[fr]!="'"): fr-=1
        while(answ[x]!="'"): x+=1
        print("原短语：",answ[fr+1:x])
        print("\n\n\n明确答案："+anss)

    # 听音选翻译
    if(mmp and j['data']['stem']['ph_en_url']!=None):
        mmp = False
        lis=[]
        print("\n\n候选翻译：")
        x=0
        while 1:
            x = answ.find("'"+j['data']['stem']['content']+"': [",x)
            #print(answ[x-1000:x+19])
            if(x==-1):break
            #print(answ[x:x+1000])
            while(answ[x:x+4]!="': ["):x+=1
            x+=1
            while 1:
                while(answ[x-22:x]!="{'content': {'mean': '" and answ[x:x+26]!="': [{'content': {'mean': '"): x+=1
                if(answ[x:x+26]=="': [{'content': {'mean': '"): break
                too = x
                while(answ[too]!="'"):too+=1
                if(lis.count(answ[x:too]) == 0):
                    lis.append(answ[x:too])
                    print(answ[x:too])
                    #print(answ[x:x+1000])
                x=too+1

    # 划线词含义
    if(mmp):
        mmp = False
        print('句子翻译：'+j['data']['stem']['remark'])
        x = answ.find(j['data']['stem']['content'])
        #print(answ[x-500:x+100])
        while(answ[x-9:x]!="'mean': '"): x-=1
        too=x+1
        while(answ[too:too+2]!="',"):too+=1
        print("\n\n答案："+answ[x:too])


    print("\n\n\n_______________________\n")
    time.sleep(0.1)
    