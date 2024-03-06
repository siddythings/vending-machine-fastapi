from app.models.users import User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create_user(db: Session, user: User):
    is_available = get_user_by_username(db, user)
    if is_available:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
        )

    db_user = User(
        username=user.username,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, user: User):
    db_user = db.query(User).filter_by(
        username=user.username
    ).one_or_none()
    return db_user


def get_user_by_id(db: Session, id):
    db_user = db.query(User).filter_by(
        id=id
    ).one_or_none()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    return db_user


def get_all_users(db: Session):
    return db.query(User).all()


def user_update(id, user: User, db: Session):
    user_details = get_user_by_id(db, id)
    is_username_available = get_user_by_username(db=db, user=user)
    if is_username_available and user_details.username != user.username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username not available to use, pick another"
        )

    update_query = {
        User.role: user.role,
        User.username: user.username
    }
    db.query(User).filter_by(id=id).update(update_query)
    db.commit()
    return db.query(User).filter_by(id=id).one()


def user_delete(id, db: Session):
    get_user_by_id(db, id)
    db.query(User).filter_by(id=id).delete()
    db.commit()
    return HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="User Deleted")
