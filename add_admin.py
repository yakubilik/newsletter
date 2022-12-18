from web_app.models import create_database, Admin

session = create_database()
admin = Admin(id=1,email="yakupkeskin777@gmail.com",password="admin",first_name="yakup")
session.add(admin)
session.commit()