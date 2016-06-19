#Adif to Csv

I wanted to check some data for a ham radio contest I had recently been competing in, and instead of fighting with 
the internal formats of several loggers I decided that the easiest mechanism to do this was to export as ADIF, 
and then to extract from ADIF.

It actually turned out

  - easier
  - quicker
  - better
  
Than I had hoped.

#Class

The basic class is documented - but there is no error checking (hangs head in shame), there is also no
 logging (looking even sadder)
 
 To use the example code - could not be simpler, check out **main.py** 
 

    from adif2csv import adif2csv
    import sys
    if len(sys.argv)!=2:
        print("Error: Expected main.py <ADIF>")
        exit()
    else:
        cvt=adif2csv()
        cvt.process(sys.argv[1])
        for a in cvt.dump():
            print(''+a, end='')
        
        
Any problems/Suggestions please leave a request.