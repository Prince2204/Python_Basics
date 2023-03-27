#Convert degree celsius to degree fahrenheit

#function to convert celsius to Fahrenheit
def convertToFahrenheit(tempInCelsius):
    return round(1.8*tempInCelsius+32,1)

celciusTemp=int(input("Enter integer value for tempreture in Celcius: "))

print("The Fahrenheit equivalent of " + str(celciusTemp) +" degrees Celsius is "+ str(convertToFahrenheit(celciusTemp)))






