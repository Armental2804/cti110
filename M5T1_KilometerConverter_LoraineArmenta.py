# KM conversion
# 20170704
# CTI-110 M5T1_KilometerConverter 
# Loraine Armenta
#
CONVERSION_FACTOR = 0.6214

def main ():
    kilometers = float (input ('Enter a distance in kilometers: '))
                        
    show_miles (kilometers)
                        
def show_miles (km):
    miles = km * CONVERSION_FACTOR
    print (km, 'kilometers equals', miles, 'miles.')
main ()
