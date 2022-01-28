total= int(input(&quot;enter the no. of total bananas :&quot;))
distance=int(input(&quot;enter the Distance :&quot;))
load= int(input(&quot;enter the max. amount of banana a camel can carrry :&quot;))
lost=0
start=total
for i in range(distance):
while start&gt;0:
start=start-load
if start==1:
lost=lost-1
lost=lost+2
lost=lost-1
start=total - lost
if start==0:
break
print(start)
