from sql import Role, User, create_db, Session

def init_database():
    create_db()
    session = Session()

    try:

        admin_role = Role()
        admin_role.name = 'Админ'
        
        user_role = Role()
        user_role.name = 'Пользователь'

        session.add_all([admin_role, user_role])
        session.commit()


        admin = User()
        admin.fio = "Администратор Системы"
        admin.login = "admin"
        admin.password = "admin123"
        admin.role = admin_role
        admin.is_block = False
        
        session.add(admin)
        session.commit()
        print('База данных успешно инициализирована')

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    init_database()