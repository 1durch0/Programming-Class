import sqlite3
from typing import List, Dict, Any

class UserStore:
    """
    A class to handle the persistence of user data in a SQLite database.
    """

    def __init__(self, db_path: str):
        """
        Initializes the UserStore with the path to the SQLite database.

        Args:
            db_path: The path to the .db file.
        """
        self.db_path = db_path
        self.init_db()

    def _get_db_conn(self):
        """Returns a database connection."""
        conn = sqlite3.connect(self.db_path)
        # Return rows as dictionaries
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        """
        Initializes the database and creates the 'users' table if it doesn't exist.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()
        conn.close()

    def load(self) -> List[Dict[str, Any]]:
        """
        Retrieves all users from the database.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return users

    def add_user(self, user_data: Dict[str, Any]) -> Dict[str, Any] | None:
        """
        Adds a new user to the database.

        Args:
            user_data: A dictionary containing the new user's data (name, email).

        Returns:
            The newly created user dictionary, including the new ID, or None on failure.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (user_data['name'], user_data['email'])
            )
            new_id = cursor.lastrowid
            conn.commit()
            return {"id": new_id, **user_data}
        except sqlite3.IntegrityError:  # Handles UNIQUE constraint errors
            return None
        finally:
            conn.close()

    def find_by_id(self, user_id: int) -> Dict[str, Any] | None:
        """
        Finds a user by their ID.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_row = cursor.fetchone()
        conn.close()
        return dict(user_row) if user_row else None
    
    def search_by_name(self, query: str) -> List[Dict[str, Any]]:
        """
        Searches for users by name using a LIKE query.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f'%{query}%',))
        users = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return users

    def update_user(self, user_id: int, updated_data: Dict[str, Any]) -> bool:
        """
        Updates a user's data.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (updated_data['name'], updated_data['email'], user_id)
        )
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user by their ID.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
        
    # The `save` method from the file-based approach is less relevant,
    # but could be adapted for bulk inserts if needed.
    def save(self, users: List[Dict[str, Any]]):
        """
        Inserts or replaces multiple users into the database.
        """
        conn = self._get_db_conn()
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT OR REPLACE INTO users (id, name, email) VALUES (:id, :name, :email)",
            users
        )
        conn.commit()
        conn.close()
