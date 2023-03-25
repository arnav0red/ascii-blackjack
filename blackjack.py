#blackjack
import random
from os import system
n=s=c1="0" #n-number, s-symbl,c1-card

def card(n,s):
    
    if n==1:
        n="A"
        c1="""           _________
           |"""+n+s+"""       |
           |         |
           |         |
           |    """+s+"""    |
           |         |
           |         |
           |_________|"""
    elif n==2:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |    """+s+"""    |
           |         |
           |    """+s+"""    |
           |         |
           |_________|"""
    elif n==3:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |    """+s+"""    |
           |    """+s+"""    |
           |    """+s+"""    |
           |         |
           |_________|"""
    elif n==4:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           |         |
           |  """+s+"""  """+s+"""   |
           |         |
           |_________|"""
    elif n==5:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           |   """+s+"""     |
           |  """+s+"""  """+s+"""   |
           |         |
           |_________|"""
    elif n==6:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |         |
           |_________|"""
    elif n==7:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           | """+s+"""  """+s+""" """+s+"""  |
           |  """+s+"""  """+s+"""   |
           |         |
           |_________|"""
    elif n==8:
       c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |_________|""" 
    elif n==9:
        c1="""           _________
           |"""+str(n)+s+"""       |
           |         |
           |  """+s+"""  """+s+"""   |
           | """+s+"""  """+s+""" """+s+"""  |
           |  """+s+"""  """+s+"""   |
           |  """+s+"""  """+s+"""   |
           |_________|"""
    elif n==10:
        c1="""           _________
           |"""+str(n)+s+"""      |
           |         |
           |  """+s+"""  """+s+"""   |
           | """+s+"""  """+s+""" """+s+"""  |
           | """+s+"""  """+s+""" """+s+"""  |
           |  """+s+"""  """+s+"""   |
           |_________|"""
    elif n==11:
      n="J"
      c1="""           _________
           |"""+str(n)+s+"""       |
           |  ______ |
           |     |   |
           |     |   |
           |     |   |
           |  \__/   |
           |_________|"""
    elif n==12:
      n="Q"
      c1="""           _________
           |"""+str(n)+s+"""       |
           |   ____  |
           |  /    \ |
           | |      ||
           | |      ||
           |  \___\/ |
           |_______\_|"""
    elif n==13:
      n="K"
      c1="""           _________
           |"""+str(n)+s+"""       |
           | |  /    |
           | | /     |
           | |       |
           | | \     |
           | |  \    |
           |_________|"""

    elif n==0:
       c1="""           _________
           |XXXXXXXXX|
           |XXXXXXXXX|
           |XXXXXXXXX|
           |XXXXXXXXX|
           |XXXXXXXXX|
           |XXXXXXXXX|
           |_________|"""
    
    else:
      print("Incorrect character entered")
      c1=""
    return c1
def sbl(a):
    if a=="h":
        a="♥"
    elif a=="d":
        a="♦"
    elif a=="c":
        a="♣"
    elif a=="s":
        a="♠"
    return a
def cdcrt():
    global ds,ps,dlist,plist,cval,pcntr,dcntr
    n="x"
    s="x"
    while((str(n)+s) in cval):
        n=random.randint(1,13)
        s=random.choice(["♥","♦","♣","♠"])

    #n=int(input("n"))
    ds2=ps2=""
    
    s=sbl(s)
    c1=card(n,s)
    if plr=="d":
        if n>10:
            ds+=10
        elif n<=10:
            ds+=n
        if n==1:
            #ds2=str(n)+" or "+str(n+10)
            dcntr+=1
        dlist+=(c1+"\n")
    elif plr=="p":
        if n>10:
            ps+=10
        elif n<=10:
            ps+=n
        if n==1:
            #ps2=str(ps)+" or "+str(ps+10)
            pcntr+=1
        plist+=(c1+"\n")
    cval.append((str(n)+str(s)))
    #print("cval=",len(cval))
    if len(cval)>=53:
        print("Cards empty\nReshuffling now")
        cval=["xx"]
    return c1
        
def output(n,a,sn):
    q=0
    if a>=1:
        if (n+10)<=21:
            q=(n+10)

    if sn=="s":
        if type(q)==int and q!=0:
            q=" or "+str(q)
        else:
            q=""
    
    return q
            
global cval
cval=["xx"]

q="y"
wins=0
loses=0
money=1500
while q=="y":
    global ds,ps,dlist,plist,pcntr,dcntr
    ds2=ps2=""
    ds=ps=0
    bet=1.8E308
    dcntr=pcntr=0
    print("                                             ###   #       #      ###   #  #  #####    #      ###  #  #             ",sep="")
    print("                                             #  #  #      # #    #      # #     #     # #    #     # #               ",sep="")
    print("                                             ###   #     #####  #       ##      #    #####  #      ##                 ",sep="")
    print("                                             #  #  #     #   #   #      # #   # #    #   #   #     # #                ",sep="")
    print("                                             ###   ####  #   #    ###   #  #   #     #   #    ###  #  #               ",sep="")
    print("WINS:",wins,sep="")
    print("LOSES:",loses,sep="")
    print("MONEY:",money,"$",sep="")    
    if money==0:
        print("YOU LOSE")
        asdasd=input("Press enter to close the program")
        break

    bet=""
    bet=(input("Enter betting amount:"))
    while not(bet.isdigit()) or float(bet)>money or float(bet)<=0:
        print("Invalid amount entered, please re-enter")
        bet=(input("Enter betting amount:"))
        print("\n")
    bet=float(bet)
    
    dlist="Dealer's cards:\n"
    plist="Player's cards:\n"
    plr="d"
    
    print("Dealer\n",cdcrt(),"\n",card(0,"s"),"\nDealer score: ",ds,output(ds,dcntr,"s"),"+",sep="")
    hidden=cdcrt()
    
    plr="p"
    #print("PA",pcntr)
    print("Player\n",cdcrt(),"\n",cdcrt(),"\nPlayer Score:",ps,output(ps,pcntr,"s"))
    
    action=input("Hit,Pass?(h,*):")
    while (action.lower=="h") and (ps<=21):
        print("Player\n",cdcrt(),"\nPlayer Score:",ps,output(ps,pcntr,"s"))
        if ps<=21:
            action=input("Hit,Pass?(h,*):")

    print("________________________________________________________________________________________________\n")
    if (ds<17) and (ps<21) and (output(ds,dcntr,"i")<17):
        print("Dealer score:",ds,output(ds,dcntr,"s"),"\n",hidden)
        eg=input("Since Dealer has less than 17 point he'll draw more cards \nPress enter to continue")

    while(ds<17)and(ps<21)and (output(ds,dcntr,"i")<17):
        plr="d"
        cdcrt()
    qwe=""
    if max(ps,output(ps,pcntr,"i"))==21:
        qwe="BLACKJACK"
    
    print("\n",plist,"Player Score:",max(ps,output(ps,pcntr,"i")),"\n",qwe,"\n",dlist,"Dealer score:",max(ds,output(ds,dcntr,"i")))

    
    if output(ps,pcntr,"i")>ps:
        ps=output(ps,pcntr,"i")
    
    if output(ds,dcntr,"i")>ds:
        ds=output(ds,dcntr,"i")
    #   print("ps",ps)
    if (ps<=21):
        if (ds>21):
            print("Dealer busts")
            print("You win")
            wins+=1
            money+=bet
        elif (ps>ds):
            print("You have a more points than Dealer")
            print("You win")
            money+=bet
            wins+=1
        elif ds>ps:
            print("Dealer has higher score")
            print("You lose")
            loses+=1
            money-=bet
        
    elif ps>21:
        print("You bust")
        print("You lose")
        loses+=1
        money-=bet
    if ps==ds:
        print("Tie")
    if ps>ds and qwe=="BLACKJACK":
        print("BLACKJACK")
        money+=(bet*0.5)
        
        
    
    q=input("Continue?(y,n):")
    while(q!="y" and q!="n"):
        print("Invalid input")
        q=input("Continue?(y,n):")


    system('cls')
