#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User, Base


class DB:
    """
    DB class for interacting with the SQLite database
    """

    def __init__(self) -> None:
        """Initialize a new DB instance and set up the engine"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments"""
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user found matching the criteria.")
        except Exception as e:
            raise InvalidRequestError(f"Invalid query: {e}")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user’s attributes in the database"""
        # Locate the user using the provided user_id
        user = self.find_user_by(id=user_id)

        # Validate and update the attributes
        valid_fields = ['email', 'hashed_password', 'session_id', 'reset_token']
        for key, value in kwargs.items():
            if key not in valid_fields:
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        # Commit the changes to the database
        self._session.commit()
