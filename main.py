import asyncio
from python_weather import IMPERIAL, METRIC, Client
from python_weather.forecast import Forecast
from python_weather.forecast import HourlyForecast


def main():
    async def getweather():
        while True:
            units = input("What units do you prefer,please enter number 1 or 2: 1)Celsius or 2)Fahrenheit\n")
            if units == '1':
                unit = METRIC
                break
            elif units == '2':
                unit = IMPERIAL
                break
            else:
                print("Please enter valid number:")


        async with Client(unit=unit) as client:
            city = input("What city's weather do you want to know?\n")
            try:
                weather = await client.get(city)
            except Exception as x:
                print(x)
                return 0

            def menu():
                while True:
                    print("What do you want to know?")
                    print("1) The hourly forecast")
                    print("2) The forecast for 3 days")
                    print("3) One word description for the day")
                    print("4) What it felt like in temperature")
                    print("5) Humidity in percent")
                    print("6) The kind of the forecast")
                    value = int(input())

                    if value in [1,2,3,4,5,6]:
                        pass
                    else:
                        continue

                    print("\n")
                    if value == 1:
                        for daily in weather:
                            for hourly in daily:
                              print(hourly)
                            break
                        break
                    elif value == 2:
                        for daily in weather:
                            print(daily)
                        break

                    elif value == 3:
                        print("Weather description: " + str(weather.description))
                        break
                    elif value == 4:
                        print("Felt like: "+ str(weather.feels_like))
                        break
                    elif value == 5:
                        print("Humidity is: "+str(weather.humidity)+ "%")
                        break
                    elif value == 6:
                        print("The forecast kind: "+ str(weather.kind))
                        break

            menu()


    asyncio.run(getweather())

if __name__ == '__main__':
    main()