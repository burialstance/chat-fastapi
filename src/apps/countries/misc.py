from src.apps.countries.models.country import Country

available_countries = {
    'Россия': '🇷🇺',
    'Украина': '🇺🇦',
    'Беларусь': '🇧🇾',
    'Казахстан': '🇰🇿',
    'Узбекистан': '🇺🇿',
    'Таджикистан': '🇹🇯',
    'Туркменистан': '🇹🇲',
    'Азербайджан': '🇦🇿',
    'Армения': '🇦🇲',
    'Молдова': '🇲🇩'
}


async def populate_countries():
    created = []
    for name, icon in available_countries.items():
        if not await Country.exists(name=name):
            country = await Country.create(name=name, icon=icon)
            created.append(country)
    return created
