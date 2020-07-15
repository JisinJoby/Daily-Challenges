def meeting_point(x1,x2,v1,v2,):
    text=""
    if(x1 >= x2 and v1 > v2) or (x2 >= x1 and v2 > v1) or (x1 != x2 and v1 == v2) :
        text="NO"
    elif (x1 == x2 and v1 == v2) or (abs(x1 - x2) % abs(v1 - v2) == 0) : 
        text="YES"
    return text

x1,v1,x2,v2=map(int,input().split())
print(meeting_point(x1,x2,v1,v2))
