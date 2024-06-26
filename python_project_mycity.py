from cs1graphics import*
from time import sleep
can=Canvas(1400,800)
can.setBackgroundColor("black")
def re(a,b,c,d,e,f):
    r=Rectangle(a,b,Point(c,d))
    f.add(r)
    r.setFillColor(e)
def tri(f,g,h,i,j,k,l,m):
    t=Polygon(Point(f,g),Point(h,i),Point(j,k))
    m.add(t)
    t.setFillColor(l)
def pa(a,b,c,d,e,f,g):
    p=Path(Point(a,b),Point(c,d))
    p.setBorderColor(e)
    p .setBorderWidth(f)
    g.add(p)
def ci(x,y,z,w,u,v):
    c=Circle(x,Point(y,z))
    c.setFillColor(w)
    c.setBorderColor(v)
    u.add(c)
def p(x,y,z,a,b,c,d,e,f,g,h,i,j,k,m,n):
    po=Polygon(Point(x,y),Point(z,a),Point(b,c),Point(d,e),Point(h,i),Point(j,k),Point(m,n))
    f.add(po)
    po.setFillColor(g)
def pol(x,y,z,a,b,c,d,e,f,g):
    po=Polygon(Point(x,y),Point(z,a),Point(b,c),Point(d,e))
    f.add(po)
    po.setFillColor(g)    
road=Layer()    
re(1400,210,700,600,"black",road)
re(100,10,60,565,"white",road)
re(100,10,60,635,"white",road)
re(100,10,210,565,"white",road)
re(100,10,210,635,"white",road)
re(100,10,460,565,"white",road)
re(100,10,460,635,"white",road)
re(100,10,610,565,"white",road)
re(100,10,610,635,"white",road)
re(100,10,860,565,"white",road)
re(100,10,860,635,"white",road)
re(100,10,1010,565,"white",road)
re(100,10,1010,635,"white",road)
re(100,10,1260,565,"white",road)
re(100,10,1260,635,"white",road)
re(1400,100,700,750,"green",can)
re(1400,150,700,425,"green",can)
can.add(road)
car=Layer()
p(100,550,200,550,200,500,220,500,car,"blue",250,530,250,580,100,580)
ci(15,118,580,"white",car,"white")
ci(15,232,580,"white",car,"white")
ra=Rectangle(100,60,Point(150,520))
ra.setFillColor("red")
ra.adjustReference(-150,300)
car.add(ra)
can.add(car)
bird=Layer()
bi=ClosedSpline(Point(1210,100),Point(1185,93),Point(1175,100),Point(1185,107))
bird.add(bi)
bi.setFillColor("white")
tri(1177,97,1177,102,1170,102,"white",bird)
tri(1197,100,1207,96,1207,104,"white",bird)
wi=Spline(Point(1178,102),Point(1195,100),Point(1200,103))
bird.add(wi)
pa(1185,105,1185,111,"black",2,bird)
pa(1190,105,1190,111,"black",2,bird)
can.add(bird)
car3=Layer()
caa=Polygon(Point(0,380),Point(-50,380),Point(-80,350),Point(-180,350),Point(-200,380),Point(-230,380),Point(-230,420),Point(0,420))
caa.setFillColor("purple")
car3.add(caa)
ci(15,-40,420,"black",car3,"white")
ci(15,-200,420,"black",car3,"white")
rec2=Rectangle(30,4,Point(-40,420))
rec2.setFillColor("white")
car3.add(rec2)
rec3=Rectangle(30,4,Point(-200,420))
rec3.setFillColor("white")
car3.add(rec3)
can.add(car3)
car3.moveTo(0,170)
pol(425,420,460,380,460,80,425,120,can,"brown")
pol(425,270,575,270,610,230,460,230,can,"brown")
re(150,300,350,270,"brown",can)
re(50,50,310,150,"yellow",can)
re(50,50,390,150,"yellow",can)
re(50,50,310,230,"yellow",can)
re(50,50,390,230,"yellow",can)
re(50,50,310,310,"yellow",can)
re(50,50,390,310,"yellow",can)
re(60,70,390,380,"gray",can)
re(60,70,310,380,"gray",can)
re(55,20,390,360,"yellow",can)
re(55,20,310,360,"yellow",can)
re(150,150,500,345,"brown",can)
re(150,300,650,270,"brown",can)
re(50,50,610,150,"yellow",can)
re(50,50,690,150,"yellow",can)
re(50,50,610,230,"yellow",can)
re(50,50,690,230,"yellow",can)
re(50,50,610,310,"yellow",can)
re(50,50,690,310,"yellow",can)
re(60,70,690,380,"gray",can)
re(60,70,610,380,"gray",can)
re(55,20,690,360,"yellow",can)
re(55,20,610,360,"yellow",can)
re(50,50,460,310,"yellow",can)
re(50,50,540,310,"yellow",can)
re(60,70,460,380,"gray",can)
re(60,70,540,380,"gray",can)
re(55,20,540,360,"yellow",can)
re(55,20,460,360,"yellow",can)
pol(275,120,425,120,460,80,310,80,can,"brown")
pol(575,120,725,120,760,80,610,80,can,"brown")
re(150,150,1000,345,"red",can)
pol(925,270,965,240,1115,240,1075,270,can,"red")
pol(1075,420,1115,380,1115,240,1075,270,can,"red")
re(60,120,960,350,"yellow",can)
re(60,60,1030,320,"yellow",can)
pol(725,420,760,380,760,80,725,120,can,"brown")
re(10,200,150,625,"gray",can)
ci(30,800,495,"white",can,"white")
ci(30,150,495,"white",can,"white")
re(10,200,800,625,"gray",can)
man=Layer()
ci(10,150,400,"black",man,"white")
pa1=Path(Point(150,435),Point(135,450))
man.add(pa1)
pa1.setBorderWidth(3)
pa1.setBorderColor("black")
pa2=Path(Point(150,435),Point(165,450))
man.add(pa2)
pa2.setBorderWidth(3)
pa2.setBorderColor("black")
pa(150,405,150,435,"black",3,man)
pa(150,415,165,430,"black",3,man)
pa(150,415,135,430,"black",3,man)
can.add(man)
man.moveTo(55,0)
tree1=Layer()
tri(200,505,300,505,250,405,"darkgreen",tree1)
tri(210,455,290,455,250,355,"darkgreen",tree1)
tri(220,405,280,405,250,305,"darkgreen",tree1)
re(40,30,250,520,"brown",tree1)
can.add(tree1)
tree1.moveTo(200,200)
tree2=Layer()
tri(700,505,800,505,750,405,"darkgreen",tree2)
tri(710,455,790,455,750,355,"darkgreen",tree2)
tri(720,405,780,405,750,305,"darkgreen",tree2)
re(40,30,750,520,"brown",tree2)
can.add(tree2)
tree2.moveTo(300,200)
tree3=Layer()
tri(200,505,300,505,250,405,"darkgreen",tree3)
tri(210,455,290,455,250,355,"darkgreen",tree3)
tri(220,405,280,405,250,305,"darkgreen",tree3)
re(40,30,250,520,"brown",tree3)
can.add(tree3)
tree3.scale(0.75)
tree3.moveTo(30,70)
tree4=Layer()
tri(700,505,800,505,750,405,"darkgreen",tree4)
tri(710,455,790,455,750,355,"darkgreen",tree4)
tri(720,405,780,405,750,305,"darkgreen",tree4)
re(40,30,750,520,"brown",tree4)
can.add(tree4)
tree4.scale(0.75)
tree4.moveTo(80,70)
ci(30,1300,100,"white",can,"white")  
for i in range(450):    
    car.move(3,0)
    car3.move(6,0)
    rec2.rotate(30)
    rec3.rotate(30)
for i in range(750):
    man.move(1,0)
    bird.move(-1,0)
