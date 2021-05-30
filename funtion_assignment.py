def Artist():
    artist = "Taylor Swift"
    print(artist)
Artist()


def Instruments(instrument):
    Instruments = ['Guitar', 'Banjo',' Piano','Ukulele']
    if instrument in Instruments:
        print(Ýes)
    else:
        print('No')
ifPresent = Instruments('Violin')

def Writers():
    writers = ['Taylor Swift' , ' Ryan Tedder' , ' Max Martin' , ' Ali Payami' , ' Jack Antonoff' , ' Imogen Heap' , ' Shellback']
    writersCount = len(writers)
    print(writersCount)
Writers()
