#Formula Resolvente

print ("Formula resolvente:")
print "ax2+bx+c=0"
print ""
a = int(raw_input("a="))
b = int(raw_input("b="))
c = int(raw_input("c="))

Bino = (b**2)-4*a*c
rBino = ((b**2)-4*a*c)**(1/2)

print"............"
print"Resultado (x):"

if Bino > 0:
   X = (-b-rBino)/2*a
   Y = (-b+rBino)/2*a
   print X , "," , Y 
elif Bino == 0:
   X = (-b)/2*a 
   print X 
else :
   print "Eq. Impossivel"