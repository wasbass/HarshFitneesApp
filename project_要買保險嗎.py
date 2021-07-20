import tkinter as tk
import csv
import sys

key_root=False     #是否完成使用者資料建立

#匯入食物熱量
f_list=[[],[]]
s_list = [[],[],[]]

food_file="Food.csv"

print("食物熱量對照表")
with open(food_file , "r") as file:
    rows = csv.reader(file)
    for row in rows:
        f_list[0].append(row[0])
        f_list[1].append(int(row[1]))
        print("%-5s%s"%(row[1],row[0]))

#匯入運動消耗量
sport_file="Sports.csv"
print("運動代號對照表")

with open(sport_file , "r") as file:
    rows = csv.reader(file)
    for row in rows:
        s_list[0].append(row[0])
        s_list[1].append(row[1])
        s_list[2].append(float(row[2]))
        #逐行印出
        print(row[1],row[2],"大卡/分鐘 每公斤")

#建立代號與消耗熱量的字典
s_dict=dict(zip(s_list[0],s_list[2]))

#建立使用者資料視窗
basic=tk.Tk()
basic.title("建立個人資料")

basic.minsize(width=500,height=300)
basic.config(background="skyblue")

#建立標籤
def inittext(text,bg = "skyblue" , fg = "black" , font ="新細明體 10"):
    basic_text = tk.Label(text = text)
    basic_text.config(bg = bg , font = font , fg = fg)
    basic_text.pack()

inittext(text = "計算你的基礎代謝率",bg = "violet" , font = "微軟正黑體 20")
inittext(text = "性別？(1男 0女)")
en_gender=tk.Entry()
en_gender.pack()
inittext(text = "年齡？(請輸入整數)")
en_age  =tk.Entry()
en_age.pack()
inittext(text = "身高(cm)？")
en_height=tk.Entry()
en_height.pack()
inittext(text="體重(kg)？")
en_weight=tk.Entry()
en_weight.pack()
inittext(text="目標體重(kg)？")
en_tg_weight=tk.Entry()
en_tg_weight.pack()

label_check=tk.Label(text="")
label_check.config(bg="skyblue",fg="red",)
label_check.pack()

#建立確認函數
def basic_check():
    try:
        global g , tg_weight , basic_energe , weight
        g=int(en_gender.get())
        a=int(en_age.get())
        h=float(en_height.get())
        w=float(en_weight.get())
        t=float(en_tg_weight.get())
        #計算基本代謝率(公式)
        if g==1:
            basic_energe=(13.7*w+5*h-6.8*a+66)*1.2
        elif g==0:
            basic_energe=(9.6*w+1.8*h-4.7*a+655)*1.2
    #要是輸入格式不正確，就不能進到主要app視窗
    except:
        label_check.config(text="輸入資料都做不好還想減肥啊？再給你一次機會")
    #格式正確之後再檢查數值是否在合理範圍
    else:
        if en_gender.get() not in ["0","1"]:
            label_check.config(text="你是不知道自己的性別嗎")
        elif a>=70:
            label_check.config(text="都幾歲了還要減肥 叫你孫子來好嗎？")
        elif a<15:
            label_check.config(text="小朋友？ 多吃一點趕快長高好嗎")
        elif h<120:
            label_check.config(text="你怎麼矮成這樣？ 小學生多吃一點好嗎")
        elif h>250 or w<30 :
            label_check.config(text="你是外星人嗎？　我們app只適用於地球人喔")
        elif t>=w:
            label_check.config(text="目標體重比較高是要怎麼減肥 低能兒？")
        elif t<30:
            label_check.config(text="變那麼瘦是想慢性自殺嗎")
        else:
            basic.destroy()
            global key_root
            key_root=True
            weight=w
            tg_weight = t

#創造OK鍵來使用確認函數並計算基本代謝率
Ok_basic=tk.Button(text="Ok",command=basic_check)
Ok_basic.pack()
basic.mainloop()

#計算出基本代謝率後就打開主要app視窗
if not key_root:
    sys.exit("Bye coward.")
root=tk.Tk()
root.title("毒舌減肥app")

#視窗外觀調整
root.minsize(width=500,height=600)
root.config(background="skyblue")
root.attributes("-alpha",0.9) #0為完全透明,1為不透明

#全域變數
i=1                 #第幾天減肥
ing=False           #是否有其他功能在使用
cal=0               #熱量初始值
cal_over=False      #是否超量
add=0               #攝取熱量
dec=0               #減少熱量

#預留區塊
label_sec1=tk.Label(bg="violet",font="微軟正黑體 15")
label_sec2=tk.Label(bg="violet")
label_sec3=tk.Label(bg="violet")
en_sec1=tk.Entry()
en_sec2=tk.Entry()
en_sec3=tk.Entry()
Ok_sec1=tk.Button()
Ok_sec2=tk.Button()
Can_sec1=tk.Button()
label_result=tk.Label(bg="skyblue",fg="red",font="微軟正黑體 15")
#label_result.config(bg="skyblue",fg="red",font="微軟正黑體 15")
eat_list = [label_sec1,en_sec1,label_result,Ok_sec1,Can_sec1,label_result]
sport_list = [label_sec1,en_sec1,Ok_sec1,label_sec2,en_sec2,label_sec3,en_sec3,Ok_sec2,Can_sec1,label_result]

#設置環境的函數
def rootlabel(l , bg = "skyblue" , font = "微軟正黑體 15" ):
    l.config(bg = bg ,font = font)
    l.pack()

def updateword(nextday = False):
    global label_day,label_basic,label_main1,label_main3,label_main4,i
    if nextday:
        i += 1
    label_day.config(text="減肥第"+str(i)+"天")
    label_basic.config(text="一天的基礎代謝率為"+str(round(basic_energe,3))+"大卡")
    label_main1.config(text="現在"+str(round(weight,3))+"公斤")
    label_main3.config(text="今日還能攝取的熱量為"+str(round(basic_energe-cal,3))+"大卡")
    label_main4.config(text="今日已攝取熱量為"+str(add)+"大卡")

def feettext(newword = "請選擇功能"):
    global label_feat
    label_feat.config(text = newword)

def resultout(text):
    global label_result
    label_result.config(text = text)

#顯示現在體重，目標體重和今日剩餘攝取熱量等項目
label_day=tk.Label(text="減肥第"+str(i)+"天")
rootlabel(label_day , bg="violet", font="微軟正黑體 24")

label_basic=tk.Label()
label_main1=tk.Label()
label_main2=tk.Label(text="目標"+str(tg_weight)+"公斤")
label_main3=tk.Label()
label_main4=tk.Label()
label_feat =tk.Label(text="請選擇功能")
updateword()

for l in [label_basic,label_main1,label_main2,label_main3,label_main4,label_feat]:
    rootlabel(l)

def othering():
    global ing
    return ing

def FunctionOn(Func=True):
    global ing
    ing = Func

def dayclean():
    global cal,add,dec,cal_over
    cal=0
    add=0
    dec=0
    cal_over=False

def rootbutton(Button,func):
    Button.config(width = 8 , height = 2 ,command = func)
    Button.pack()

def Cancel(Func):
    global label_sec1,en_sec1,Ok_sec1,label_sec2,en_sec2,label_sec3,en_sec3,Ok_sec2,Can_sec1,label_result
    if Func == "Eat":
        for d in [label_sec1,en_sec1,label_result,Ok_sec1,Can_sec1]:
            d.pack_forget()
    else:
        for d in [label_sec1,en_sec1,Ok_sec1,label_sec2,en_sec2,label_sec3,en_sec3,Ok_sec2,Can_sec1,label_result]:
            d.pack_forget()
    FunctionOn(False)
    feettext()

def Funcview(Func):
    global label_sec1,label_sec2,label_sec3,en_sec1,en_sec2,en_sec3,Ok_sec1,Ok_sec2,Can_sec1,label_result
    if Func == "Eat":
        label_sec1.config(text="吃了幾大卡啊")
        Ok_sec1.configure(text="OK")
        Can_sec1.configure(text="Cancel", command= lambda : Cancel("Eat"))
        for new in eat_list:
            new.pack()

    else:
        label_sec1.config(text="請輸入消耗熱量")
        label_sec2.config(text="或選擇輸入運動項目")
        label_sec3.config(text="時間(分鐘數)")
        Ok_sec1.config(text="OK")
        Ok_sec2.config(text="OK")
        Can_sec1.configure(text="Cancel" , command= lambda : Cancel("Sports"))
        for new in sport_list:
            new.pack()

def isoverfat():
    global cal_over,basic_energe,cal
    cal_over=False
    if basic_energe<cal:
        cal_over=True

#函數設置
def eat():
    #先確認沒有其他運行中的功能
    if othering():
        return
    #再確認是否熱量超標
    if cal_over:
        feettext("還敢吃啊？熱量都爆表了")
        return
    #熱量沒超標才能吃
    global en_sec1,Ok_sec1,Can_sec1
    FunctionOn()
    feettext("Eat")
    def Ok():
        #檢測是否為數字
        try:
            float(en_sec1.get())
        except:
            resultout("請輸入數字")
        else:
            eaten=float(en_sec1.get())
            #不是正數就要求重新輸入
            if eaten<0:
                resultout("請輸入正數")
            else:
                global cal,add
                cal+=eaten
                add+=eaten
                updateword()
                isoverfat()
                Cancel("Eat")
    Ok_sec1.configure(command=Ok)
    Funcview("Eat")

def sports():
    global en_sec1,en_sec2,en_sec3,Ok_sec1,Ok_sec2,Can_sec1
    if othering():
        return
    FunctionOn()
    feettext("Sports")
    def Ok1():
        try:
            float(en_sec1.get())
        except:
            resultout("請輸入數字")
        else:
            cos=float(en_sec1.get())
            if cos<0:
                resultout("請輸入正數")
            else:
                global cal,dec,cal_over
                cal-=cos
                dec+=cos
                isoverfat()
                updateword()
                Cancel("Sports")
    def Ok2():
        try:
            sel=s_dict[en_sec2.get()]
            time=float(en_sec3.get())
        except:
            resultout("輸入錯誤")
        else:
            if time<0:
                resultout("請輸入正數")
                return
            global cal,dec,cal_over
            cal-=sel*time*weight
            dec+=sel*time*weight
            isoverfat()
            updateword()
            Cancel("Sport")
    Ok_sec1.config(command=Ok1)
    Ok_sec2.config(command=Ok2)
    Funcview("Sports")

#清除今天的卡路里
def cleanup():
    if othering():
        return
    dayclean()
    updateword()
    feettext()
#把今天的卡路里記錄下來，並往後推一天
def output():
    if othering():
        return
    global cal_over
    if cal_over:
        feettext("給我先去運動")
        return

    #把每一天的體重存到文件檔裡頭
    global cal,add,dec,i,weight,g,basic_energe
    if g==1:
        basic_energe-=1.2*13.7*weight
        weight-=((basic_energe+dec-add)/7700)
        basic_energe+=1.2*13.7*weight
    else:
        basic_energe-=1.2*9.6*weight
        weight-=((basic_energe+dec-add)/7700)
        basic_energe+=1.2*9.6*weight

    #確認是否達標
    if weight<=tg_weight:
        feettext("目標達成！別這樣就沾沾自喜，請繼續保持！")
    else:
        feettext("減肥是長久的事，不要放棄")
    with open("要買保險嗎.txt","a+") as f:
        f.write("第"+str(i)+"天攝取量為"+str(round(add,3))+"大卡 消耗量為"+str(round(dec,3))+"大卡 今日體重為"+str(round(weight,3))+" \n")
    dayclean()
    updateword(nextday=True)

#跳出功能，除非達到減重計畫否則不給跳出
def quit():
    if othering():
        return
    if weight>tg_weight:
        feettext("別想逃避啊 肥豬")
    else:
        root.destroy()

#建立功能按鈕
E=tk.Button(text="Eat")
rootbutton(E,eat)
S=tk.Button(text="Sports")
rootbutton(S,sports)
C=tk.Button(text="Cleanup")
rootbutton(C,cleanup)
O=tk.Button(text="Output")
rootbutton(O,output)
Q=tk.Button(text="Quit")
rootbutton(Q,quit)

#常駐視窗
root.mainloop()