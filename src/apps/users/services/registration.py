from src.apps.users.models.user import User
from src.apps.profiles.models.profile import Profile
from src.apps.countries.models.country import Country
from src.apps.search_options.models.search_options import SearchOptions

from .. import schemas


async def signup_user(form: schemas.SignUpForm) -> schemas.UserPublic:
    user = await User.create(
        first_name=form.first_name,
        last_name=form.last_name
    )

    country = await Country.get(name=form.country.value)
    profile = await Profile.create(
        user=user,
        age=form.age,
        gender=form.gender,
        country=country
    )
    search_options = await SearchOptions.create(user=user)

    return schemas.UserPublic.from_orm(user)
