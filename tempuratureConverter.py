class Converter:
    def __init__(self, temp) -> None:
        self.temp = temp
    
    def celcius_to_fahrenheit(self):
        return (self.temp * 9 / 5) + 32
    
    def celcius_to_kelvin(self):
        return self.temp + 273.15
    
    def fahrenheit_to_celcius(self):
        return (self.temp - 32) * 5 / 9
    
    def fahrenheit_to_kelvin(self):
        return (self.temp + 459.67) * 5 / 9
    
    def kelvin_to_celcius(self):
        return self.temp - 273.15
    
    def kelvin_to_fahrenheit(self):
        return (self.temp - 273.15) * 9 / 5
    


while True:
    try:
        temperature = int(input("Enter temperature: "))
        converter = Converter(temperature)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue
    else:
        break

print(f"Fahrenheit: {converter.celcius_to_fahrenheit()}")
print(f"Kelvin: {converter.celcius_to_kelvin()}")
print(f"Celcius: {converter.fahrenheit_to_celcius()}")
print(f"Kelvin: {converter.fahrenheit_to_kelvin()}")
print(f"Celcius: {converter.kelvin_to_celcius()}")
print(f"Fahrenheit: {converter.kelvin_to_fahrenheit()}")