# from asyncore import file_dispatcher


# find twinkle in the sample file_dispatcher
f = open('sample.txt' , 'r')
a = f.read()
if  'twinkle' in a:
    print("Twinkle is present in the sample")
    
else :
    print("Twinkle is not present in sample ")
f.close()


