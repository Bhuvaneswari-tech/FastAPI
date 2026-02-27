from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse, UserLogin
from app.core.security import hash_password, verify_password, decode_access_token

class UserService:
    
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> UserResponse:
        existing_user = self.user_repo.get_user_by_email(user_data.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        user_dict = user_data.model_dump()
        user_dict['password'] = hash_password(user_dict['password'])
        user = self.user_repo.create_user(user_dict)
        return UserResponse.from_orm(user)

    def get_user_by_email(self, email: str) -> UserResponse:
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return UserResponse.from_orm(user)

    def update_user(self, email: str, update_data: UserUpdate) -> UserResponse:
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        update_dict = update_data.model_dump(exclude_unset=True)
        if 'password' in update_dict:
            update_dict['password'] = hash_password(update_dict['password'])
        
        updated_user = self.user_repo.update_user(email, update_dict)
        return UserResponse.from_orm(updated_user)

    def delete_user(self, email: str):
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        self.user_repo.delete_user(email)
