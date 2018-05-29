# convert £ to euros
EuroRate=0.88
def convertToEuro(pounds):
    euros = pounds*EuroRate
    return euros

pounds=float(input("pounds?"))
euros=convertToEuro(pounds)
print(euros,"Euros")










