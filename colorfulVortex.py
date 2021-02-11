import turtle
from math import sqrt, pi


def hsl2hex(hue,sat,lum):
    ''' converts HSL color code to hex color code '''
    if sat==0:
        RGB=[lum*255,lum*255,lum*255]
        rt,gt,bt=hex(round(RGB[0]))[2:],hex(round(RGB[1]))[2:],hex(round(RGB[2]))[2:]
        if len(rt)==1:
            rt='0'+rt
        if len(gt)==1:
            gt='0'+gt
        if len(bt)==1:
            bt='0'+bt
        retstr='#'+rt+gt+bt
        return retstr
    if lum<0.5:
        tmp1=lum*(1+sat)
    else:
        tmp1=lum+sat-lum*sat
    tmp2=2*lum-tmp1
    hue=hue/360
    tempRGB=[hue+0.333,hue,hue-0.333]
    for ind in range(3):
        if tempRGB[ind]>1:
            tempRGB[ind]-=1
        elif tempRGB[ind]<0:
            tempRGB[ind]+=1
    RGB=[]
    tst1f=lambda x: tmp2+(tmp1-tmp2)*6*x
    tst2f=lambda x: tmp1
    tst3f=lambda x: tmp2+(tmp1-tmp2)*(0.666-x)*6
    for tempC in tempRGB:
        if 6*tempC<1:
            RGB.append(tst1f(tempC))
        elif 2*tempC<1:
            RGB.append(tst2f(tempC))
        elif 3*tempC<2:
            RGB.append(tst3f(tempC))
        else:
            RGB.append(tmp2)
    RGB=[inten*255 for inten in RGB]
    rt,gt,bt=hex(round(RGB[0]))[2:],hex(round(RGB[1]))[2:],hex(round(RGB[2]))[2:]
    if len(rt)==1:
        rt='0'+rt
    if len(gt)==1:
        gt='0'+gt
    if len(bt)==1:
        bt='0'+bt
    retstr='#'+rt+gt+bt
    return retstr


wn = turtle.Screen()
wn.bgcolor("black")

h,s,l=0,0.613,0

mango=turtle.Turtle()
mango.pensize(1)
mango.speed(0)
r=100
density_constant=1#higher the constant, less dense the lines will be
y=int(360/density_constant)
section_of_circum=2*pi*r/y
tang_len=sqrt((1.61803398875*r)**2 - r**2)

mango.up()    
mango.right(90)
mango.forward(r)
mango.left(90)

mango.color(hsl2hex(h,s,l))

for i in range(y):
    if i%2==0:
        mango.down()
        mango.forward(tang_len)
        mango.left(180)
        mango.up()
        mango.forward(tang_len)
        mango.left(180)
        l+=1/360 * density_constant
        h+=2 * density_constant
        mango.color(hsl2hex(h,s,l))
    mango.forward(section_of_circum)
    mango.left(density_constant)
mango.left(90)
mango.forward(r)
mango.right(90)

mango.getscreen().getcanvas().postscript(file="f65.eps")

wn.exitonclick()