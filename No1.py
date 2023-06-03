''' w.f.e to print the ways of labour as per the following cod'n 
       0> and <=4 = 30
       4> and <=6 = 40
       6> and <=8 50
       8>  80
 '''
 # Required working hour so that i am taking a variable for this 
h = int(input('Please Enter The Working Hour: \n')) # i am use int becuse of its confrom that the working hour must be number so that i am directly take int.
if h>0 and h<=4: # first cond'n for check
    w=h*30 # as per cond'n i am taking this 
elif h>4 and h<=6: # as per 2nd cond'n
    w=30*4+(h-4)*40 # 1st i am calculating for 4 hour aftter that i am apply the 2nd cond'n
elif h>6 and h<=8: # as per 3rd cond'n
    w=30*4+40*2+(h-6)*50
else: # this is the last part so i am calculating directly for else part we only give statement 
    w=30*4+40*2+50*2+(h-8)*80
print(f'the wags of the labour as per given working hour of {h} is :{w} ')
# End Of Code....................
# now start to execute the code..........lets check if any mistake done please message tag me i am improve my self. and use your information on my next video thank you.