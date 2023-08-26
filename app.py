from typing import List
import sqlite3
import pandas as pd

N = 1


class Recipe:
    def __init__(self, name: str, cursor, conn, N):
        self.name = name
        crud_string = f"""
            INSERT INTO recipes
            VALUEs
            ({N}, "{name}")
            """
        cursor.execute(crud_string)

        conn.commit()
        N += 1

    def add_ingredients(self, ingredients: List[str], cursor, conn, N):
        self.ingredients = ingredients
        ingredient_string = ["".join(ingredient) for ingredient in ingredients]
        crud_string = f"""
            INSERT INTO ingredients
            VALUES
            ({N}, "{ingredient_string}")
"""
        cursor.execute(crud_string)

        conn.commit()


def main() -> None:
    conn = sqlite3.connect("recipe_book")
    cursor = conn.cursor()
    create_tables(cursor, conn)

    chicken_pie = create_recipe("Chicken Pie", cursor, conn)

    chicken_pie.add_ingredients(["chicken", "pastry", "salt", "pepper"], cursor, conn)

    cursor.execute(
        """
          SELECT
          a.recipe_name,
          b.ingredients
          FROM recipes a
          LEFT JOIN ingredients b ON a.recipe_id = b.recipe_id
          """
    )

    df = pd.DataFrame(cursor.fetchall(), columns=["recipe_name", "ingredients"])
    print(df)


def create_tables(cursor, conn):
    cursor.execute(
        """
                        CREATE TABLE IF NOT EXISTS recipes
                        ([recipe_id] INTEGER PRIMARY KEY, [recipe_name] TEXT)
                        """
    )

    cursor.execute(
        """
                        CREATE TABLE IF NOT EXISTS ingredients
                        ([recipe_id] INTEGER PRIMARY KEY, [ingredients] TEXT)
                        """
    )
    conn.commit()


def create_recipe(name, cursor, conn, N) -> Recipe:
    return Recipe(name, cursor, conn, N)


main()
