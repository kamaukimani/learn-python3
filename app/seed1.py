

from faker import Faker
import random

from sqlalchemy import create_engine,select
from sqlalchemy.orm import sessionmaker

from models import Game, User

if __name__ == "__main__":
    engine = create_engine("sqlite:///one_to_many.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Game).delete()
    session.query(User).delete()

    session.commit()

    fake = Faker()

    genres = [
        "action",
        "adventure",
        "strategy",
        "puzzle",
        "first-person shooter",
        "racing",
    ]

    platforms = [
        "nintendo 64",
        "gamecube",
        "wii",
        "wii u",
        "switch",
        "playstation",
        "playstation 2",
        "playstation 3",
        "playstation 4",
        "playstation 5",
        "xbox",
        "xbox 360",
        "xbox one",
        "pc",
    ]

    # Create games
    games = []

    for i in range(50):
        game = Game(
            title=fake.unique.name(),
            genre=random.choice(genres),
            platform=random.choice(platforms),
            price=random.randint(5, 60),
        )

        games.append(game)

    session.add_all(games)
    session.flush()

    # Create users
    users = []

    for i in range(25):
        user = User(
            name=fake.unique.name(),
        )

        users.append(user)

    session.add_all(users)
    session.flush()

    # Establish many-to-many relationships
    for user in users:
        number_of_games = random.randint(1, 5)

        selected_games = random.sample(
            games,
            number_of_games,
        )

        user.games.extend(selected_games)

    session.commit()
    session.close()

    games=session.execute(select(game_users).where(game_users.c.user_id == 1))
    print(games)




