num=int(input("?מהו מחיר קנייתך בקניון\n"))
A=bool(input("True/False ?האם יש במשפחתך תלמיד הלומד בבית ספר אורט אלון\n"))
if num < 400:
    print ("קיבלת חבילה ובה 3 סופגניות")
elif (num>=400) and (num<=800) and (A==True):
    print ("קיבלת 8 סופגניות וכוס קפה בארומה")
elif (num>=400) and (num<=800) and (A==False):
    print ("קיבלת חבילה ובה 5 סופגניות")
elif num>800:
    num=num-800
    y=num%100
    y=y/100
    num=num/100
    num=num-y
    num=num+10
    print ("קיבלת {} סופגניות ו2 כוסות קפה בארומה".format(int(num)))
