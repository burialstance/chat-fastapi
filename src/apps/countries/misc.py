from src.apps.countries.models.country import Country
from src.conf.enums import CountriesEnum


country_icons = {
    CountriesEnum.RUSSIA: '🇷🇺',
    CountriesEnum.UKRAINE: '🇺🇦',
    CountriesEnum.BELARUS: '🇧🇾',
    CountriesEnum.KAZAKHSTAN: '🇰🇿',
    CountriesEnum.UZBEKISTAN: '🇺🇿',
    CountriesEnum.TAJIKISTAN: '🇹🇯',
    CountriesEnum.TURKMENISTAN: '🇹🇲',
    CountriesEnum.AZERBAIJAN: '🇦🇿',
    CountriesEnum.ARMENIA: '🇦🇲',
    CountriesEnum.MOLDOVA: '🇲🇩'
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
