import asyncio
from python_weather import IMPERIAL, METRIC, Client

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

            print("\nThe forecast for 3 days:")
            for daily in weather:
                print(daily)

            print("\nThe forecast for today from 0 to 21 o'clock:")
            for hourly in daily:
                print(f' --> {hourly!r}')

    asyncio.run(getweather())
if __name__ == '__main__':
    main()