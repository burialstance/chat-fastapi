from src.apps.countries.models.country import Country
from src.conf.enums import CountriesEnum


country_icons = {
    CountriesEnum.RUSSIA: 'π·πΊ',
    CountriesEnum.UKRAINE: 'πΊπ¦',
    CountriesEnum.BELARUS: 'π§πΎ',
    CountriesEnum.KAZAKHSTAN: 'π°πΏ',
    CountriesEnum.UZBEKISTAN: 'πΊπΏ',
    CountriesEnum.TAJIKISTAN: 'πΉπ―',
    CountriesEnum.TURKMENISTAN: 'πΉπ²',
    CountriesEnum.AZERBAIJAN: 'π¦πΏ',
    CountriesEnum.ARMENIA: 'π¦π²',
    CountriesEnum.MOLDOVA: 'π²π©'
}


async def populate_countries():
    created = []
    for country in list(CountriesEnum):
        if not await Country.exists(name=country.value):
            country_icon = country_icons.get(country, None)
            new_country = await Country.create(
                name=country.value, icon=country_icon
            )
            created.append(new_country)

    if created:
        print('created countries', [i.name for i in created])
    return created
